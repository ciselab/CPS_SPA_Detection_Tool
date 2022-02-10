#!/usr/bin/env python
import pytest
import os
import pathlib
import clang.cindex

from dt.ast_cpp_v2 import traverse

# Tell clang.cindex where libclang.dylib is
clang.cindex.Config.set_library_path("C:\\Program Files\\LLVM\\bin")


def setup_clang(file_name):
    index = clang.cindex.Index.create()
    tu = index.parse(file_name)
    root = tu.cursor  # Get the root of the AST
    return root


@pytest.mark.parametrize("file_name, result", [
    pytest.param("ast_test_file.cpp", [("usleep", "4200")],
                 id="usleep(4200)"),
    pytest.param("ast_test_file_2.cpp", [('usleep', '50000'), ("usleep", "3")],
                 id="usleep 50000 and 3"),
    pytest.param("ast_test_file_3.cpp", [('usleep', '50000'), ("usleep", "4.2"), ("usleep", "0.3"), ("usleep", "3")],
                 id="usleep float"),
    # pytest.param("ast_test_file_4.cpp", [('usleep', '4.2'), ("usleep", "-0.3")],
    #              id="usleep float"),
])
def test_string_results_to_list(file_name: str, result: dict):
    file_name_path = os.path.join(pathlib.Path.home(),
                                  "Documents", "GitHub", "CPS_SPA_Detection_Tool", "tests", file_name)
    list_sleep_dur = []
    root = setup_clang(file_name_path)
    traverse(root, list_sleep_dur)
    assert list_sleep_dur == result
