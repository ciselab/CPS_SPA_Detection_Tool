#!/usr/bin/env python
"""
Searching through previous versions of each file.
"""
import os
import csv
import re
from dt.utils import get_csv_file
from pathlib import PurePosixPath
import dt.dict_repo_list
import dt.search_current
from dt.utils import write_row_results
from datetime import datetime
import pydriller
import glob
from dataclasses import dataclass


# var_name = "numeric_function_within"
var_name = "sleeps"

list_results = []
delim_stand = u"\u25A0"


@dataclass
class Project:
    name: str = ""
    url_project: str = ""
    sha_project: str = ""
    final_results: str = ""


current_project = Project()


def cleanup_results_to_list_v2(start: str) -> list:
    """
    Change string input to list. String read from the .csv file containing results to be build back to a list.

    Args:
        start: String input that needs to be converted to list.

    Returns:
        cleaned_up_results: List of results (var name, var number, changed number, line before)
    """
    cleaned_up_results = []
    split = start.split("), (")
    for each in split:
        results_line_full = ""
        if len(each) > 1:
            data = each
            data = data.replace("[(", "")
            data = data.replace("', '\u25A0')]", "")
            data = data.replace("\\'", "\'")  # 4
            data_split = data.split(u", '\u25A0', '")

            results_line = data_split[1:]
            for items in results_line:
                results_line_full = results_line_full + items
            data_results = results_line_full
            data_results = data_results.replace("', '\u25A0'", "")  # multiple
            data_results = data_results.replace("\\t", "\t")
            data_results = data_results.replace("\\n", "\n")

            first_set = data_split[0]
            first_set = first_set.replace("'", "")
            first_set = first_set.replace(" ", "")
            data_input_final = first_set.split(",")

            results_com = (data_input_final[0], data_input_final[1], data_input_final[2], data_results.strip())
            cleaned_up_results.append(results_com)
    return cleaned_up_results


def csv_read(csv_wr_res):
    """
    Read .csv file, apply expected field names.
    Starts the git log follow function for each result from the .csv file.

    Args:
        csv_wr_res: csv.writer object, specifies .csv file.
    """
    result_files = [f for f in os.listdir(os.path.join("..", "results"))]
    counter_files = 0
    for each_file in result_files:
        if os.path.basename(each_file) == f"{var_name}_{current_project.name}_results.csv":
            each_file_full_path = os.path.join("..", "results", each_file)
            if PurePosixPath(each_file_full_path).suffix != '.swp':
                with open(each_file_full_path, 'r', encoding='utf-8') as results_csv_file:
                    fieldnames = ['file_name', 'results', 'encoding']
                    csv_reader = csv.DictReader(results_csv_file, fieldnames=fieldnames, delimiter=u"\u25A0")
                    for row in csv_reader:
                        dt.dict_repo_list.build_repo_dict()
                        file_path = row['file_name']
                        project_path_extra = current_project.url_project + "\\"
                        file_short = file_path.replace(project_path_extra, '')
                        check_follow(csv_wr_res, file_short, counter_files, file_path, row['results'], row['encoding'])
                        counter_files = counter_files + 1


