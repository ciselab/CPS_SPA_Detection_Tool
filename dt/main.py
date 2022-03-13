#!/usr/bin/env python
"""
Starting both search_current.py and search_current_history.py one after another.
"""

from datetime import datetime
from dt import search_current, patterns
from dt import search_current_history
# from dt import graph_results


def main() -> None:
    print("---CURRENT TIME---")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")
    print("---STARTING---")

    print("[SLEEPS] START")
    search_current.main(patterns.MAGICAL_WAITING_NUMBER)
    search_current_history.main(patterns.MAGICAL_WAITING_NUMBER)
    # graph_results.main("sleeps")
    print("[SLEEPS] DONE")
    #
    # print("[HARD CODED FINE TUNING] START")
    # search_current.main("hcft")
    # search_current_history.main("hcft")
    # # graph_results.main("hcft")
    # print("[HARD CODED FINE TUNING] DONE")
    #
    # print("[SLEEPS VAR NAME] START")
    # search_current.main("sleeps_var_name")
    # search_current_history.main("sleeps_var_name")
    # graph_results.main("sleeps_var_name")
    # print("[SLEEPS VAR NAME] DONE")
    #
    # print("[VAR NUMBER] START")
    # search_current.main("var_with_number")
    # search_current_history.main("var_with_number")
    # graph_results.main("var_with_number")
    # print("[VAR NUMBER] DONE")

    print("---FINISHED---")
    print(f"Started at: {current_time}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == '__main__':
    main()
