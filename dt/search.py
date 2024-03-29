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
import dt.ast_python as ast_python
import dt.dict_repo_list
# from dt import patterns
from dt.utils.csv import CsvWriter, CsvReader
from dt.utils.files import remove_file_if_exists, get_file_encoding, remove_log_files
from dt.utils.paths import results_base_path, project_results_path
from dt.utils.paths import logs_base_path, EnsurePathExistence
from dt.patterns import MAGICAL_WAITING_NUMBER


# GLOBAL PROCESSING UTILITIES
@dataclass
class Project:
    name: str = ""
    pattern_name: str = ""
    url_project: str = ""
    sha_project: str = ""
    language: str = "cpp"
    sel_modules: bool = True
    current_base_hash: str = ""

    def output_filename(self):
        if self.current_base_hash:
            pre_set = f"{self.current_base_hash}_"
        else:
            pre_set = ""
        return os.path.join(
            project_results_path(self.name),
            f"{pre_set}{self.pattern_name}_{self.name}_final.csv")

    def base_directory(self):
        return dt.dict_repo_list.projects[self.name]["local"]

    @EnsurePathExistence
    def result_path(self):
        if self.current_base_hash:
            pre_set = f"{self.current_base_hash}"
            res_name = f"{self.name}_{pre_set}"
        else:
            res_name = f"{self.name}"
        return os.path.join(results_base_path(), res_name)

    def intermediate_filename(self):
        if self.current_base_hash:
            pre_set = f"{self.current_base_hash}_"
        else:
            pre_set = ""
        return f"{pre_set}{self.pattern_name}_{self.name}_initial.csv"

    def pattern_filename(self, final=False):
        if self.current_base_hash:
            pre_set = f"{self.current_base_hash}_"
        else:
            pre_set = ""
        if final:
            return f"{pre_set}{self.pattern_name}_pattern_data_final.csv"
        else:
            return f"{pre_set}{self.pattern_name}_pattern_data_initial.csv"

    def files(self) -> set:
        file_set = set()
        # noinspection SpellCheckingInspection
        file_extensions: Dict[str, List[str]] = {
            'cpp': ['.c', '.cpp', '.h', '.hpp', '.cxx', '.cc', '.hh', '.h++'],
            'python': ['.py'],
        }
        # search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
        #                  '.ipp', '.inl', '.txx', '.tpp', '.tpl',
        #                  '.c++m', '.cppm', '.cxxm', '.kt',
        #                  '.java', '.go', '.py', '.rb', '.rs',
        #                  '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']

        if self.sel_modules:
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
        else:
            for root, dirs, files in os.walk(self.base_directory(), topdown=True):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    _, filename_ext = os.path.splitext(filename)
                    if filename_ext.lower() in file_extensions[self.language]:
                        file_set.add(file_path)

        return file_set


current_project = Project()


# INITIAL/GENERAL PROCESSING
def initial_search() -> None:
    # Set up results output file
    results_path = os.path.join(
        current_project.result_path(),
        current_project.intermediate_filename())
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
    write_pattern_data(pattern_occurrences, current_project.pattern_filename())


def write_pattern_data(pattern_occurrences, file_name: str = "pattern_data.csv"):
    data_path = os.path.join(current_project.result_path(), file_name)
    writer = CsvWriter(data_path)
    print(f'[{current_project.name}] {pattern_occurrences} possible occurrences '
          f'for {current_project.pattern_name}')
    writer.writerow([
        current_project.name, current_project.sha_project,
        current_project.pattern_name, pattern_occurrences])


def process_file(filename: os.path, encoding: str) -> Tuple[int, List]:
    abs_path = os.path.join(current_project.base_directory(), filename)
    if current_project.language == "python":
        return ast_python.parse_file(abs_path, encoding, current_project.pattern_name)
    else:
        return ast_cpp_antlr.parse_file(abs_path, encoding, current_project.pattern_name)   # C++