def clean_git_log(log_results_path: str, encoding: str) -> dict:
    """
    Checks if the file passed contains the same pattern.

    Args:
        log_results_path:  Path to the file.
        encoding: Encoding used with this file.

    Returns:
        Overview of the results matching the pattern.
    """
    if encoding == "None":
        encoding = None
    dict_changed_files = {}
    last_name_change = None
    try:
        with open(log_results_path, 'r', encoding=encoding) as analyse_log_results:
            for each_line in analyse_log_results:
                pattern_commit = r"(commit)\s([0-9a-zA-Z]+)"
                # changed_file_pattern = r"^(:[0-9a-zA-Z]+\s[0-9a-zA-Z]+\s[0-9a-zA-Z]+" \
                #                        r"\s[0-9a-zA-Z]+\s[0-9a-zA-Z]+\s)([a-zA-Z0-9\/.-]+)\s([a-zA-Z0-9\/.-]+)\n"
                changed_file_pattern = r"^(:[0-9]+\s[0-9]+\s[0-9a-fA-F]+\s[0-9a-fA-F]+" \
                                       r"\s[0-9a-zA-Z]+\s)([a-zA-Z0-9\/.-_]*)\s([a-zA-Z0-9\/.-_]*)\n"

                matching_patterns_commit = re.match(pattern_commit, each_line)
                if matching_patterns_commit:
                    current_hash = matching_patterns_commit.groups()[1]
                    if last_name_change:
                        dict_changed_files[current_hash] = last_name_change
                    else:
                        dict_changed_files[current_hash] = None

                matching_patterns_changed_file = re.match(changed_file_pattern, each_line)
                if matching_patterns_changed_file:
                    dict_changed_files[current_hash] = (matching_patterns_changed_file.groups()[1],
                                                        matching_patterns_changed_file.groups()[2])
                    last_name_change = (matching_patterns_changed_file.groups()[1],
                                        matching_patterns_changed_file.groups()[2])
    except UnicodeDecodeError as e:
        with open("encoding_error.log", 'a') as ef_file:
            now = datetime.now()
            current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            ef_file.write(f"[{current_date_time}] {e}")
        pass

    return dict_changed_files


def check_follow(csv_wr_res, path_short: str, counter_files: int, path_long: str, results: str, encoding: str):
    """
    Using git log to follow when the file has been changed.

    Args:
        csv_wr_res: .csv writing object.
        path_short: Path from the project to the file.
        counter_files: Counter (log result file number).
        path_long: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: Encoding of the file.
    """
    current_wd = os.getcwd()
    dir_path = os.path.join("..", "..", current_project.name)
    os.chdir(f'{dir_path}')
    write_to_file = os.path.join(current_wd, "..", "results", "log_results_"+str(counter_files))
    os.system(f"git log --raw --follow {path_short} > {write_to_file}")

    dict_results = clean_git_log(write_to_file, encoding)
    analyse_file_checkout(dict_results, path_long, results, encoding, csv_wr_res)

    os.chdir(f'{current_wd}')


def print_found_results(path_long: str, each_hash: str, var_name_each: str, var_value_each, matching_patterns,
                        current_prev_line: str, result_prev_line: str, each_line: str):
    """
    Printing results in the console, same as is written to a file.
    Mainly used in development stage.
    Args:
        path_long: Location of the file (full path).
        each_hash: Current hash of the commit.
        var_name_each: Name current variable.
        var_value_each: Value of the variable to be compared with.
        matching_patterns: Matched pattern.
        current_prev_line: Currently analysed previous code line.
        result_prev_line: Stored from previous analysis stage.
        each_line: Current code line.
    """
    print(f"project name: {current_project.name}")
    print(f"file name: {path_long}")
    print(f"hash: {each_hash}")
    print(f"var name: {var_name_each}")
    print(f"var value 1: {var_value_each}")
    print(f"var value 2: {matching_patterns}")
    print(f"previous line current: {current_prev_line.strip()}")
    print(f"previous line stored: {result_prev_line.strip()}")
    print(f"current line: {each_line}")


