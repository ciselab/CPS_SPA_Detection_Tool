#!/usr/bin/env python
"""
Analyse files and merge results for each file.
Removes results where only new variables were introduced.
"""
import ast
import os
import pathlib
import re
from datetime import datetime
from deepdiff import DeepDiff
from dt.utils.csv import CsvReader, CsvWriter
from dt.utils.files import remove_file_if_exists
from dt.dict_repo_list import projects


link_project = ""
counter = int
counter_warnings_in_file = int
total_warnings = int


def start_write_md_file(file_name: str, project_name: str) -> None:
    remove_file_if_exists(file_name)
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(f"# {project_name}\n\n")


def continue_write_md_file(file_name: str, set_filenames, compare_results, dict_previous_file_names) -> None:
    global total_warnings
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(f"## Result number #{counter}\n\n")
        print(f'{counter=}')
        file.write(f"### File name(s)\n")
        for file_name_in_set in set_filenames:
            file.write(f"{file_name_in_set}\n")
        file.write("\n")
        file.write(f"### Compare results\n")
        for each_result_entry in compare_results:
            file.write(f"{each_result_entry}\n")
        file.write("\n")
        file.write(f"### Number of warnings:\n")
        file.write(f"{counter_warnings_in_file}\n\n")
        print(f"{counter_warnings_in_file=}")
        total_warnings = total_warnings + counter_warnings_in_file


# HISTORY PROCESSING
def analysing(file: str, file_name: str, project_name: str) -> None:
    global counter
    dict_previous_file_names = {}
    compare_results = []
    set_filenames = set()
    list_results = []
    global counter_warnings_in_file
    counter_warnings_in_file = 1
    name = f"collected_{file_name}"
    #path_file = os.path.join(pathlib.Path.home(), "Documents", "Server_results", name)
    path_file = os.path.join(pathlib.Path.home(), "GitHub", "CPS_SPA_Detection_Tool", "results", name)
    remove_file_if_exists(path_file)
    writer = CsvWriter(path_file)

    #path_file_md = os.path.join(pathlib.Path.home(), "Documents", "Server_results", project_name + ".md")
    path_file_md = os.path.join(pathlib.Path.home(), "GitHub", "CPS_SPA_Detection_Tool", "results", project_name + ".md")
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
                counter_warnings_in_file = 1
                dict_previous_file_names.clear()
                set_filenames.clear()
                compare_results = []
            else:
                counter_warnings_in_file = counter_warnings_in_file+1
            set_filenames.add(row['filename_1'])
            set_filenames.add(row['filename_2'])
            dict_previous_file_names[row['hash_1']] = row['filename_1']
            dict_previous_file_names[row['hash_2']] = row['filename_2']

            a = list(ast.literal_eval(row['results_1']))
            b = list(ast.literal_eval(row['results_2']))
            comp = DeepDiff(a, b, ignore_order=True)

            if comp:
                link_1 = f"{link_project}/blob/{row['hash_1']}/{row['filename_1']}"
                link_2 = f"{link_project}/blob/{row['hash_2']}/{row['filename_2']}"
                if 'values_changed' in comp:
                    type_result = 'values_changed'
                    for each in comp[type_result]:
                        list_results_new = comp[type_result][each]['new_value']
                        list_results_old = comp[type_result][each]['old_value']
                        number = re.findall("[0-9]+", each)
                        if len(number) == 2:
                            if not number[1] == '2':
                                list_results_changed = a[int(number[0])]
                                print_results_as = f"\n####Values changed\nNEW:{list_results_new}" \
                                                   f"\nOLD:{list_results_old}\nCHANGED:{list_results_changed}" \
                                                   f"\nVersion 1(new): {link_2}\nVersion 2(old): {link_1}"
                        else:
                            list_results_changed = a[int(number[0])]
                            print_results_as = f"\n####Values changed\nNEW:{list_results_new}" \
                                               f"\nOLD:{list_results_old}\nCHANGED:{list_results_changed}" \
                                               f"\nVersion 1(new): {link_2}\nVersion 2(old): {link_1}"
                if 'iterable_item_added' in comp:
                    type_result = 'iterable_item_added'
                    for each in comp[type_result]:
                        list_results.append(comp[type_result][each])
                    print_results_as = f"\n####Values added\nValues: {list_results}\nNot available in: {link_1}\nAdded in: {link_2}"
                if 'iterable_item_removed' in comp:
                    type_result = 'iterable_item_removed'
                    for each in comp[type_result]:
                        list_results.append(comp[type_result][each])
                    print_results_as = f"\n####Values removed\nValues: {list_results}\nAvailable in: {link_1}\nRemoved in: {link_2}"
                print_results_as = f"{print_results_as}\n####True or False Positive:\n[todo]\n####Note:\n[todo]"

                if print_results_as:
                    compare_results.append(print_results_as)
                    list_results.clear()
        # TO LAST
        if len(set_filenames) > 0:
            # LAST ONE
            csv_row = [set_filenames, compare_results, dict_previous_file_names]
            if csv_row and (len(compare_results) > 0):
                writer.writerow(csv_row)
                counter = counter + 1
                continue_write_md_file(path_file_md, set_filenames, compare_results, dict_previous_file_names)


def main() -> None:
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("START")
    global link_project
    global counter
    global total_warnings
    list_analyse_files = [
        ("hcft_Arduino-IRremote_final.csv", "Arduino-IRremote"),
        # ("hcft_Arduino_final.csv", "Arduino"),
        # ("hcft_ardumower_final.csv", "ardumower"),
        # ("hcft_ardupilot_final.csv", "ardupilot")
    ]
    for file in list_analyse_files:
        counter = 0
        total_warnings = 0
        project_name = file[1]
        link_project = projects[project_name]["remote"]
        #file_path = os.path.join(pathlib.Path.home(), "Documents", "Server_results", "tool", file[0])
        file_path = os.path.join(pathlib.Path.home(), "GitHub", "CPS_SPA_Detection_Tool", "results", "tool", file[0])
        analysing(file_path, file[0], project_name)
    print("END")

    print(f"Total amount of warnings: {total_warnings}")

    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
