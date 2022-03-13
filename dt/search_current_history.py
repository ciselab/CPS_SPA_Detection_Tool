#!/usr/bin/env python
"""
Searching through previous versions of each file.
"""
import ast
import glob
import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple

import pydriller
from deepdiff import DeepDiff

import dt.ast_cpp_antlr as ast_cpp_antlr
import dt.dict_repo_list
import dt.search_current
from dt.utils.csv import write_row, CsvWriter, CsvReader
from dt.utils.files import remove_file_if_exists
from dt.utils.paths import results_base_path, make_dir_if_not_exists, project_results_path, logs_base_path

hc_counter = 0


@dataclass
class Project:
    name: str = ""
    pattern_name: str = ""
    url_project: str = ""
    sha_project: str = ""

    def get_output_filename(self):
        return os.path.join(project_results_path(self.name), f"{self.name}_{self.pattern_name}_final.csv")


current_project = Project()
location_log_files = os.path.join(dt.dict_repo_list.location_github, "CPS_SPA_Detection_Tool", "results")


def csv_read(csv_wr_res, pattern_name: str) -> None:
    """
    Read .csv file, apply expected field names.
    Starts the git log follow function for each result from the .csv file.

    Args:
        csv_wr_res: csv.writer object, specifies .csv file.
        pattern_name: Used pattern name.
    """
    result_files = [f for f in os.listdir(project_results_path(current_project.name))]

    for counter_files, current_file in enumerate(result_files):
        if not os.path.basename(current_file) == f"{pattern_name}_{current_project.name}_results.csv":
            continue
        full_file_path = os.path.join(project_results_path(current_project.name), current_file)
        fieldnames = ['file_name', 'encoding', 'result_count', 'results']
        with CsvReader(full_file_path, fieldnames=fieldnames) as reader:
            for row in reader:
                print(f"{row=}")
                relative_file_path = row['file_name']
                absolute_file_path = os.path.join(current_project.url_project, relative_file_path)
                print(f"{row['encoding']=}")
                check_follow(
                    csv_wr_res,
                    relative_file_path,
                    counter_files,
                    absolute_file_path,
                    row['results'], row['encoding'],
                    pattern_name)


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
        print(f"{encoding=}")
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
        error_enc = os.path.join(location_log_files, "encoding_error.log")
        with open(error_enc, 'a') as ef_file:
            now = datetime.now()
            current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            ef_file.write(f"[{current_date_time}] {e}")
        pass

    return dict_changed_files


def check_follow(csv_wr_res, path_short: str, counter_files: int, path_long: str, results: str, encoding: str,
                 pattern_name: str) -> None:
    """
    Using git log to follow when the file has been changed.

    Args:
        csv_wr_res: .csv writing object.
        path_short: Path from the project to the file.
        counter_files: Counter (log result file number).
        path_long: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: Encoding of the file.
        pattern_name: Pattern name of pattern used.
    """
    current_wd = os.getcwd()
    dir_path = os.path.join("..", "..", current_project.name)
    os.chdir(dir_path)
    write_to_file = os.path.join(logs_base_path(), f"log_results_{counter_files}")
    os.system(f"git log --raw --follow {path_short} > {write_to_file}")

    dict_results = clean_git_log(write_to_file, encoding)
    analyse_file_checkout(dict_results, path_long, results, encoding, csv_wr_res, pattern_name)

    os.chdir(current_wd)


