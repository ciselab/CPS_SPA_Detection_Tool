#!/usr/bin/env python
"""
Using Antlr4.
"""
import os
from datetime import datetime
from typing import List, Tuple

from antlr4 import FileStream, CommonTokenStream
from antlr4 import ParseTreeWalker

from dt import patterns
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser
from dt.ast_impl.cpp.parsing import DtCppParserListener, TranslationUnit
from dt.patterns import MagicalWaitingNumber
from dt.utils.files import get_file_encoding
from dt.utils.paths import logs_base_path


def parse_ast(tree: CPP14Parser.TranslationUnitContext) -> TranslationUnit:
    """
    Uses Antlr4 and the ParseTreeListener pattern to parse the given tree.

    Args:
        tree: The root node for the AST
    """
    walker = ParseTreeWalker()
    listener = DtCppParserListener()
    walker.walk(listener, tree)
    return listener.get_translation_unit()


def parse_file(abs_path, encoding, pattern_name, skip_failed_encoding: int = 0) -> Tuple[int, List]:
    """
    Parses a CPP file using Antlr4 with the given encoding and antipattern name.

    :param abs_path: An absolute path to the file to parse
    :param encoding: The file encoding
    :param pattern_name: The pattern we wish to gather data for
    :param skip_failed_encoding: Only used when get_file_encoding returns an encoding,
        but Antlr4's FileStream cannot use it.
    :return: a Tuple containing the number of results and a List of those results
    """
    count_results: int = 0
    parse_results: List = []

    try:
        source = FileStream(abs_path, encoding=encoding)
        lexer = CPP14Lexer(source)
        stream = CommonTokenStream(lexer)
        parser = CPP14Parser(stream)
        tree = parser.translationUnit()

        translation_unit = parse_ast(tree)
        if pattern_name == patterns.MAGICAL_WAITING_NUMBER:
            for term in MagicalWaitingNumber.terms_of_interest():
                result_interest, number_results = translation_unit.find_identifier(term)
                if result_interest:
                    parse_results.extend(result_interest)
                count_results = count_results + number_results
        elif pattern_name == patterns.HARDCODED_FINE_TUNING:
            result_interest, number_results = translation_unit.get_identifiers_with_numeric_values()
            if result_interest:
                parse_results.extend(result_interest)
            count_results = count_results + number_results
        else:
            print(f"{pattern_name=} NOT IMPLEMENTED")
    except UnicodeDecodeError:
        print(f"[ERROR] UnicodeDecodeError: {abs_path} encoding={encoding}")
        encoding = get_file_encoding(abs_path, skip_failed_encoding)
        skip_failed_encoding = skip_failed_encoding + 1
        return parse_file(abs_path, encoding, pattern_name, skip_failed_encoding)
    except FileNotFoundError as e:
        error_fnf = os.path.join(logs_base_path(), "antlr_error_file_not_found.log")
        with open(error_fnf, 'a') as ef_file:
            now = datetime.now()
            current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            ef_file.write(f"[{current_date_time}] {e}\n")

    return count_results, parse_results
