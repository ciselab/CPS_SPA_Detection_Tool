#!/usr/bin/env python
"""
Searching through the current state of the repository.
"""
import ast
import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, List, Dict

import pydriller
from deepdiff import DeepDiff

import dt.ast_cpp_antlr as ast_cpp_antlr
import dt.dict_repo_list
from dt import patterns
from dt.utils.csv import CsvWriter, CsvReader
from dt.utils.files import remove_file_if_exists, get_file_encoding, remove_log_files
from dt.utils.paths import results_base_path, project_results_path, make_dir_if_not_exists, \
    logs_base_path


# GLOBAL PROCESSING UTILITIES
@dataclass
class Project:
    name: str = ""
    pattern_name: str = ""
    url_project: str = ""
    sha_project: str = ""
    language: str = "cpp"

    def output_filename(self):
        return os.path.join(project_results_path(self.name), f"{self.name}_{self.pattern_name}_final.csv")

    def base_directory(self):
        return dt.dict_repo_list.projects[self.name]["local"]

    def result_path(self):
        return os.path.join(results_base_path(), self.name)

    def intermediate_filename(self):
        return f"{self.pattern_name}_{self.name}_results.csv"

    def files(self) -> set:
        file_set = set()
        # noinspection SpellCheckingInspection
        file_extensions: Dict[str, List[str]] = {
            'cpp': ['.c', '.cpp', '.h', '.hpp', '.cxx', '.cc', '.hh', '.h++'],
        }
        # search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
        #                  '.ipp', '.inl', '.txx', '.tpp', '.tpl',
        #                  '.c++m', '.cppm', '.cxxm', '.kt',
        #                  '.java', '.go', '.py', '.rb', '.rs',
        #                  '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']

        for top_level, recursive in dt.dict_repo_list.projects_modules[self.name]:
            directory_path = os.path.join(self.base_directory(), top_level)
            for root, dirs, files in os.walk(directory_path, topdown=True):
                if not recursive:
                    dirs.clear()
                for filename in files:
                    file_path = os.path.join(root, filename)
                    _, filename_ext = os.path.splitext(filename)
                    if filename_ext.lower() in file_extensions[self.language]:
                        file_set.add(file_path)

        return file_set


current_project = Project()


def history_search_15(pattern_name: str) -> None:
    """
    Start the history search with received pattern.

    Args:
        pattern_name: Name of the pattern
    """
    for project_name in dt.dict_repo_list.projects.keys():
        global current_project
        current_project = Project(name=project_name, pattern_name=pattern_name,
                                  url_project=dt.dict_repo_list.projects[project_name]["local"],
                                  sha_project=dt.dict_repo_list.projects[project_name]["sha"])
        history_search()