def print_found_results(path_long: str, compared_hash: str, each_hash: str, var_name_each: str, var_value_each,
                        matching_patterns, current_prev_line: str, result_prev_line: str, each_line: str) -> None:
    """
    Printing results in the console, same as is written to a file.
    Mainly used in development stage.
    Args:
        path_long: Location of the file (full path).
        compared_hash: Hash from which the var is compared to.
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
    print(f"compared hash: {compared_hash}")
    print(f"hash: {each_hash}")
    print(f"var name: {var_name_each}")
    print(f"var value 1: {var_value_each}")
    print(f"var value 2: {matching_patterns}")
    print(f"previous line current: {current_prev_line.strip()}")
    print(f"previous line stored: {result_prev_line.strip()}")
    print(f"current line: {each_line}")


def searching_using_antlr(csv_wr_res, path_long, pattern_name, previous_result, current_hash, previous_hash,
                          encoding_file):
    number_results: int
    result: List[Tuple[int, str, str]]
    print(f'{path_long=}')
    number_results, result = ast_cpp_antlr.main(csv_wr_res, path_long, pattern_name, previous_result, current_hash,
                                                previous_hash)
    if result != 0:
        # comp = set(results_list).symmetric_difference(set(result))
        # comp = set(results_list) ^ (set(result))
        # comp = [item for item in results_list if item not in result]
        comp = DeepDiff(previous_result, result, ignore_order=True)
        # print(f"HISTORY: {result=}")
        # print(f"COMPARE: {results_list=}")
        # print(f"\n{comp=}\n")
        if comp:
            # print("\nGOING THROUGH THE HISTORY")
            # print(f"{result=}")
            # print(f"{current_hash=}")
            # print("COMPARE WITH")
            # print(f"{previous_result=}")
            # print(f"{previous_hash=}")
            # print(f"{comp=}\n")
            write_row(csv_wr_res, path_long, result, encoding_file, previous_result, current_hash, previous_hash,
                      caller='history')
            return result
        else:
            return previous_result


def analyse_file_checkout(dict_results: dict, path_long: str, results: str, encoding: str, csv_wr_res,
                          pattern_name: str) -> None:
    """
    Analysing the current file for the same pattern, var name with a changed var value.

    Args:
        dict_results: Dict of the git log results.
        path_long: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: File encoding.
        csv_wr_res: .csv writing object.
        pattern_name: Pattern name of pattern used.
    """
    project_hash = current_project.sha_project
    local_project = current_project.url_project
    repo_check = pydriller.GitRepository(local_project)
    encoding_file = str(encoding)
    if encoding_file == "None":
        encoding_file = None

    results_list = ast.literal_eval(results)

    global hc_counter
    hc_counter = hc_counter + 1

    previous_hash = project_hash

    for each_hash in dict_results.keys():
        repo_check.checkout(each_hash)

        if dict_results[each_hash]:  # Used if filename has been changed.
            path_long = dict_results[each_hash][0]

        results_list = searching_using_antlr(csv_wr_res, path_long, pattern_name, results_list, each_hash,
                                             previous_hash, encoding_file)
        previous_hash = each_hash

    repo_check = pydriller.GitRepository(local_project)
    repo_check.checkout(project_hash)


def remove_log_files() -> None:
    """
    Remove all the log files.
    """
    hc_logs_path = os.path.join(logs_base_path(), "log_results_*")
    log_files_list = glob.glob(hc_logs_path)
    if log_files_list:
        print(f"Log files exist, removing {len(log_files_list)} files.")
    for file in log_files_list:
        os.remove(file)


def hash_projects_to_file() -> None:
    """
    Writes projects current hash to file for backup purposes.
    """
    hash_file = os.path.join(results_base_path(), "intermediate", "hash_projects.txt")
    make_dir_if_not_exists(os.path.dirname(hash_file))
    with open(hash_file, 'w') as writer:
        for project in dt.dict_repo_list.projects.values():
            writer.write(f"{project['local']} , {project['sha']}\n")


def main(pattern_name: str = "sleeps") -> None:
    """ BUILDING UP """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("Starting")
    dt.dict_repo_list.build_repo_dict()
    dt.dict_repo_list.build_repo_dict_sha()
    hash_projects_to_file()  # backup

    for name in dt.dict_repo_list.projects.keys():
        global current_project
        current_project = Project(name=name, pattern_name=pattern_name,
                                  url_project=dt.dict_repo_list.projects[name]["local"],
                                  sha_project=dt.dict_repo_list.projects[name]["sha"])

        """ REMOVING FILES """
        hc_final_results_path = current_project.get_output_filename()
        remove_file_if_exists(hc_final_results_path)

        remove_log_files()

        """ START """
        print(f"[{current_project.name}] Start reading")
        csv_writer = CsvWriter(current_project.get_output_filename())

        csv_read(csv_writer, pattern_name)
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
