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

function_calls = []             # List of AST node objects that are function calls
function_declarations = []      # List of AST node objects that are function declarations

list_interest = ["usleep", "sleep"]
dict_sleep = {}         # line number: usleep

""" CHANGE THESE """
# Tell clang.cindex where libclang.dylib is
clang.cindex.Config.set_library_path("C:\\Program Files\\LLVM\\bin")
file_name = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "CPS_SPA_Detection_Tool", "tests", "files",
                         "ast_test_file_3.cpp")


# Traverse the AST tree
def traverse(node, list_sleep_dur):
    for child in node.get_children():
        if child.kind == clang.cindex.CursorKind.OVERLOADED_DECL_REF:
            print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
            print(f"\tchild {child.displayname} location line: {child.location.line}")
            if child.displayname in list_interest:
                dict_sleep[child.location.line] = child.displayname
        elif ((child.kind == clang.cindex.CursorKind.INTEGER_LITERAL) or (child.kind == clang.cindex.CursorKind.FLOATING_LITERAL)):
            print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
            print(f"\tchild {child.displayname} location line: {child.location.line}")

            """ Get sleep duration """
            token = next(child.get_tokens())
            print(f"\tdur: {token.spelling}")

            if child.location.line in dict_sleep.keys():
                list_sleep_dur.append((dict_sleep[child.location.line], token.spelling))
        traverse(child, list_sleep_dur)


def main():
    index = clang.cindex.Index.create()

    # Generate AST from filepath passed in the command line
    if not os.path.exists(file_name):
        print(f"[ERROR] File {file_name} does not exist.")
    else:
        tu = index.parse(file_name)
        root = tu.cursor        # Get the root of the AST

        list_sleep_dur = []
        traverse(root, list_sleep_dur)

        print("\n### Found matching results ###")
        [print(fun, ':', value) for fun, value in list_sleep_dur]


if __name__ == "__main__":
    main()