# HISTORY PROCESSING
def history_search() -> None:
    total_pattern_occurrences: int = 0
    # Clear old results
    remove_file_if_exists(current_project.output_filename())
    # Read the intermediate results
    result_file = os.path.join(
        current_project.result_path(),
        current_project.intermediate_filename())

    fieldnames = ['filename', 'encoding', 'result_count', 'results']
    with CsvReader(result_file, fieldnames=fieldnames) as reader:
        for row in reader:
            # Ignore files where no initial results were found
            if row['result_count'] == '0':
                continue
            relative_file_path = row['filename']
            encoding = row['encoding']
            initial_results = ast.literal_eval(row['results'])
            pattern_occurrences = process_file_history(
                relative_file_path,
                encoding,
                initial_results)

            total_pattern_occurrences = total_pattern_occurrences + pattern_occurrences
    write_pattern_data(total_pattern_occurrences, current_project.pattern_filename(final=True))


def process_file_history(relative_file_path: os.path, encoding: str, initial_results: List) -> int:
    pattern_occurrences: int = 0
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

        adjusted_newer_results = []
        if len(newer_results) > 0:
            for entry in newer_results:
                line = tuple((entry[0], entry[1], entry[3]))
                adjusted_newer_results.append(line)

        adjusted_results = []
        if len(results) > 0:
            for entry in results:
                line = tuple((entry[0], entry[1], entry[3]))
                adjusted_results.append(line)

            comp = DeepDiff(adjusted_newer_results, adjusted_results, ignore_order=True)

            if comp:
                if 'values_changed' in comp:
                    pattern_occurrences = pattern_occurrences + len(comp['values_changed'])
                if 'iterable_item_added' in comp:
                    pattern_occurrences = pattern_occurrences + len(comp['iterable_item_added'])
                if 'iterable_item_removed' in comp:
                    pattern_occurrences = pattern_occurrences + len(comp['iterable_item_removed'])
                csv_row = [relative_file_path, encoding,
                           commit_hash, results,
                           newer_filename, newer_commit_hash, newer_results]
                writer.writerow(csv_row)

        newer_commit_hash = commit_hash
        newer_results = results
        newer_filename = relative_file_path

    # checkout original commit
    repo.checkout(current_project.sha_project)
    return pattern_occurrences


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
    if Project.current_base_hash:
        pre_set = f"{Project.current_base_hash}_"
    else:
        pre_set = ""
    current_working_dir = os.getcwd()
    os.chdir(current_project.base_directory())
    log_file = os.path.join(logs_base_path(), f"history_{pre_set}{os.path.basename(rel_path)}.log")
    os.system(f"git log --raw --follow {rel_path} > {log_file}")
    filename_history = parse_git_log(log_file)
    os.chdir(current_working_dir)
    return filename_history


# Main Entry Point
def main(project_name: str = "Test_CPS_SPA_DT", pattern_name: str = MAGICAL_WAITING_NUMBER, sel_modules: bool = True,
         current_base_hash: str = "", history_project: bool = True, programming_language: str = "cpp"):
    start_time = datetime.now()
    start_time_fmt = start_time.strftime("%H:%M:%S")
    print(f"[Process] Start time: {start_time_fmt}")
    remove_log_files()

    global current_project
    if project_name not in dt.dict_repo_list.projects.keys():
        return

    current_project = Project(name=project_name,
                              pattern_name=pattern_name,
                              url_project=dt.dict_repo_list.projects[project_name]["local"],
                              sha_project=dt.dict_repo_list.projects[project_name]["sha"],
                              sel_modules=sel_modules,
                              language=programming_language,
                              current_base_hash=current_base_hash
                              )

    remove_file_if_exists(os.path.join(
        current_project.result_path(),
        current_project.pattern_filename()))
    remove_file_if_exists(os.path.join(
        current_project.result_path(),
        current_project.pattern_filename(final=True)))

    project_start_time = datetime.now()
    project_start_time_fmt = project_start_time.strftime("%H:%M:%S")
    print(f"\t[{current_project.name}] Start time: {project_start_time_fmt}")
    # Process current revision
    initial_search()
    # for interesting files, process history
    if history_project:
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
