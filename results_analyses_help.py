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


# HISTORY PROCESSING
def analysing(file: str, file_name: str) -> None:
    dict_previous_file_names = {}
    compare_results = []
    set_filenames = set()
    name = f"collected_{file_name}"
    path_file = os.path.join(pathlib.Path.home(), "Documents", "Server_results", name)
    remove_file_if_exists(path_file)
    writer = CsvWriter(path_file)
    fieldnames = ['filename_1', 'encoding_1', 'hash_1', 'results_1', 'filename_2', 'hash_2', 'results_2']
    with CsvReader(file, fieldnames=fieldnames) as reader:
        for row in reader:
            # print(f"{set_filenames=}\n{row['filename_1']=}\n{row['filename_2']=}")
            # print(f"{len(set_filenames)=}")
            if (row['filename_1'] not in set_filenames) \
                    and (row['filename_2'] not in set_filenames) \
                    and len(set_filenames) > 0:
                csv_row = [set_filenames, compare_results, dict_previous_file_names]
                if csv_row and (len(compare_results) > 0):
                    # print(f"{csv_row=}")
                    # print(f"{len(compare_results)=}")
                    writer.writerow(csv_row)
                dict_previous_file_names.clear()
                set_filenames.clear()
                # compare_results.clear()
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
        # print("TO LAST")
        # print(f"{set_filenames=}")
        if len(set_filenames) > 0:
            # print("LAST ONE")
            csv_row = [set_filenames, compare_results,dict_previous_file_names]
            if csv_row and (len(compare_results) > 0):
                # print(f"{csv_row=}")
                # print(f"{len(compare_results)=}")
                writer.writerow(csv_row)


def main():
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    print("START")
    list_analyse_files = [
        "hcft_Arduino-IRremote_final.csv",
        "hcft_Arduino_final.csv",
        "hcft_ardumower_final.csv",
        "hcft_ardupilot_final.csv"]
    for file in list_analyse_files:
        file_path = os.path.join(pathlib.Path.home(), "Documents", "Server_results", "tool", file)
        analysing(file_path, file)
    print("END")

    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