def search_current(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    dt.dict_repo_list.build_repo_dict()
    dt.dict_repo_list.build_repo_dict_sha()
    initial_search()
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


# INITIAL/GENERAL PROCESSING
def initial_search() -> None:
    # Set up results output file
    results_path = os.path.join(current_project.result_path(), current_project.intermediate_filename())
    remove_file_if_exists(results_path)

    # Set up writer and counter for intermediate results
    writer = CsvWriter(results_path)
    pattern_occurrences: int = 0
    for filename in current_project.files():
        file_encoding = get_file_encoding(filename)
        relative_filename = os.path.relpath(filename, start=current_project.base_directory())

        count, results = process_file(relative_filename, file_encoding)
        pattern_occurrences += count
        csv_row = [relative_filename, file_encoding, count, results]
        writer.writerow(csv_row)
    write_pattern_data(
        current_project.name,
        current_project.sha_project,
        current_project.pattern_name,
        pattern_occurrences)


def write_pattern_data(project_name, project_hash, pattern_name, pattern_occurrences):
    data_path = os.path.join(results_base_path(), f"pattern_data.csv")
    writer = CsvWriter(data_path)
    print(f'[{project_name}] {pattern_occurrences} occurrences for {pattern_name}')
    writer.writerow([project_name, project_hash, pattern_name, pattern_occurrences])


def process_file(filename: os.path, encoding: str) -> Tuple[int, List]:
    abs_path = os.path.join(current_project.base_directory(), filename)
    return ast_cpp_antlr.parse_file(abs_path, encoding, current_project.pattern_name)
    # return ast_cpp_antlr.main(None, abs_path, encoding, current_project.pattern_name)


# HISTORY PROCESSING
def history_search() -> None:
    # Clear old results
    remove_file_if_exists(current_project.output_filename())
    # Read the intermediate results
    result_file = os.path.join(current_project.result_path(), current_project.intermediate_filename())
    fieldnames = ['filename', 'encoding', 'result_count', 'results']
    with CsvReader(result_file, fieldnames=fieldnames) as reader:
        for row in reader:
            relative_file_path = row['filename']
            encoding = row["encoding"]
            initial_results = ast.literal_eval(row["results"])
            process_file_history(relative_file_path, encoding, initial_results)


def process_file_history(relative_file_path: os.path, encoding: str, initial_results: List) -> None:
    # Open a file writer to append newly found results
    writer = CsvWriter(current_project.output_filename())
    # Gather the current file's history and instantiate a repo object
    file_history = get_file_history(relative_file_path)
    repo = pydriller.GitRepository(current_project.url_project)
    # General state for processing
    first_commit_skipped: bool = False
    newer_commit_hash = ""
    newer_results = initial_results
    newer_filename = relative_file_path

    for commit_hash in file_history.keys():
        if not first_commit_skipped:
            newer_commit_hash = commit_hash
            first_commit_skipped = True
            continue

        if file_history[commit_hash] is not None:
            relative_file_path = file_history[commit_hash]

        repo.checkout(commit_hash)

        _, results = process_file(relative_file_path, encoding)
        # print(f"{newer_commit_hash=} {newer_results=}")
        # print(f"{commit_hash=} {results=}\n")

        comp = DeepDiff(newer_results, results, ignore_order=True)
        if comp:
            csv_row = [relative_file_path, encoding,
                       commit_hash, results,
                       newer_filename, newer_commit_hash, newer_results]
            writer.writerow(csv_row)

        newer_commit_hash = commit_hash
        newer_results = results
        newer_filename = relative_file_path

    # checkout original commit
    repo.checkout(current_project.sha_project)


def parse_git_log(log_file: os.path) -> Dict[str, str]:
    """
    Checks if the file passed contains the same pattern.

    Args:
        log_file:  Path to the git log file.

    Returns:
        A Dictionary with commit hashes that tracks filenames throughout its history.
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

    with open(log_file, 'r') as log_results:
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


def get_file_history(rel_path: os.path) -> Dict[str, str]:
    current_working_dir = os.getcwd()
    os.chdir(current_project.base_directory())
    log_file = os.path.join(logs_base_path(), f"history_{os.path.basename(rel_path)}.log")
    os.system(f"git log --raw --follow {rel_path} > {log_file}")
    filename_history = parse_git_log(log_file)
    os.chdir(current_working_dir)
    return filename_history


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


def hash_projects_to_file() -> None:
    """
    Writes projects current hash to file for backup purposes.
    """
    hash_file = os.path.join(results_base_path(), "intermediate", "hash_projects.txt")
    make_dir_if_not_exists(os.path.dirname(hash_file))
    with open(hash_file, 'w') as writer:
        for project in dt.dict_repo_list.projects.values():
            writer.write(f"{project['local']} , {project['sha']}\n")


def search_current_history(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
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
        remove_file_if_exists(current_project.output_filename())
        remove_log_files()

        """ START """
        print(f"[{current_project.name}] Start reading")
        # csv_writer = CsvWriter(current_project.output_filename())

        # csv_read(csv_writer, pattern_name)
        history_search()
        print(f"[{current_project.name}] Done")

    """ DONE """
    print(f"---COMPLETED ALL {len(dt.dict_repo_list.projects.keys())} PROJECTS---")
    remove_log_files()
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


# Main Entry Point
def main(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
    start_time = datetime.now()
    start_time_fmt = start_time.strftime("%H:%M:%S")
    print(f"[Process] Start time: {start_time_fmt}")
    dt.dict_repo_list.build_repo_dict()
    dt.dict_repo_list.build_repo_dict_sha()
    remove_log_files()

    global current_project
    for project_name in dt.dict_repo_list.projects.keys():
        current_project = Project(name=project_name,
                                  pattern_name=pattern_name,
                                  url_project=dt.dict_repo_list.projects[project_name]["local"],
                                  sha_project=dt.dict_repo_list.projects[project_name]["sha"])
        project_start_time = datetime.now()
        project_start_time_fmt = project_start_time.strftime("%H:%M:%S")
        print(f"\t[{current_project.name}] Start time: {project_start_time_fmt}")
        # Process current revision
        initial_search()
        # for interesting files, process history
        history_search()
        # Print end time and duration
        project_end_time = datetime.now()
        project_end_time_fmt = datetime.now().strftime("%H:%M:%S")
        print(f"\t[{current_project.name}] End time: {project_end_time_fmt}, "
              f"duration: {project_end_time - project_start_time}")

    end_time = datetime.now()
    end_time_fmt = start_time.strftime("%H:%M:%S")
    print(f"[Process] End time: {end_time_fmt}, "
          f"duration: {end_time - start_time}")
    remove_log_files()


if __name__ == "__main__":
    main()
