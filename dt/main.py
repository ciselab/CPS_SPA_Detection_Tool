#!/usr/bin/env python
"""
Starting both search_current.py and search_current_history.py one after another.
"""

from dt import search_current
from dt import search_current_history
from dt import graph_results


def main():
    search_current.main()
    search_current_history.main()
    graph_results.main()


if __name__ == '__main__':
    main()
