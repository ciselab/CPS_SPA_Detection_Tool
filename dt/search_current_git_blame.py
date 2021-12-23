#!/usr/bin/env python
"""
Searching through the diffs of each commit
"""
import os
import csv
import re
from utils import get_csv_file
from pathlib import PurePosixPath
import dt.dict_repo_list
import dt.search_current
from utils import write_row_results
from datetime import datetime
import pydriller


# var_name = "numeric_function_within"
var_name = "sleeps"
var_results_file_name = var_name + "_results.csv"
results_commits_name = "commits_PX4_Autopilot"
list_results = []
delim_stand = u"\u25A0"


def cleanup_results_to_list(start):
    cleaned_up_results = []
    start_split = start.split(u"\u25A0'), ((")
    for each in start_split:
        results_line_full = ""
        if len(each) > 1:
            data = each.replace("\'", "")
            data = data.replace("[", "")
            data = data.replace(", \u25A0)]", "")
            data = data.replace(" ", "")        # Needs to be replaced by something else
            data = data.replace("((", "")
            data = data.replace(",\u25A0]", "")
            data = data.replace(")", "")
            data_split = data.split(u",\u25A0,")
            results_line = data_split[1:]
            for items in results_line:
                results_line_full = results_line_full + items
            data_results = results_line_full.replace("\\t", "\t")
            data_results = data_results.replace("\\n", "\n")
            first_set = data_split[0]
            data_input_final = first_set.split(",")
            results_com = (data_input_final[0], data_input_final[1], data_input_final[2], data_results)
            cleaned_up_results.append(results_com)
    return cleaned_up_results


def csv_read(csv_wr_res):
    result_files = [f for f in os.listdir(os.path.join("..", "results"))]
    counter_files = 0
    for each_file in result_files:
        if os.path.basename(each_file) == var_results_file_name:
            each_file_full_path = os.path.join("..", "results", each_file)
            if PurePosixPath(each_file_full_path).suffix != '.swp':
                with open(each_file_full_path, encoding='utf-8') as results_csv_file:
                    fieldnames = ['file_name', 'results', 'encoding']
                    csv_reader = csv.DictReader(results_csv_file, fieldnames=fieldnames, delimiter=u"\u25A0")
                    for row in csv_reader:
                        dt.dict_repo_list.build_repo_dict()
                        url = dt.dict_repo_list.projects["PX4-Autopilot"]["local"]
                        file_path = row['file_name']
                        project_path_extra = url + "\\"
                        file_short = file_path.replace(project_path_extra, '')
                        check_follow(csv_wr_res, file_short, counter_files, file_path, row['results'], row['encoding'])
                        counter_files = counter_files + 1


def clean_git_log(log_results_path: str, encoding):
    if encoding == "None":
        encoding = None
    dict_changed_files = {}
    last_name_change = None
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

    return dict_changed_files


def check_follow(csv_wr_res, path_short, counter_files, path_long, results, encoding):
    current_wd = os.getcwd()
    dir_path = os.path.join("..", "..", "PX4-Autopilot")
    os.chdir(f'{dir_path}')
    write_to_file = os.path.join(current_wd, "..", "results", "log_results_"+str(counter_files))
    os.system(f"git log --raw --follow {path_short} > {write_to_file}")

    dict_results = clean_git_log(write_to_file, encoding)
    analyse_file_checkout("PX4-Autopilot", dict_results, path_long, results, encoding, csv_wr_res)

    os.chdir(f'{current_wd}')


def print_information(csv_wr_res, project_name, file_name_full_path,
                      commit_hash, search_var_name, var_value, var_value_found):
    # print("Found variable changes:")
    # print(f"Project: {project_name}")
    # print(f"File: {file_name_full_path}")
    # print(f"Commit hash: {commit_hash}")
    # print(f"{search_var_name} : {var_value} -> {var_value_found}")
    # print("\n---\n")
    write_row_results(csv_wr_res, project_name, file_name_full_path,
                      commit_hash, search_var_name, var_value, var_value_found)


def analyse_file_checkout(project, dict_results, path_long, results, encoding, csv_wr_res):
    project_hash = dt.dict_repo_list.projects[project]["sha"]
    local_project = dt.dict_repo_list.projects[project]["local"]
    repo_check = pydriller.GitRepository(local_project)
    encoding_file = str(encoding)
    if encoding_file == "None":
        encoding_file = None

    results_list = cleanup_results_to_list(results)
    first_check = True
    same_var_name_comp = None

    for each_hash in dict_results.keys():
        repo_check.checkout(each_hash)

        if dict_results[each_hash]:
            path_long = dict_results[each_hash][0]

        results_file = []
        for each_result_var in results_list:
            var_name_each = each_result_var[0]
            result_prev_line = each_result_var[3]
            current_prev_line = ""

            if first_check:
                if same_var_name_comp != var_name_each:
                    var_value_each = each_result_var[1]
                    first_check = False
            """var_with_number"""
            # regex_pattern = r"\s+(" + re.escape(var_name_each) + r")\s*=\s*([0-9]+)"
            """numeric_function_within"""
            # regex_pattern = r"\s*\s*[a-zA-Z_]+\(" + re.escape(var_name_each) + r",\s([-0-9.]+)"
            """sleeps"""
            regex_pattern = r"^.*?" + re.escape(var_name_each) + r"\s*\(*([0-9]+)"
            try:
                with open(path_long, 'r', encoding=encoding_file) as analyse_file:
                    for each_line in analyse_file:
                        matching_patterns = re.findall(regex_pattern, each_line)
                        results_pattern_with_var_name = (var_name_each, matching_patterns)
                        if matching_patterns:
                            results_file.append(results_pattern_with_var_name)
                            if matching_patterns[0] != var_value_each:
                                # print(f"comparison: {current_prev_line} VS {result_prev_line}")
                                # print(f"hash: {each_hash}, path: {path_long}")
                                if current_prev_line == result_prev_line:
                                    print_information(csv_wr_res, local_project, path_long, each_hash,
                                                      var_name_each, var_value_each, matching_patterns[0])
                                    var_value_each = matching_patterns[0]       # New comparison value
                                    same_var_name_comp = var_name_each
                        current_prev_line = each_line
            except FileNotFoundError as e:
                with open("error_file_not_found.log", 'a') as ef_file:
                    now = datetime.now()
                    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    ef_file.write(f"[{current_date_time}] {e}")
                pass
    repo_check = pydriller.GitRepository(local_project)
    repo_check.checkout(project_hash)


def hash_projects_to_file():
    print(dt.dict_repo_list.projects["PX4-Autopilot"])
    with open('hash_projects.txt', 'w') as writer:
        for project in dt.dict_repo_list.projects:
            writer.write(dt.dict_repo_list.projects[project]["local"])
            writer.write(" , ")
            writer.write(dt.dict_repo_list.projects[project]["sha"])
            writer.write("\n")


def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("Starting")
    dt.dict_repo_list.build_repo_dict()
    dt.dict_repo_list.build_repo_dict_sha()
    hash_projects_to_file()     # backup

    file_commits_results = os.path.join("..", "results", results_commits_name+"_results.csv")
    if os.path.exists(file_commits_results):
        print(f"File {file_commits_results} exists, removing file.")
        os.remove(file_commits_results)
    print("Start reading")
    csv_file_results = get_csv_file("final_two")
    csv_wr_res = csv.writer(
        csv_file_results, delimiter=u"\u25A0", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    csv_read(csv_wr_res)
    print("Done")

    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
