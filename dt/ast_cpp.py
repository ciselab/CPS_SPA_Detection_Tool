#!/usr/bin/env python
"""
AST for C++ (and C)
"""
import os
# import sys
import pathlib
# from clang import cindex
import clang.cindex as cl
cl.Config.set_library_file("C:\\Program Files\\LLVM\\bin\\libclang.dll")


def find_typerefs(node, typename):
    """ Find all references to the type named 'typename'
    """
    if node.kind.is_reference():
        try:
            ref_node = cl.Cursor(node)
            if ref_node.spelling == typename:
                print(f'Found {typename} [line={node.location.line}, col={node.location.column}]')
        except Exception as e:
            print(f"type {type(node)}")
            print(f"over here: {e}")
            pass
    # Recurse for children of this node
    for c in node.get_children():
        try:
            find_typerefs(c, typename)
        except Exception as e:
            print(f"something: {e}")
            pass


index = cl.Index.create()
# tu = index.parse(sys.argv[1])
file_name = os.path.join(pathlib.Path.home(), "Documents", "GitHub", "PX4-Autopilot", "src", "modules", "ekf2", "EKF2.cpp")
print(f"filename: {file_name}")
tu = index.parse(file_name)
print(f"parsing = {tu}")
print(f'Translation unit: {tu.spelling}')
type_input = "int"
# find_typerefs(tu.cursor, sys.argv[2])
find_typerefs(tu.cursor, type_input)
