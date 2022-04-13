#!/usr/bin/env python
"""
Analyse files and merge results for each file.
Removes results where only new variables were introduced.
"""
import ast
import os
import pathlib
from datetime import datetime
from deepdiff import DeepDiff
from dt.utils.csv import CsvReader, CsvWriter
from dt.utils.files import remove_file_if_exists
from dt.dict_repo_list import projects


link_project = ""
counter = int


def start_write_md_file(file_name: str, project_name: str):
    remove_file_if_exists(file_name)
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(f"# {project_name}\n\n")


def continue_write_md_file(file_name: str, set_filenames, compare_results, dict_previous_file_names):
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(f"## Result number #{counter}\n\n")
        file.write(f"### File name(s)\n")
        for file_name_in_set in set_filenames:
            file.write(f"{file_name_in_set}\n")
        file.write("\n")
        # file.write(f"{set_filenames}\n\n")
        file.write(f"### Compare results\n")
        for each_result_entry in compare_results:
            file.write(f"{each_result_entry}\n")
        file.write("\n")
        file.write(f"### Files\n")
        for each_hash in dict_previous_file_names:
            file_name = dict_previous_file_names[each_hash]
            link_file = f"{link_project}/blob/{each_hash}/{file_name}"
            file.write(f"[{each_hash} : {dict_previous_file_names[each_hash]}]{{{link_file}}}\n")
        file.write(f"\n")
        file.write(f"### True or False Positive\n[todo]\n\n")
        file.write(f"### Note\n[todo]\n\n\n")


# HISTORY PROCESSING
def analysing(file: str, file_name: str, project_name: str) -> None:
    global counter
    dict_previous_file_names = {}
    compare_results = []
    set_filenames = set()
    name = f"collected_{file_name}"
    path_file = os.path.join(pathlib.Path.home(), "Documents", "Server_results", name)
    remove_file_if_exists(path_file)
    writer = CsvWriter(path_file)

    path_file_md = os.path.join(pathlib.Path.home(), "Documents", "Server_results", project_name + ".md")
    start_write_md_file(path_file_md, project_name)

    fieldnames = ['filename_1', 'encoding_1', 'hash_1', 'results_1', 'filename_2', 'hash_2', 'results_2']
    with CsvReader(file, fieldnames=fieldnames) as reader:
        for row in reader:
            """ Checking for different file """
            if (row['filename_1'] not in set_filenames) \
                    and (row['filename_2'] not in set_filenames):
                csv_row = [set_filenames, compare_results, dict_previous_file_names]
                if csv_row and (len(compare_results) > 0):
                    writer.writerow(csv_row)
                    counter = counter + 1
                    continue_write_md_file(path_file_md, set_filenames, compare_results, dict_previous_file_names)
                dict_previous_file_names.clear()
                set_filenames.clear()
                compare_results = []
            set_filenames.add(row['filename_1'])
            set_filenames.add(row['filename_2'])
            dict_previous_file_names[row['hash_1']] = row['filename_1']
            dict_previous_file_names[row['hash_2']] = row['filename_2']

            comp = DeepDiff(row['results_1'], row['results_2'], ignore_order=True)
            if comp:
                if 'values_changed' in comp:
                    type_result = 'values_changed'
                if 'iterable_item_added' in comp:
                    type_result = 'iterable_item_added'
                if 'iterable_item_removed' in comp:
                    type_result = 'iterable_item_removed'
                list_results = ast.literal_eval(comp[type_result]['root']['new_value'])
                if list_results:
                    compare_results.append(list_results)
        # TO LAST
        if len(set_filenames) > 0:
            # LAST ONE
            csv_row = [set_filenames, compare_results, dict_previous_file_names]
            if csv_row and (len(compare_results) > 0):
                writer.writerow(csv_row)
                counter = counter + 1
                continue_write_md_file(path_file_md, set_filenames, compare_results, dict_previous_file_names)


def main():
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("START")
    global link_project
    global counter
    list_analyse_files = [
        ("hcft_Arduino-IRremote_final.csv", "Arduino-IRremote"),
        ("hcft_Arduino_final.csv", "Arduino"),
        ("hcft_ardumower_final.csv", "ardumower"),
        ("hcft_ardupilot_final.csv", "ardupilot")]
    for file in list_analyse_files:
        counter = 0
        project_name = file[1]
        link_project = projects[project_name]["remote"]
        file_path = os.path.join(pathlib.Path.home(), "Documents", "Server_results", "tool", file[0])
        analysing(file_path, file[0], project_name)
    print("END")

    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
