import os
import csv
from typing import TextIO

from dt.utils import dir_location_report

DELIMITER_SYMBOL = u"\u25B2"


class CsvWriter:
    def __init__(self, filename: str):
        self.filename = filename


class CsvReader:
    pass


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


def write_row(csv_writer, file, results, encoding, previous_result, current_hash, previous_hash, caller='current'):
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