def analyse_file_checkout(dict_results: dict, path_long: str, results: str, encoding: str, csv_wr_res):
    """
    Analysing the current file for the same pattern, var name with a changed var value.

    Args:
        dict_results: Dict of the git log results.
        path_long: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: File encoding.
        csv_wr_res: .csv writing object.
    """
    project_hash = current_project.sha_project
    local_project = current_project.url_project
    repo_check = pydriller.GitRepository(local_project)
    encoding_file = str(encoding)
    if encoding_file == "None":
        encoding_file = None

    results_list = cleanup_results_to_list_v2(results)
    var_value_each = {}

    for each_hash in dict_results.keys():
        repo_check.checkout(each_hash)

        if dict_results[each_hash]:
            path_long = dict_results[each_hash][0]

        for number_result, each_result_var in enumerate(results_list):
            var_name_each = each_result_var[0]
            result_prev_line = each_result_var[3]
            current_prev_line = ""

            if number_result not in var_value_each:
                var_value_each = {number_result: each_result_var[1]}
            """var_with_number"""
            # regex_pattern = r"\s+(" + re.escape(var_name_each) + r")\s*=\s*([0-9]+)"
            """numeric_function_within"""
            # regex_pattern = r"\s*\s*[a-zA-Z_]+\(" + re.escape(var_name_each) + r",\s([-0-9.]+)"
            """sleeps"""
            regex_pattern = r"^.*?" + re.escape(var_name_each) + r"\s*\(*([0-9]+)"
            try:
                with open(path_long, 'r', encoding=encoding_file) as analyse_file:
                    for line_number, each_line in enumerate(analyse_file):
                        matching_patterns = re.findall(regex_pattern, each_line)
                        if matching_patterns:
                            if matching_patterns[0] != var_value_each[number_result]:
                                if current_prev_line.strip() == result_prev_line.strip():
                                    write_row_results(csv_wr_res, current_project.name, path_long, each_hash,
                                                      var_name_each, each_result_var[1], matching_patterns[0])
                                    # print_found_results(path_long, each_hash, var_name_each, each_result_var[1],
                                    #                     matching_patterns[0], current_prev_line, result_prev_line,
                                    #                     each_line)
                                    var_value_each = {number_result: matching_patterns[0]}  # New comparison value
                        current_prev_line = each_line
            except FileNotFoundError as e:
                with open("error_file_not_found.log", 'a') as ef_file:
                    now = datetime.now()
                    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    ef_file.write(f"[{current_date_time}] {e}")
                pass
            except UnicodeDecodeError as e:
                with open("encoding_error.log", 'a') as ee_file:
                    now = datetime.now()
                    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    ee_file.write(f"[{current_date_time}] {e}")
                pass
    repo_check = pydriller.GitRepository(local_project)
    repo_check.checkout(project_hash)


def remove_log_files():
    """
    Remove all the log files.
    """
    hc_logs_path_part = os.path.join("..", "results", "log_results_")
    all_logs = hc_logs_path_part + "*"
    found_log_files = glob.glob(all_logs)
    if found_log_files:
        print(f"Log files exists, removing {len(found_log_files)} files.")
    for file in found_log_files:
        os.remove(file)


def hash_projects_to_file():
    """
    Writes projects current hash to file for backup purposes.
    """
    with open('hash_projects.txt', 'w') as writer:
        for project in dt.dict_repo_list.projects:
            writer.write(dt.dict_repo_list.projects[project]["local"])
            writer.write(" , ")
            writer.write(dt.dict_repo_list.projects[project]["sha"])
            writer.write("\n")


def main():
    """ BUILDING UP """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("Starting")
    dt.dict_repo_list.build_repo_dict()
    dt.dict_repo_list.build_repo_dict_sha()
    hash_projects_to_file()     # backup

    for name in dt.dict_repo_list.projects.keys():

        global current_project
        current_project = Project(name=name, url_project=dt.dict_repo_list.projects[name]["local"],
                                  sha_project=dt.dict_repo_list.projects[name]["sha"],
                                  final_results=f"{name}_{var_name}_final")

        """ REMOVING FILES """
        print(f"[{current_project.name}] Checking to remove files.")
        file_commits_results = os.path.join("..", "results", current_project.name+"_results.csv")
        if os.path.exists(file_commits_results):
            print(f"File {file_commits_results} exists, removing file.")
            os.remove(file_commits_results)

        hc_final_results_path = os.path.join("..", "results", current_project.final_results + "_results.csv")
        if os.path.exists(hc_final_results_path):
            print(f"File {hc_final_results_path} exists, removing file.")
            os.remove(hc_final_results_path)

        remove_log_files()

        """ START """
        print(f"[{current_project.name}] Start reading")
        csv_file_results = get_csv_file(current_project.final_results)
        csv_wr_res = csv.writer(
            csv_file_results, delimiter=u"\u25A0", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        csv_read(csv_wr_res)
        print(f"[{current_project.name}] Done")

    """ DONE """
    print(f"---COMPLETED ALL {len(dt.dict_repo_list.projects.keys())} PROJECTS---")
    remove_log_files()
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
