#!/usr/bin/env python
"""
Starting the script for the selected AP.
"""

import sys
from datetime import datetime
from dt import search, patterns


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
