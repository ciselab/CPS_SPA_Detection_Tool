#!/usr/bin/env python
""" Usage: call with <filename>
"""

# import sys
import os
import pathlib
import clang.cindex

function_calls = []             # List of AST node objects that are function calls
function_declarations = []      # List of AST node objects that are fucntion declarations


# Traverse the AST tree
def traverse(node):

    # Recurse for children of this node
    for child in node.get_children():
        traverse(child)

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
# file_name = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "PX4-Autopilot", "src", "modules", "ekf2", "EKF2.cpp")
file_name = os.path.join(pathlib.Path.home(), "Documents", "COSMOS", "test_files", "test_file.cpp")
tu = index.parse(file_name)

root = tu.cursor        # Get the root of the AST
traverse(root)

print(f"try out: {clang.cindex.CursorKind.DECL_STMT}")

# Print the contents of function_calls and function_declarations
print(f"function calls: {function_calls}")
print(function_declarations)
