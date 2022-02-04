#!/usr/bin/env python
"""
Searching through the current state of the repository.
"""
import os
import re
import csv
from chardet.universaldetector import UniversalDetector
from datetime import datetime
import dt.dict_repo_list
from dt.graph_creation import create_graph
from dt.utils import get_csv_file, write_row
from dt.search_setup import use_search_pattern
from dt.search_setup import var_name_pattern
from dt.search_setup import var_number_pattern


results_long_list = []
dir_location_report = os.path.join("..", "results")
delim_stand = u"\u25A0"


def no_encoding_found(file: os.path) -> str:
    """
    When the default, Windows-1252 and utf-8 encoding is not correct, chardet is being used.
    This tool tries to detect which encoding is used.

    Args:
        file: Location of the file to find type of encoding used.

    Returns:
        Encoding used in the file, detected by chardet.
    """
    try:
        with open(file, "rb") as rd_file:
            raw_data = rd_file.readlines()
            detector = UniversalDetector()
            for rd_line in raw_data:
                detector.feed(rd_line)
                if detector.done:
                    break
            detector.close()
        if detector.result:
            enc = detector.result["encoding"]
            if enc:
                print(f"encoding: {enc}")
                return enc
            else:
                print("No encoding result.")
        else:
            print("No Result from detector.")
    except UnicodeDecodeError:
        """
        In case chardet is not able to detect which encoding was used.
        """
        print(f"UnicodeDecodeError: {file}")


def read_file_encoding(file: os.path, p, url: str, csv_writer, key_project, name_pattern: str, enc=None) -> int:
    """
    Read a file and apply the correct encoding to read the file. Then finding the matching pattern in each line.

    Args:
        file: Path to the file to be read.
        p: Pre-compiled regex pattern to search for in the file (Regular Expression Objects).
        url: Url to the project
        csv_writer: CSV Writers object
        key_project: project name
        name_pattern: Name of the pattern used.
        enc: If encoding provided, this will be used.

    Returns:
        The amount matching the pattern giving in this file.
    """
    count = 0
    encodings_options = ['Windows-1252', 'utf-8']
    enc_select = None
    remember_prev_line = ""
    var_name_check = (name_pattern == "sleeps_var_name")
    vars_names_list = []

    if isinstance(enc, int):
        if enc >= len(encodings_options):
            """
            Tried encodings still not correct, continue to use chardet.
            """
            enc_select = no_encoding_found(file)
        elif enc < len(encodings_options):
            enc_select = encodings_options[enc]
    try:
        results_long_list.clear()
        with open(file, 'r', encoding=enc_select) as content_file:
            for line_number, line in enumerate(content_file):
                check = list(re.findall(p, line))
                if var_name_check:
                    vars_names = (re.findall(var_name_pattern, line))
                    if vars_names:
                        vars_names_list.append(vars_names)
                if check:
                    for each_check in check:
                        each_check = list(each_check)
                        check_before_found = False
                        if var_name_check:
                            for each in vars_names_list:
                                for e in each:
                                    if re.match(var_number_pattern, e[1]):
                                        if each_check[1] == e[0]:
                                            check_before_found = True
                                            each_check[1] = e[1]
                            # if not check_before_found:
                            #     print(f"[WARNING] Not found with {each_check} in {file}")
                        if not var_name_check or (var_name_check and check_before_found):
                            count += 1
                            line_number_fix = line_number + 1
                            results_long_list.append((each_check[0], each_check[1], line_number_fix,
                                                      delim_stand, remember_prev_line, delim_stand))
                remember_prev_line = line
        if results_long_list:
            write_row(csv_writer, file, str(results_long_list), str(enc_select))
    except UnicodeDecodeError:
        """
        Some files are using an encoding that cannot be immediately read.
        Most of these files, seem to be using Windows-1252 followed by utf-8 encoding.
        To keep the duration of this script as short as possible, this encoding will be tried first.
        """
        if not isinstance(enc, int):
            enc = 0
        elif not enc >= len(encodings_options):
            enc = encodings_options.index(enc_select) + 1
        if not enc >= len(encodings_options):
            result = read_file_encoding(file, p, url, csv_writer, key_project, name_pattern, enc)
            if isinstance(result, int):
                count += result
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    return count


