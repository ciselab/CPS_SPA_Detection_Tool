#!/usr/bin/env python
"""
Creates one file of all number of results files.

Each pattern for each project creates an one line file with results.
Due to compatibility of using Docker with a container for each project and pattern.
This script combines all these results into one file.
"""
from os import walk
from dt.utils.files import remove_file_if_exists

results_path = "C:\\Users\\Imara\\Documents\\Server_results"
f = []
state = ""
for (dir_path, dir_names, filenames) in walk(results_path):
    for file in filenames:
        file_full_path = str(dir_path) + "\\" + str(file)
        f.append(file_full_path)

remove_file_if_exists('pattern_data_total.csv')

with open('pattern_data_total.csv', 'w', encoding="utf-8") as outfile:
    for entry in f:
        if "pattern_data" not in entry:
            continue
        if "final" in entry:
            state = "\u25B2final"
        elif "initial" in entry:
            state = "\u25B2initial"
        with open(entry, encoding="utf-8") as infile:
            file_input = infile.read().rstrip("\n") + state
            outfile.write(str(file_input))
        outfile.write("\n")
