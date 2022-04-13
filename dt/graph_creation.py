#!/usr/bin/env python
"""
Creating a graph from results
"""
import re
import time
import pathlib
import os
import matplotlib.pyplot as plt


def create_graph(data: dict, data_title: str, sub_dir: str) -> None:
    """
    Create a bar graph with the input received.

    Args:
        data: Data to create the graph with in {key(each bar): value}.
        data_title: Title for the graph.
        sub_dir: Subdirectory to store the graph in.
    """
    plt.cla()
    plt.title(data_title)
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()), rotation=90)

    current = str(time.time())
    pattern = r"[0-9]+"
    result_current = re.match(pattern, current)
    format_current = result_current[0]

    location = os.path.join(pathlib.Path.home(), "CPS_SPA_Detection_Tool", "results", sub_dir)
    if not os.path.exists(os.path.abspath(location)):
        os.makedirs(location)

    new_title = data_title.replace(" ", "_")
    file_name = str(format_current + "_" + new_title)

    """Adjustments"""
    plt.tight_layout()

    """ Save plot """
    save_location = os.path.join(location, file_name)
    plt.savefig(save_location)
