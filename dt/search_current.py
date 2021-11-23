#!/usr/bin/env python
"""
Searching through the diffs of each commit
"""
import os
import re
from chardet.universaldetector import UniversalDetector
import dt.dict_repo_list
from datetime import datetime
from graph_creation import create_graph


def no_encoding_found(file: os.path) -> str:
    """
    When the default, Windows-1252 and utf-8 encoding is not correct, chardet is being used.
    This tool tries to detect which encoding is used.
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


def read_file_encoding(file: os.path, p, enc=None) -> int:
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
        with open(file, 'r', encoding=enc_select) as content_file:
            for line in content_file:
                check = re.findall(p, line)
                count += len(check)
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
            result = read_file_encoding(file, p, enc)
            if isinstance(result, int):
                count += result
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    else:
        return count


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict) -> int:
    """
    Starts the mining process on the repository indicated by the given URL
    Through the current state of the repository. Only looking at files with specified extensions.

    Args:
        key_project: Project name from the dictionary.
        search_for_pattern: Pattern to find in the code to occur.
        repo_dictionary: Dictionary of with the project name and local location.

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
                result = read_file_encoding(file, p)
                if isinstance(result, int):
                    count += result
    return count


def start_searching(search_for_pattern: str, title_graph: str, search_type: str):
    """
    Start the search with received pattern.

    Args:
        search_for_pattern: Pattern to search with in this current round.
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
    """
    data_graph = {}
    dt.dict_repo_list.build_repo_dict()
    repo_dictionary = dt.dict_repo_list.projects
    for key_repo_name in repo_dictionary.keys():
        counted = dig_for_code(key_repo_name, search_for_pattern, repo_dictionary)
        print(f"{key_repo_name}: {counted}")
        if counted > 0:
            data_graph[key_repo_name] = counted
    if data_graph:
        create_graph(data_graph, title_graph, search_type)


def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    dict_search_patterns = {
        "sleep function": r'^(.*)(sleep\()',
        "Sleep function": r'^(.*)(Sleep\()',
        "sleep_for": r'^(.*)(sleep_for)',
        "setTimeout": r'^(.*)(setTimeout)',
        "sleep space": r'^(.*)(sleep" ")',
        "var with number": r'(?=_[a-z_0-9]|[a-z])[a-z_0-9]+(?=\s*=\s*[0-9])',
    }
    for name in dict_search_patterns:
        print(f"Searching: {name}")
        start_searching(dict_search_patterns[name], name, "current")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
