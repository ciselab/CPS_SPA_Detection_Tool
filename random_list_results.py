#!/usr/bin/env python
"""
Used for selecting files for manual verification randomly.
"""
import random
from os.path import join
from dt.utils.paths import results_base_path

random_lists = join(results_base_path(), "random_project_files.csv")

# Number of file for analysis, which differ from the amount of results in each file.
# noinspection SpellCheckingInspection
# dict_projects_result_files = {
#     "number_hcft_Arduino_IRremote_final": 92,
#     "number_hcft_ardumower_final": 97,
#     "number_hcft_Arduino_final": 340,
# }
dict_projects_result_files = {
    "Arduino-IRremote": 24,
    "Arduino": 92,
    "ardupilot": 499,
}
# list_projects_number = [number_hcft_Arduino_IRremote_final, number_hcft_ardumower_final, number_hcft_Arduino_final]


# Starts standard at 2, as an Excel sheet is used to write notes. The first row is used for the column names.
def get_nums(end: int, start: int = 2, interval: int = 1):
    return list(range(start, end, interval))


def main() -> None:
    print(random_lists)
    print(f"Creates file: {random_lists}")
    with open(random_lists, 'a', encoding="utf-8") as outfile:
        for project in dict_projects_result_files.keys():
            list_numbers = get_nums(dict_projects_result_files[project])
            randomized_list = random.sample(list_numbers, len(list_numbers))
            # outfile.write(random.shuffle(list_numbers))  # can be used as well, but directly, doesn't return anything
            outfile.write(f"[{project}] {str(randomized_list)}\n")


if __name__ == '__main__':
    main()
