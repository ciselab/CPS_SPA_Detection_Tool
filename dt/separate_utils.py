#!/usr/bin/env python
"""
Utils that can be used separately.
"""
import os
from pathlib import Path
from dt import dict_repo_list


def print_dirs() -> None:
    """
    Resulting template:
        "AirSim": [
            Path_Entry("AirLib", False), Path_Entry(join("AirLib", "include"), False), Path_Entry("Unreal", True)
        ],
    """
    # noinspection SpellCheckingInspection
    red_list = [".git", ".github", "azure", "docker", "docs", "doc", "gradle", "tests", "test", "examples", "example",
                "templates", "template", "test_data", "integrationtest", "integrationtests", "web", "launch"]
    dict_repo_list.build_repo_dict()
    repo_dictionary = dict_repo_list.projects
    dir_set = set()
    for key_repo_name in repo_dictionary.keys():
        start_input = repo_dictionary[key_repo_name]["local"]
        for root, f_dir, file in os.walk(start_input):
            root_project = root.replace(start_input, "")
            if root_project:
                dir_set.add(Path(root_project).parts[1])
        print(f'"{key_repo_name}": [')
        print(f"\t", end="")
        last_set = len(dir_set) - 1
        for number, entry in enumerate(dir_set):
            if entry.lower() not in red_list:
                print(f'Path_Entry("{entry}", True)', end="")
                if number != last_set:
                    print(f', ', end="")
        print("\n],")
        dir_set.clear()


def main() -> None:
    print("Starting...")
    print_dirs()
    print("Finished")


if __name__ == "__main__":
    main()
