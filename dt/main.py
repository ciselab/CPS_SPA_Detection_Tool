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


if __name__ == '__main__':
    main()
