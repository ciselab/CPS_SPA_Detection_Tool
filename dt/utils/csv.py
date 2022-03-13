import csv
import os
from typing import List


class CsvUtil:
    """
    A base class for CSV Utilities that provides some defaults for things like delimiters and newlines.
    """
    LINE_TERMINATOR = '\n'
    DELIMITER_SYMBOL = u"\u25B2"
    FILE_MODE = "r"

    def __init__(self, filename: os.path, encoding: str = "utf-8"):
        self.filename = filename
        self.encoding = encoding


class CsvWriter(CsvUtil):
    """
    A thin wrapper around csv.writer that deals with file handles internally and sets the appropriate options.
    API methods adopted as necessary.
    """
    FILE_MODE = "a"

    def __init__(self, filename: os.path, encoding: str = "utf-8"):
        super().__init__(filename, encoding=encoding)
        self.__file_handle = open(self.filename, self.FILE_MODE, encoding=self.encoding, newline=self.LINE_TERMINATOR)
        self.__csv_writer = csv.writer(self.__file_handle, delimiter=self.DELIMITER_SYMBOL,
                                       quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator=self.LINE_TERMINATOR)

    def writerow(self, csv_row: List):
        self.__csv_writer.writerow(csv_row)


class CsvReader(CsvUtil):
    def __init__(self, filename: os.path, fieldnames: List[str], encoding: str = "utf-8"):
        super().__init__(filename, encoding)
        self.__file_handle = open(self.filename, self.FILE_MODE, encoding=self.encoding, newline=self.LINE_TERMINATOR)
        self.__csv_reader = csv.DictReader(self.__file_handle, fieldnames=fieldnames, delimiter=self.DELIMITER_SYMBOL)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file_handle.close()

    def __iter__(self):
        return self.__csv_reader.__iter__()

    def __next__(self):
        return self.__csv_reader.__next__()


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
