#!/usr/bin/env python
"""
Starting both search_current.py and search_current_history.py one after another.
"""

from dt import search_current
from dt import search_current_history
from dt import graph_results


def main() -> None:
    print("[SLEEPS] START")
    search_current.main("sleeps")
    search_current_history.main("sleeps")
    graph_results.main("sleeps")
    print("[SLEEPS] DONE")

    print("[SLEEPS VAR NAME] START")
    search_current.main("sleeps_var_name")
    search_current_history.main("sleeps_var_name")
    graph_results.main("sleeps_var_name")
    print("[SLEEPS VAR NAME] DONE")

    print("[VAR NUMBER] START")
    search_current.main("var_with_number")
    search_current_history.main("var_with_number")
    graph_results.main("var_with_number")
    print("[VAR NUMBER] DONE")


if __name__ == '__main__':
    main()
