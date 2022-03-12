#!/usr/bin/env python
"""
Searching through the current state of the repository.
"""
import os
from datetime import datetime

import dt.ast_cpp_antlr as ast_cpp_antlr
import dt.dict_repo_list
from dt.graph_creation import create_graph
from dt.utils.csv import CsvWriter
from dt.utils.files import get_project_files, remove_file_if_exists

results_long_list = []
dir_location_report = os.path.join("..", "results")


def count_pattern_occurrences(project_name: str, csv_writer, name: str) -> int:
    """
    Starts the mining process on the repository indicated by the given project name.
    Through the current state of the repository. Only looking at files with specified extensions.

    Args:
        project_name: Project name from the dictionary.
        csv_writer: CSV Writers object
        name: Name of the pattern used.

    Returns:
        count: How often the pattern occurs in the code of specified project.
    """
    count: int = 0
    project_files: set = get_project_files(project_name)

    for file in project_files:
        number_results: int
        number_results, _ = ast_cpp_antlr.main(csv_writer, file, name)
        if isinstance(number_results, int):
            count += number_results
    return count


def start_searching(title_graph: str, search_type: str, pattern_name: str) -> None:
    """
    Start the search with received pattern.

    Args:
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
        pattern_name: Name of the pattern
    """
    data_graph = {}
    dt.dict_repo_list.build_repo_dict()
    repo_dictionary = dt.dict_repo_list.projects
    for project_name in repo_dictionary.keys():

        results_filename = os.path.join(dir_location_report, f"{pattern_name}_{project_name}_results.csv")
        remove_file_if_exists(results_filename)
        csv_writer = CsvWriter(results_filename)

        counted = count_pattern_occurrences(project_name, csv_writer, pattern_name)
        print(f"{project_name}: {counted}")
        if counted > 0:
            data_graph[project_name] = counted
    if data_graph:
        create_graph(data_graph, title_graph, search_type)


def main(pattern_name: str = "sleeps") -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    start_searching(pattern_name, "current", pattern_name)
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
