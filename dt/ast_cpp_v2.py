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

file_name = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "CPS_SPA_Detection_Tool", "tests", "ast_test_file.cpp")


def new_traverse(node):
    for child in node.get_children():
        if child.location.line == 18:   # Currently hard-coded to check this line only.
            print(f'FOUND {child.displayname} [line={child.location.line}, col={child.location.column}] type: {child.kind}')
            if child.kind == clang.cindex.CursorKind.DECL_REF_EXPR:
                print(f"\tchild {child.displayname} location line: {child.location.line}")
                if child.referenced:
                    print(f"\treferenced? {child.referenced.displayname} location line: {child.referenced.location.line}")
            elif child.kind == clang.cindex.CursorKind.OVERLOADED_DECL_REF:
                print(f"\tchild {child.displayname} location line: {child.location.line}")
                if child.referenced:
                    print(f"\treferenced? {child.referenced.displayname} location line: {child.referenced.location.line}")
            elif child.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
                print(f"\tchild {child.displayname} location line: {child.location.line}")
                if child.referenced:
                    print(f"\treferenced? {child.referenced.displayname}; location line: {child.referenced.location.line}")

                """ Get sleep duration """
                # method 1
                # for i in child.get_tokens():
                #     print(f"\tdur: {i.spelling}")

                # method 2
                # gen = child.get_tokens()
                # token = next(gen)
                # print(f"\tdur: {token.spelling}")

                # method 3
                token_2 = next(child.get_tokens())
                print(f"\tdur: {token_2.spelling}")

            elif child.kind == clang.cindex.CursorKind.UNEXPOSED_EXPR:
                print(f"\tchild {child.displayname} location line: {child.location.line}")
                if child.referenced:
                    print(f"\treferenced? {child.referenced.displayname}; location line: {child.referenced.location.line}")

        new_traverse(child)


# Traverse the AST tree
def traverse(node):

    # Recurse for children of this node
    for child in node.get_children():
        traverse(child)
        # print(child.kind)
        # for s_child in child.get_children():
        #     print(f"-->{s_child.kind}")

    # Add the node to function_calls
    if node.type.kind == clang.cindex.CursorKind.CALL_EXPR:
        function_calls.append(node)
    #
    # # Add the node to function_declarations
    if node.type.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        function_declarations.append(node)

    # if node.type.kind == clang.cindex.CursorKind.INVALID:
    #     print(f"found invalids: {node.displayname}")

    # if node.type.kind == clang.cindex.CursorKind.DECL_STMT:
    #     print(f'Found {node.displayname} [line={node.location.line}, col={node.location.column}]')

    # Print out information about the node
    print(f'Found {node.displayname} [line={node.location.line}, col={node.location.column}] type: {node.kind}')


# Tell clang.cindex where libclang.dylib is
clang.cindex.Config.set_library_path("C:\\Program Files\\LLVM\\bin")
index = clang.cindex.Index.create()

# Generate AST from filepath passed in the command line
if not os.path.exists(file_name):
    print(f"[ERROR] File {file_name} does not exist.")
else:
    tu = index.parse(file_name)

    root = tu.cursor        # Get the root of the AST
    # traverse(root)
    new_traverse(root)

    # Print the contents of function_calls and function_declarations
    # print(f"function calls: {function_calls}")
    # print(function_declarations)
