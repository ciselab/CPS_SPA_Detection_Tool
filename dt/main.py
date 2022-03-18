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


def main() -> None:
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    print("---STARTING---")

    project_name = sys.argv[1]
    pattern_name = sys.argv[2]

    pattern_cls = patterns.pattern_lookup.get(pattern_name, None)
    if pattern_cls is None:
        return

    with TemporaryDirectory(prefix=f"{project_name}_{pattern_name}_") as td:
        project_path = os.path.join(dict_repo_list.location_github, project_name)
        if not os.path.exists(project_path):
            return
        print(f"Copying {project_path} to {td}")
        copytree(project_path, td, dirs_exist_ok=True)  # src, dest
        dict_repo_list.projects[project_name]["local"] = td
        dict_repo_list.build_repo_dict_sha()

        print(f"[{pattern_cls.header_name()}] START")
        search.main(project_name, pattern_cls.name())
        print(f"[{pattern_cls.header_name()}] DONE")

    print("---FINISHED---")
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == '__main__':
    main()
