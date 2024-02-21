#!/usr/bin/env python
from os.path import dirname, realpath, join


def get_results_file_path():
    file_results = "results.csv"
    dir_current = dirname(realpath(__file__))
    filename = join(dir_current, file_results)
    return filename


def main():
    print("Analysis Results python file.")
    get_results_file_path()


if __name__ == "__main__":
    main()
