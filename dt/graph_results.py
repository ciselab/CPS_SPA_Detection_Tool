#!/usr/bin/env python
"""
Create a graph of the results.
"""

import os
import glob
from functools import partial
from dt import graph_creation, patterns


def raw_line_count(filename: str) -> int:
    """
    Count lines in a file.

    Args:
        filename: Filepath to check the amount of lines.
    Returns:
         Sum of all the lines in the file.
    """
    with open(filename, 'rb', buffering=0) as f:
        buf_gen = iter(partial(f.read, 1024 * 1024), b'')
        return sum(buf.count(b'\n') for buf in buf_gen)


def find_files_to_graph(hc_logs_path_part: str) -> dict:
    """
    From location with all the log files, will start the line counting function.
    The resulting number is used to generate a graph.

    Args:
        hc_logs_path_part: Path to where all the log files are located, including the same part of file name.
    Returns:
        Dictionary of the file with the number of lines counted.
    """
    data_results_sleeps = {}
    all_logs = hc_logs_path_part + "*"
    found_sleeps_results_files = glob.glob(all_logs)
    for file in found_sleeps_results_files:
        len_file = raw_line_count(file)
        if not len_file == 0:
            file_name = os.path.basename(file)
            data_results_sleeps[file_name] = len_file
            print(f"[{file_name}] {len_file}")
    return data_results_sleeps


def main(pattern_name: str = patterns.MAGICAL_WAITING_NUMBER) -> None:
    print("---START CREATING GRAPHS---")
    print("First round of results")
    graph_creation.create_graph(find_files_to_graph(os.path.join("..", "results", f"{pattern_name}_")),
                                pattern_name, pattern_name)
    print("Final results")
    graph_creation.create_graph(find_files_to_graph(os.path.join("..", "results", f"*{pattern_name}_final_")),
                                f"{pattern_name}_final", f"{pattern_name}_final")
    print("---DONE---")


if __name__ == '__main__':
    main()
