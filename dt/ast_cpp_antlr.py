#!/usr/bin/env python
"""
Using Antlr4.
"""
import os
from datetime import datetime

from antlr4 import FileStream, CommonTokenStream
from antlr4 import ParseTreeWalker

from dt import patterns
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser
from dt.ast_impl.cpp.parsing import DtCppParserListener, TranslationUnit
from dt.patterns import MagicalWaitingNumber
from dt.utils.files import get_file_encoding
from dt.utils.paths import logs_base_path

# location_file_default = "D:\\GitHub\\AirSim\\MavLinkCom\\src\\impl\\MavLinkConnectionImpl.cpp"
location_file_default = os.path.join("..", "tests", "files", "ast_test_file_6.cpp")
# location_file_default = os.path.join("..", "tests", "files", "ast_test_file_3.cpp")
# location_file_default = "C:\\Users\\Imara\\Documents\\GitHub\\AirSim\\GazeboDrone\\src\\main.cpp"


def parse_ast(tree: CPP14Parser.TranslationUnitContext) -> TranslationUnit:
    """
    Option number 4

    Args:
        tree:
    """
    walker = ParseTreeWalker()
    listener = DtCppParserListener()
    walker.walk(listener, tree)
    return listener.get_translation_unit()


# def main(csv_writer=None, location_file: str = location_file_default, search_ap: str = "hcft") -> Optional[int]:
def main(csv_writer=None, location_file: str = location_file_default, search_ap: str = "hcft",
         previous_result: list = [], current_hash: str = "", previous_hash: str = ""):
    # print(f"file name: {location_file}")
    encoding: str = ""
    total_results: int = 0
    parse_results = []

    try:
        encoding = get_file_encoding(location_file)
        source = FileStream(location_file, encoding=encoding)
        lexer = CPP14Lexer(source)
        stream = CommonTokenStream(lexer)
        parser = CPP14Parser(stream)
        tree = parser.translationUnit()

        translation_unit = parse_ast(tree)
        # print(f'{translation_unit.functions=}')
        if search_ap == patterns.MAGICAL_WAITING_NUMBER:
            for term in MagicalWaitingNumber.terms_of_interest():
                result_interest, number_results = translation_unit.find_identifier(term)
                if result_interest:
                    parse_results.extend(result_interest)
                total_results = total_results + number_results
                # print(f'{parse_results=}')
        elif search_ap == patterns.HARDCODED_FINE_TUNING:
            result_interest, number_results = translation_unit.get_identifiers_with_numeric_values()
            if result_interest:
                parse_results.extend(result_interest)
            total_results = total_results + number_results
            # print(f'{parse_results=}')
        else:
            print(f"{search_ap=} NOT IMPLEMENTED")
        # print(f"{total_results=}")

        print(f"{parse_results=} {len(parse_results)=}")
        if csv_writer and len(parse_results) > 0:
            if not (current_hash and previous_hash):
                csv_row = [location_file, encoding, current_hash, str(parse_results),
                           previous_hash, previous_result]
                csv_writer.writerow(csv_row)
    except UnicodeDecodeError:
        print(f"[ERROR] UnicodeDecodeError: {location_file} encoding={encoding}")
    except FileNotFoundError as e:
        error_fnf = os.path.join(logs_base_path(), "antlr_error_file_not_found.log")
        with open(error_fnf, 'a') as ef_file:
            now = datetime.now()
            current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            ef_file.write(f"[{current_date_time} - {current_hash}] {e}\n")

    return total_results, parse_results


if __name__ == "__main__":
    main()
