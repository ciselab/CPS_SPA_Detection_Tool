#!/usr/bin/env python
"""
Searching through the diffs of each commit
"""
import os
import csv
import re

from git import Repo
from utils import get_csv_file
from pathlib import PurePosixPath
import dt.dict_repo_list
import dt.search_current
from utils import write_row_commits, write_row_line_v2
from git.exc import GitCommandError


results_long_list = []
save_results_at = "results_git_blame_4.txt"
dir_location_report = os.path.join("..", "results")
var_name = "var_with_number"
results_commits_name = "commits_PX4_Autopilot"
commits_list = []
count_errors_git = 0


def string_to_list(results):
    cleaned_up_results = []
    list_results = results.split("(")
    for each in list_results:
        if len(each) > 1:
            cleanup_1 = each.replace(")", "")
            cleanup_2 = cleanup_1.replace("]", "")
            cleanup_3 = cleanup_2.replace("'", "")
            cleanup_4 = cleanup_3.replace(" ", "")
            list_new = cleanup_4.split(",")
            list_two = list_new[:3]
            cleaned_up_results.append(list_two)
    return cleaned_up_results


def use_git_blame_better(file: str, url: str, results):
    """
    Args:
        file: full file path needed for git blame
        url: Path to the project repository (root of project)
        results: matching var name + var number
    Returns:
    """
    csv_file_commits = get_csv_file(results_commits_name)
    csv_wr_comm = csv.writer(
        csv_file_commits, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    csv_file_line = get_csv_file("long_results")
    csv_wr_line = csv.writer(
        csv_file_line, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    repo = Repo(url)
    commits_list.clear()
    for commit, lines in repo.blame(None, file):
        results_list = string_to_list(results)

        for each_results in results_list:
            regex_pattern = r"(\s+" + re.escape(each_results[0]) + "\s*=\s*([0-9]+))"
            for line_number, each_line in enumerate(lines):
                matching_patterns = re.findall(regex_pattern, each_line)
                if matching_patterns:
                    if matching_patterns[0][1] != each_results[1]:
                        print(f"match. pattern: {matching_patterns[0]}")
                        write_row_line_v2(csv_wr_line,
                                          matching_patterns[0][0], each_results,
                                          commit, file,  each_results[2], str(line_number))
        commits_list.append(commit)
    write_row_commits(csv_wr_comm, file, str(commits_list))


def csv_read():
    result_files = [f for f in os.listdir(os.path.join("..", "results"))]
    for each_file in result_files:
        if os.path.basename(each_file) == "var_with_number_results.csv":
            each_file_full_path = os.path.join("..", "results", each_file)
            if PurePosixPath(each_file_full_path).suffix != '.swp':
                with open(each_file_full_path) as results_csv_file:
                    fieldnames = ['file_name', 'results', 'encoding']
                    csv_reader = csv.DictReader(results_csv_file, fieldnames=fieldnames)
                    for line_number, row in enumerate(csv_reader):
                        dt.dict_repo_list.build_repo_dict()
                        url = dt.dict_repo_list.projects["PX4-Autopilot"]["local"]
                        try:
                            use_git_blame_better(row['file_name'], url, row['results'])
                        except GitCommandError:
                            # print(f"ERROR: GitCommandError...")
                            global count_errors_git
                            count_errors_git += 1
                            pass


def main():
    print("Starting")
    file_commits_results = os.path.join("..", "results", results_commits_name+"_results.csv")
    if os.path.exists(file_commits_results):
        print(f"File {file_commits_results} exists, removing file.")
        os.remove(file_commits_results)
    print("Start reading")
    csv_read()
    print(f"Amount of GitCommandErrors: {count_errors_git}")


if __name__ == "__main__":
    main()
