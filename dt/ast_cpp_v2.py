#!/usr/bin/env python
"""
AST for C++ (and C) [DRAFT]

Usage:
- Tell clang.cindex where libclang.dylib is.
- Change file_name to location test file.
- Then run the script.
"""

import os
import pathlib
import clang.cindex
from dt.utils import write_row

list_interest = ["usleep", "sleep", "MSleep", "sleep_for"]
# note: MSleep is used in AirSim in gazebo::common::Time::MSleep
dict_sleep = {}         # line number: usleep
dict_una_op = {}        # line number: column
count = 0

""" CHANGE THESE """
# Tell clang.cindex where libclang.dylib is
clang.cindex.Config.set_library_path("C:\\Program Files\\LLVM\\bin")
# file_name_default = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "CPS_SPA_Detection_Tool", "tests", "files",
#                          "ast_test_file_4.cpp")
file_name_default = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "AirSim", "GazeboDrone", "src", "main.cpp")


# Traverse the AST tree
def traverse(node, list_sleep_dur):
    # global count
    # print(count)
    # count = count+1
    for child in node.get_children():
        if (child.location.file is not None) and (str(child.location.file) == file_name_default):
            # print(f"file: {child.location.file} VS {file_name_default}")
            # if str(child.location.file) == file_name_default:
            print(f"file: {child.location.file} and {file_name_default}")
            print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
            if child.kind == clang.cindex.CursorKind.UNARY_OPERATOR:
                dict_una_op[child.location.line] = child.location.column
            elif child.kind == clang.cindex.CursorKind.OVERLOADED_DECL_REF:
                # print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
                # print(f"\tchild {child.displayname} location line: {child.location.line}")
                # if child.displayname in list_interest:
                #     dict_sleep[child.location.line] = child.displayname
                if any(element in child.displayname for element in list_interest):
                    dict_sleep[child.location.line] = child.displayname
            elif ((child.kind == clang.cindex.CursorKind.INTEGER_LITERAL)
                  or (child.kind == clang.cindex.CursorKind.FLOATING_LITERAL)):
                # print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
                # print(f"\tchild {child.displayname} location line: {child.location.line}")

                """ Get sleep duration """
                token = next(child.get_tokens())
                duration = token.spelling

                """ If there is a UNARY_OPERATOR before add - sign (+ sign not supported) """
                if child.location.line in dict_una_op.keys():
                    column = child.location.column
                    if dict_una_op[child.location.line] == column-1:
                        duration = "-" + duration

                if child.location.line in dict_sleep.keys():
                    list_sleep_dur.append((dict_sleep[child.location.line], duration))
            try:
                traverse(child, list_sleep_dur)
            except StopIteration:
                # print("ERROR: StopIteration")
                pass    # No other siblings


def main(csv_writer=None, file_name: str = file_name_default) -> int:
    dict_sleep.clear()
    dict_una_op.clear()
    print(f"file name: {file_name}")

    # temporarily: making sure only cpp files in projects are analysed by clang
    if pathlib.Path(file_name).suffix == '.cpp':
        index = clang.cindex.Index.create()

        # Generate AST from filepath passed in the command line
        if not os.path.exists(file_name):
            print(f"[ERROR] File {file_name} does not exist.")
        else:
            tu = index.parse(str(file_name), options=1, args=['-x', 'c++'])
            root = tu.cursor        # Get the root of the AST

            list_sleep_dur = []
            traverse(root, list_sleep_dur)

            if list_sleep_dur:
                print(f"\n### Found matching results [{file_name}] ###")
                [print(fun, ':', value) for fun, value in list_sleep_dur]
            # write_row(csv_writer, file_name, str(list_sleep_dur), "None")
            return len(list_sleep_dur)


if __name__ == "__main__":
    main()
