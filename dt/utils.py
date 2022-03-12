#!/usr/bin/env python
"""
Common for utils.
"""
import os
import pathlib
from typing import Optional
from typing import TextIO
from chardet.universaldetector import UniversalDetector

location = os.path.join(pathlib.Path.home(), "CPS_SPA_Detection_Tool", "results", "repo")
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
    hash_file_location = os.path.join(location, project_name)
    if os.path.exists(hash_file_location):
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


def get_csv_file(addition_name: str) -> TextIO:
    """
    The final name of the file that is being returned opened is as follows {addition_name}_results.csv.
    Checks if a results directory is available, otherwise will create one.
    The file will be created at the results location with the name as previously described.

    Args:
        addition_name: Name for which the results file should be opened.
    Returns:
         Opened file.
    """
    results_file_name = addition_name + "_results.csv"
    if not os.path.exists(os.path.abspath(dir_location_report)):
        os.makedirs(dir_location_report)
    full_path_results_file = os.path.join(dir_location_report, results_file_name)
    return open(full_path_results_file, "a", encoding='utf-8', newline='\n')


def write_row(csv_writer, file: str, results: str, encoding: str) -> None:
    """
    Write a row in the .csv file.
    Args:
        csv_writer: csv.writer object, specifies .csv file.
        file: Full path file name.
        results: Results found.
        encoding:  Encoding used to read this file.
    """
    csv_line = [file, results, encoding]
    csv_writer.writerow(csv_line)


def write_row_final(csv_writer, file, results, encoding, previous_result, current_hash, previous_hash, caller='current'):
    if caller == 'current':
        csv_line = [file, results, encoding]
    else:
        csv_line = [file, current_hash, results, previous_hash, previous_result, encoding]
    csv_writer.writerow(csv_line)


def write_row_results_more(csv_writer_commits,
                           project_name: str, file_name_full_path: str, comparative_hash: str,
                           commit_hash: str, search_var_name: str, var_value: str, var_value_found: str) -> None:
    """
    Writes row in the .csv file with results found while going through the history of the file.
    Args:
        csv_writer_commits: csv.writer object, specifies .csv file.
        project_name: Name of the project for which these are the results.
        file_name_full_path: Full path file name.
        comparative_hash: Results were compared to the file from this commit (hash).
        commit_hash: Hash commit where the change was found.
        search_var_name: Name of which the variable was connected, such as "sleep" or "sleep_for".
        var_value: Value compared to, connected to comparative_hash.
        var_value_found:  Value found, which is different then the var_value.
    """
    csv_line_commits = [project_name, file_name_full_path, comparative_hash, commit_hash,
                        search_var_name, var_value, var_value_found]
    csv_writer_commits.writerow(csv_line_commits)


def file_encoding(file: os.path, enc_select: str = 'utf-8', enc=None) -> str:
    """
    Read a file and apply the correct encoding to read the file.

    Args:
        file: Path to the file to be read.
        enc_select: current encoding.
        enc: encoding in list location.

    Returns:
        enc: Returns the file's encoding.
    """
    encodings_options = ['Windows-1252', 'ascii']

    if isinstance(enc, int):
        if enc >= len(encodings_options):
            """
            Tried encodings still not correct, continue to use chardet.
            """
            det_enc = no_encoding_found(file)
            if det_enc:
                enc_select = det_enc
        elif enc < len(encodings_options):
            enc_select = encodings_options[enc]
    try:
        with open(file, 'r', encoding=enc_select):
            print(f"encoding: {enc_select}")
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
            file_encoding(file, enc_select, enc)
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    return enc_select


def no_encoding_found(file: os.path) -> Optional[str]:
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
                print(f"[ENCODING]: {enc}")
                return enc
            else:
                print("[ENCODING]: No encoding result.")
        else:
            print("[ENCODING]:No Result from detector.")
    except UnicodeDecodeError:
        """
        In case chardet is not able to detect which encoding was used.
        """
        print(f"UnicodeDecodeError: {file}")
