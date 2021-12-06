#!/usr/bin/env python
"""
Searching through the diffs of each commit
"""
import os
import re
import csv
from chardet.universaldetector import UniversalDetector
from datetime import datetime
import dt.dict_repo_list
from graph_creation import create_graph
from utils import get_csv_file, write_row


results_long_list = []
save_results_at = "results_git_blame_4.txt"
dir_location_report = os.path.join("..", "results")


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


def read_file_encoding(file: os.path, p, url: str, csv_writer, enc=None) -> int:
    """
    Read a file and apply the correct encoding to read the file. Then finding the

    Args:
        file: Path to the file to be read.
        p: Pre-compiled regex pattern to search for in the file (Regular Expression Objects).
        url: Url to the project
        csv_writer: CSV Writers object
        enc: If encoding provided, this will be used.

    Returns:
        The amount matching the pattern giving in this file.
    """
    count = 0
    encodings_options = ['Windows-1252', 'utf-8']
    enc_select = None
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
                check = re.findall(p, line)
                if check:
                    for each_find in check:
                        results_long_list.append((each_find, line_number))
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
            result = read_file_encoding(file, p, url, csv_writer, enc)
            if isinstance(result, int):
                count += result
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    else:
        return count


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict, csv_writer) -> int:
    """
    Starts the mining process on the repository indicated by the given URL
    Through the current state of the repository. Only looking at files with specified extensions.

    Args:
        key_project: Project name from the dictionary.
        search_for_pattern: Pattern to find in the code to occur.
        repo_dictionary: Dictionary of with the project name and local location.
        csv_writer: CSV Writers object

    Returns:
        count: How often the keyword occurs in the code of specified project.
    """
    url = repo_dictionary[key_project]["local"]
    count = 0

    p = re.compile(search_for_pattern, re.M)
    for root, directories, files in os.walk(url):
        for name in files:
            file = os.path.join(root, name)

            file_name, file_extension = os.path.splitext(file)
            # noinspection SpellCheckingInspection
            search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
                             '.ipp', '.inl', '.txx', '.tpp', '.tpl',
                             '.c++m', '.cppm', '.cxxm', '.kt',
                             '.java', '.go', '.py', '.rb', '.rs',
                             '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']

            if file_extension.lower() in search_in_ext:
                result = read_file_encoding(file, p, url, csv_writer)
                if isinstance(result, int):
                    count += result
    return count


def start_searching(search_for_pattern: str, title_graph: str, search_type: str, csv_writer):
    """
    Start the search with received pattern.

    Args:
        search_for_pattern: Pattern to search with in ths current round.
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
        csv_writer: CSV Writers object
    """
    data_graph = {}
    dt.dict_repo_list.build_repo_dict()
    repo_dictionary = dt.dict_repo_list.projects
    for key_repo_name in repo_dictionary.keys():
        counted = dig_for_code(key_repo_name, search_for_pattern, repo_dictionary, csv_writer)
        print(f"{key_repo_name}: {counted}")
        if counted > 0:
            data_graph[key_repo_name] = counted
    if data_graph:
        create_graph(data_graph, title_graph, search_type)


def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    if os.path.exists(save_results_at):
        print("File exists, removing file.")
        os.remove(save_results_at)

    """ Pattern name needs to be without spaces """
    dict_search_patterns = {
        # "sleep function": r'^(.*)(sleep\()',
        # "Sleep function": r'^(.*)(Sleep\()',
        # "sleep_for": r'^(.*)(sleep_for)',
        # "setTimeout": r'^(.*)(setTimeout)',
        # "sleep space": r'^(.*)(sleep" ")',
        "var_with_number": r'([a-z_A-Z][a-z_0-9A-Z.]*)\s*=\s*([0-9]+)',
    }
    for name in dict_search_patterns:
        file_commits_results = os.path.join(dir_location_report, name+"_results.csv")
        if os.path.exists(file_commits_results):
            print(f"File {file_commits_results} exists, removing file.")
            os.remove(file_commits_results)
        print(f"Searching: {name}\n")
        csv_file = get_csv_file(name)
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        start_searching(dict_search_patterns[name], name, "current", csv_writer)

    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
