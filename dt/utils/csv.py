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
