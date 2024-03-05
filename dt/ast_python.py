#!/usr/bin/env python
"""
Using python's build-in AST parser.
"""
import os
import ast
from typing import List, Tuple
from dt.ast_impl.python.parsing import PatternVisitor, MagicalWaitingNumber, HardCodedFineTuning
from dt.patterns import MAGICAL_WAITING_NUMBER, HARDCODED_FINE_TUNING


def parse_file(abs_path: os.path, encoding: str, pattern_name: str, skip_failed_encoding: int = 0) -> Tuple[int, List]:
    """
    Parses a CPP file using Antlr4 with the given encoding and antipattern name.

    :param abs_path: An absolute path to the file to parse
    :param encoding: The file encoding
    :param pattern_name: The pattern we wish to gather data for
    :param skip_failed_encoding: [ONLY USED WITH ANTLR4'S IMPLEMENTATION] Only used when get_file_encoding returns an encoding,
        but Antlr4's FileStream cannot use it. [UNUSED HERE]
    :return: a Tuple containing the number of results and a List of those results
    """
    count_results: int = 0
    parse_results: List = []

    try:
        r = open(abs_path, 'r', encoding=encoding)
        tree = ast.parse(r.read())
    except SyntaxError as e:
        return count_results, parse_results
    except FileNotFoundError as fn:
        return count_results, parse_results

    pv = PatternVisitor()

    if pattern_name == MAGICAL_WAITING_NUMBER:
        pv.register_pattern(MagicalWaitingNumber)
    elif pattern_name == HARDCODED_FINE_TUNING:
        pv.register_pattern(HardCodedFineTuning)

    pv.visit(tree)
    for match in pv.matches:
        parse_results.append((match[4], match[5], match[1], match[6]))

    r.close()

    count_results = len(pv.matches)

    return count_results, parse_results


def main():
    """
    This function is only used to check out how this AST parser works.
    """
    abs_path = "../tests/files/python_ast_test_file.py"
    number, res = parse_file(abs_path, "utf-8", "mwn")
    print(f"{number=}, {res=}")


if __name__ == '__main__':
    main()
