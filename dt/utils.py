#!/usr/bin/env python
"""
Common for utils.
"""
import os
from os import path
from typing import Optional
import pathlib

location = path.join(pathlib.Path.home(), "CPS_SPA_Detection_Tool", "results", "repo")
dir_location_report = os.path.join("..", "results")


def build_results_path(project: str) -> [str, Optional]:
    """
    Building the path to where the results file should be, checks if exists.

    Args:
        project: Name of the project.

    Returns:
        - Path to the project results file (containing commit hashes).
        - None if path does not exists.

    """
    project_name = str(project + '.txt')
    hash_file_location = path.join(location, project_name)
    if path.exists(hash_file_location):
        return hash_file_location
    else:
        return None


def list_file_content(file_location: str) -> list:
    """
    Reads the file and converts the content to a list, an entry for each line.

    Args:
        file_location: Location of the file.

    Returns:
        list_content_file: List of content read from the file.

    """
    list_content_file = []
    content_file = open(file_location, 'r')
    for line in content_file:
        list_content_file.append(line)
    content_file.close()
    return list_content_file


def get_csv_file(addition_name: str):
    results_file_name = addition_name + "_results.csv"
    if not os.path.exists(os.path.abspath(dir_location_report)):
        os.makedirs(dir_location_report)
    full_path_results_file = os.path.join(dir_location_report, results_file_name)
    return open(full_path_results_file, "a", encoding='utf-8')


def write_row(csv_writer, file: str, results: str, encoding: str):
    csv_line = [file, results, encoding]
    csv_writer.writerow(csv_line)


def write_row_commits(csv_writer_commits, file: str, commits: str, results, encoding: str):
    csv_line_commits = [file, commits, results, encoding]
    csv_writer_commits.writerow(csv_line_commits)


def write_row_line(csv_writer_commits, input_line: str):
    csv_line_commits = [input_line]
    csv_writer_commits.writerow(csv_line_commits)


def write_row_line_v2(csv_writer_commits,
                      pattern: str, found_pattern: str, commit_hash: str, file: str,
                      line_number_org: str, line_number_new: str):
    csv_line_commits = [pattern, found_pattern, commit_hash, file, line_number_org, line_number_new]
    csv_writer_commits.writerow(csv_line_commits)


def write_row_results(csv_writer_commits,
                      project_name: str, file_name_full_path: str, commit_hash: str,
                      search_var_name: str, var_value: str, var_value_found: str):
    csv_line_commits = [project_name, file_name_full_path, commit_hash, search_var_name, var_value, var_value_found]
    csv_writer_commits.writerow(csv_line_commits)
