#!/usr/bin/env python
"""
Starting the script for the selected AP.
"""

from datetime import datetime
from dt import dict_repo_list, patterns, search
from shutil import copytree
from tempfile import TemporaryDirectory
import os
import sys


def main(project_name, pattern_name, current_base_hash, sel_modules: bool = True, history_project: bool = True) -> None:
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    print("---STARTING---")

    if not project_name:
        project_name = sys.argv[1]
    if not pattern_name:
        pattern_name = sys.argv[2]
    if not current_base_hash:
        tmp_current_base_hash = "_"
    else:
        tmp_current_base_hash = f"_{current_base_hash}"

    pattern_cls = patterns.pattern_lookup.get(pattern_name, None)
    if pattern_cls is None:
        print("Error: Pattern is non-existing.")
        return

    tmp_dir = f"{project_name}_{pattern_name}{tmp_current_base_hash}"
    print(f"Creating tmp dir: {tmp_dir}")
    print(f"Project path: {os.path.join(dict_repo_list.location_github, project_name)}")

    with TemporaryDirectory(prefix=tmp_dir) as td:
        print("Start creating tmp dir.")
        new_project_name = f"{project_name}{tmp_current_base_hash}"
        project_path = os.path.join(dict_repo_list.location_github, new_project_name)
        if not os.path.exists(project_path):
            print(f"Error: Path does not exist: {project_path}")
            return
        print(f"Copying {project_path} to {td}")
        copytree(project_path, td, dirs_exist_ok=True)  # src, dest
        if sel_modules:
            dict_repo_list.projects[project_name]["local"] = td
            dict_repo_list.build_repo_dict_sha()

        print(f"[{pattern_cls.header_name()}] START")
        search.main(project_name, pattern_cls.name(), sel_modules, current_base_hash, history_project)
        print(f"[{pattern_cls.header_name()}] DONE")

    print("---FINISHED---")
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == '__main__':
    main(False, False, False, False)
