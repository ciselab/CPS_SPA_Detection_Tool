#!/usr/bin/env python
"""
Searching through the current state of the repository.
"""
import os
from datetime import datetime
from typing import Tuple, List

import dt.ast_cpp_antlr as ast_cpp_antlr
import dt.dict_repo_list
from dt import patterns
from dt.utils.csv import CsvWriter
from dt.utils.files import get_project_files, remove_file_if_exists, intermediary_results_filename, \
    get_file_encoding
from dt.utils.paths import results_base_path, project_base_path, project_results_path


def process_project(project_name: str, pattern_name: str, write_pattern: bool = False) -> None:
    # Set up results output file
    results_path = os.path.join(
        project_results_path(project_name),
        intermediary_results_filename(project_name, pattern_name))
    remove_file_if_exists(results_path)

    # Set up writer and counter for intermediate results
    writer = CsvWriter(results_path)
    pattern_occurrences: int = 0
    for filename in get_project_files(project_name):
        file_encoding = get_file_encoding(filename)
        relative_filename = os.path.relpath(filename, start=project_base_path(project_name))

        count, results = process_file(filename, pattern_name)
        pattern_occurrences += count
        csv_row = [relative_filename, file_encoding, count, results]
        writer.writerow(csv_row)
    if write_pattern:
        write_pattern_data(pattern_name, dt.dict_repo_list.projects[project_name]['sha'], pattern_occurrences, project_name)


def write_pattern_data(project_name, project_hash, pattern_name, pattern_occurrences):
    data_path = os.path.join(results_base_path(), f"pattern_data.csv")
    writer = CsvWriter(data_path)
    print(f'[{project_name}] {pattern_occurrences} occurrences for {pattern_name}')
    writer.writerow([project_name, project_hash, pattern_name, pattern_occurrences])


def process_file(filename: os.path, pattern_name: str) -> Tuple[int, List]:
    return ast_cpp_antlr.main(None, filename, pattern_name)


def start_searching(title_graph: str, search_type: str, pattern_name: str) -> None:
    """
    Start the search with received pattern.

    Args:
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
        pattern_name: Name of the pattern
    """
    for project_name in dt.dict_repo_list.projects.keys():
        process_project(project_name, pattern_name)


def main(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    dt.dict_repo_list.build_repo_dict()
    start_searching(pattern_name, "current", pattern_name)
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