def walk_dirs(key_project: str) -> set:
    """
    Goes through the dirs, noted in dt.dict_repo_list.projects_modules, and returns the files.

    Args:
        key_project: Name (key) of the project.

    Returns:
        Set of the files (full path).
    """
    full_files = set()
    # noinspection SpellCheckingInspection
    search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
                     '.ipp', '.inl', '.txx', '.tpp', '.tpl',
                     '.c++m', '.cppm', '.cxxm', '.kt',
                     '.java', '.go', '.py', '.rb', '.rs',
                     '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']
    start_input = dt.dict_repo_list.projects[key_project]["local"]
    for each_dir, _, _ in os.walk(start_input):
        for number, _ in enumerate(dt.dict_repo_list.projects_modules[key_project]):
            full_path_list = os.path.join(start_input,
                                          dt.dict_repo_list.projects_modules[key_project][number].top_level)
            if each_dir == full_path_list:
                start_full_path = os.path.join(start_input, each_dir)
                for root, dirs, files in os.walk(start_full_path, topdown=True):
                    if not dt.dict_repo_list.projects_modules[key_project][number].recursive:
                        """If not True (True means going recursively through the dirs), 
                        the dirs are cleared so only the current level is checked."""
                        dirs.clear()
                    for name in files:
                        file = os.path.join(root, name)
                        file_name, file_extension = os.path.splitext(file)
                        if file_extension.lower() in search_in_ext:
                            full_files.add(file)
    return full_files


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict, csv_writer, name: str) -> int:
    """
    Starts the mining process on the repository indicated by the given URL
    Through the current state of the repository. Only looking at files with specified extensions.

    Args:
        key_project: Project name from the dictionary.
        search_for_pattern: Pattern to find in the code to occur.
        repo_dictionary: Dictionary of with the project name and local location.
        csv_writer: CSV Writers object
        name: Name of the pattern used.

    Returns:
        count: How often the keyword occurs in the code of specified project.
    """
    url = repo_dictionary[key_project]["local"]
    count = 0
    p = re.compile(search_for_pattern, re.M)
    result_walk = walk_dirs(key_project)

    for file in result_walk:
        result = read_file_encoding(file, p, url, csv_writer, key_project, name)
        if isinstance(result, int):
            count += result
    return count


def start_searching(search_for_pattern: str, title_graph: str, search_type: str, name: str) -> None:
    """
    Start the search with received pattern.

    Args:
        search_for_pattern: Pattern to search with in ths current round.
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
        # csv_writer: CSV Writers object
        name: Name of the pattern
    """
    data_graph = {}
    dt.dict_repo_list.build_repo_dict()
    repo_dictionary = dt.dict_repo_list.projects
    for key_repo_name in repo_dictionary.keys():

        pattern_project_filename = f"{name}_{key_repo_name}"

        file_commits_results = os.path.join(dir_location_report, pattern_project_filename + "_results.csv")
        if os.path.exists(file_commits_results):
            print(f"File {file_commits_results} exists, removing file.")
            os.remove(file_commits_results)

        csv_file = get_csv_file(pattern_project_filename)
        csv_writer = csv.writer(csv_file, delimiter=delim_stand, quotechar='"',
                                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        counted = dig_for_code(key_repo_name, search_for_pattern, repo_dictionary, csv_writer, name)
        print(f"{key_repo_name}: {counted}")
        if counted > 0:
            data_graph[key_repo_name] = counted
    if data_graph:
        create_graph(data_graph, title_graph, search_type)


def main(pattern_name: str = "sleeps") -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    start_searching(use_search_pattern(pattern_name), pattern_name, "current", pattern_name)
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
