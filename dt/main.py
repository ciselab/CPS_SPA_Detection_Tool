#!/usr/bin/env python
"""
Starting the script for the selected AP.
"""

import os
import sys
from datetime import datetime
from dt import search, patterns
from dt.utils import files, paths


def main() -> None:
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    print("---STARTING---")

    for project_name in sys.argv[1:]:
        result_path = paths.project_results_path(project_name)
        files.remove_file_if_exists(os.path.join(result_path, "pattern_data.csv"))
        files.remove_file_if_exists(os.path.join(result_path, "pattern_data_final.csv"))

    print("[MAGICAL WAITING NUMBER] START")
    search.main(patterns.MAGICAL_WAITING_NUMBER, projects=sys.argv[1:])
    print("[MAGICAL WAITING NUMBER] DONE")

    print("[HARD CODED FINE TUNING] START")
    search.main(patterns.HARDCODED_FINE_TUNING, projects=sys.argv[1:])
    print("[HARD CODED FINE TUNING] DONE")

    print("---FINISHED---")
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == '__main__':
    main()
