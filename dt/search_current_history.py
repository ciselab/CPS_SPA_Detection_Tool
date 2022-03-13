#!/usr/bin/env python
"""
Searching through previous versions of each file.
"""
import ast
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
from dt import patterns
from dt.utils.csv import CsvWriter, CsvReader
from dt.utils.files import remove_file_if_exists, remove_log_files
from dt.utils.paths import results_base_path, make_dir_if_not_exists, project_results_path, logs_base_path, \
    project_base_path


@dataclass
class Project:
    name: str = ""
    pattern_name: str = ""
    url_project: str = ""
    sha_project: str = ""

    def get_output_filename(self):
        return os.path.join(project_results_path(self.name), f"{self.name}_{self.pattern_name}_final.csv")


current_project = Project()


def csv_read(csv_writer, pattern_name: str) -> None:
    """
    Read .csv file, apply expected field names.
    Starts the git log follow function for each result from the .csv file.

    Args:
        csv_writer: csv.writer object, specifies .csv file.
        pattern_name: Used pattern name.
    """
    result_file = os.path.join(
        project_results_path(current_project.name),
        f'{pattern_name}_{current_project.name}_results.csv')

    fieldnames = ['filename', 'encoding', 'result_count', 'results']
    with CsvReader(result_file, fieldnames=fieldnames) as reader:
        for row in reader:
            relative_file_path = row['filename']
            absolute_file_path = os.path.join(current_project.url_project, relative_file_path)
            check_follow(csv_writer, relative_file_path, absolute_file_path, row['results'], row['encoding'],
                         pattern_name)


def parse_git_log(log_results_path: str) -> dict:
    """
    Checks if the file passed contains the same pattern.

    Args:
        log_results_path:  Path to the file.

    Returns:
        Overview of the results matching the pattern.
    """
    # RE PATTERNS
    pattern_commit = r"commit\s" \
                     r"([0-9a-zA-Z]+)"
    changed_file_pattern = r"^:[0-9]+\s[0-9]+\s[0-9a-fA-F]+\s[0-9a-fA-F]+\s[0-9a-zA-Z]+\s" \
                           r"([a-zA-Z0-9\/.-_]*)\s" \
                           r"([a-zA-Z0-9\/.-_]*)"

    # local data
    filename_history = {}
    last_name = None

    with open(log_results_path, 'r') as log_results:
        for line in log_results:
            matching_patterns_commit = re.match(pattern_commit, line)
            if matching_patterns_commit:
                current_hash = matching_patterns_commit.groups()[0]
                if last_name:
                    filename_history[current_hash] = last_name
                else:
                    filename_history[current_hash] = None

            matching_patterns_changed_file = re.match(changed_file_pattern, line)
            if matching_patterns_changed_file:
                match_groups = matching_patterns_changed_file.groups()
                if len(match_groups[1]) > 0:  # we found a rename
                    filename_history[current_hash] = match_groups[1]
                    last_name = match_groups[0]

    return filename_history


def check_follow(csv_writer, rel_path: str, abs_path: str, results: str, encoding: str, pattern_name: str) -> None:
    """
    Using git log to follow when the file has been changed.

    Args:
        csv_writer: .csv writing object.
        rel_path: Path from the project to the file.
        abs_path: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: Encoding of the file.
        pattern_name: Pattern name of pattern used.
    """
    current_wd = os.getcwd()
    os.chdir(project_base_path(current_project.name))
    write_to_file = os.path.join(logs_base_path(), f"log_results_{current_project.name}")
    os.system(f"git log --raw --follow {rel_path} > {write_to_file}")

    filename_history = parse_git_log(write_to_file)
    analyse_file_checkout(filename_history, abs_path, results, encoding, csv_writer, pattern_name)

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


def searching_using_antlr(csv_writer, abs_path, pattern_name, previous_result, current_hash, previous_hash,
                          encoding_file):
    number_results: int
    parse_results: List[Tuple[int, str, str]]
    number_results, parse_results = ast_cpp_antlr.main(csv_writer, abs_path, pattern_name,
                                                       previous_result, current_hash, previous_hash)
    if len(parse_results) != 0:
        rel_path = os.path.relpath(abs_path, start=current_project.url_project)
        # comp = set(results_list).symmetric_difference(set(parse_results))
        # comp = set(results_list) ^ (set(parse_results))
        # comp = [item for item in results_list if item not in parse_results]
        comp = DeepDiff(previous_result, parse_results, ignore_order=True)
        # print(f"HISTORY: {parse_results=}")
        # print(f"COMPARE: {results_list=}")
        # print(f"\n{comp=}\n")
        if comp:
            # print("\nGOING THROUGH THE HISTORY")
            # print(f"{parse_results=}")
            # print(f"{current_hash=}")
            # print("COMPARE WITH")
            # print(f"{previous_result=}")
            # print(f"{previous_hash=}")
            # print(f"{comp=}\n")
            csv_row = [rel_path, encoding_file,
                       current_hash, parse_results,
                       previous_hash, previous_result]
            csv_writer.writerow(csv_row)
            return parse_results
        else:
            return previous_result


def analyse_file_checkout(filename_history: dict, path_long: str, results: str, encoding: str, csv_writer,
                          pattern_name: str) -> None:
    """
    Analysing the current file for the same pattern, var name with a changed var value.

    Args:
        filename_history: Dictionary tracking file renames throughout commits.
        path_long: Full path to the file.
        results: Results contain var name and value and previous line.
        encoding: File encoding.
        csv_writer: .csv writing object.
        pattern_name: Pattern name of pattern used.
    """
    project_hash = current_project.sha_project
    local_project = current_project.url_project
    repo_check = pydriller.GitRepository(local_project)
    encoding_file = str(encoding)
    if encoding_file == "None":
        encoding_file = None

    results_list = ast.literal_eval(results)

    previous_hash = project_hash

    for commit_hash in filename_history.keys():
        repo_check.checkout(commit_hash)

        if filename_history[commit_hash]:  # Used if filename has been changed.
            path_long = filename_history[commit_hash]

        results_list = searching_using_antlr(csv_writer, path_long, pattern_name, results_list, commit_hash,
                                             previous_hash, encoding_file)
        previous_hash = commit_hash

    repo_check = pydriller.GitRepository(local_project)
    repo_check.checkout(project_hash)


def hash_projects_to_file() -> None:
    """
    Writes projects current hash to file for backup purposes.
    """
    hash_file = os.path.join(results_base_path(), "intermediate", "hash_projects.txt")
    make_dir_if_not_exists(os.path.dirname(hash_file))
    with open(hash_file, 'w') as writer:
        for project in dt.dict_repo_list.projects.values():
            writer.write(f"{project['local']} , {project['sha']}\n")


def main(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
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
        remove_file_if_exists(current_project.get_output_filename())
        remove_log_files()

        """ START """
        print(f"[{current_project.name}] Start reading")
        csv_writer = CsvWriter(current_project.get_output_filename())

        csv_read(csv_writer, pattern_name)
        print(f"[{current_project.name}] Done")

    """ DONE """
    print(f"---COMPLETED ALL {len(dt.dict_repo_list.projects.keys())} PROJECTS---")
    # remove_log_files()
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
