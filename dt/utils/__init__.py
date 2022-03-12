#!/usr/bin/env python
"""
Common for utils.
"""
import os
import pathlib

location = os.path.join(pathlib.Path.home(), "CPS_SPA_Detection_Tool", "results", "repo")
dir_location_report = os.path.join("..", "results")


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
