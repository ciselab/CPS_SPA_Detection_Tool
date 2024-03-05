#!/usr/bin/env python
import ast
from typing import NamedTuple

current_function_def = []


class PatternMatch(NamedTuple):
    tag: str
    line_number: int
    end_line_number: int
    offset: int
    msg: str
    val: str
    name_function_def: str


class HardCodedFineTuning:
    TAG = "HCFT"

    @classmethod
    def check(cls, node):
        global current_function_def

        if isinstance(node, ast.Assign):
            for arg_node in node.targets:
                if not isinstance(arg_node, ast.Name):
                    continue
                if not isinstance(node.value, ast.Constant):
                    continue

                name_func_def = ""
                if current_function_def:
                    if current_function_def[1] < node.lineno <= current_function_def[2]:
                        name_func_def = current_function_def[0]

                return PatternMatch(tag=cls.TAG, line_number=node.lineno, end_line_number=node.end_lineno,
                                    offset=node.col_offset, msg=f"{arg_node.id}", val=f"{node.value.value}",
                                    name_function_def=name_func_def)
        if isinstance(node, ast.FunctionDef):
            current_function_def = [node.name, node.lineno, node.end_lineno]


class MagicalWaitingNumber:
    TAG = "MWN"
    NAME_PATTERNS = ["sleep", "delay"]

    @classmethod
    def check(cls, node):
        global current_function_def

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                name = node.func.attr
            elif isinstance(node.func, ast.Subscript):
                return
            else:
                try:
                    name = node.func.id
                except AttributeError:
                    return
            if name not in cls.NAME_PATTERNS:
                return

            for arg_node in node.args:

                if not isinstance(arg_node, ast.Constant):
                    continue
                name_func_def = ""
                if current_function_def:
                    if current_function_def[1] < node.lineno <= current_function_def[2]:
                        name_func_def = current_function_def[0]
                return PatternMatch(tag=cls.TAG, line_number=node.lineno, end_line_number=node.end_lineno,
                                    offset=node.col_offset, msg=f"{name}", val=f"{arg_node.value}",
                                    name_function_def=name_func_def)

        if isinstance(node, ast.FunctionDef):
            current_function_def = [node.name, node.lineno, node.end_lineno]


class PatternVisitor(ast.NodeVisitor):
    def __init__(self):
        self.__patterns = []
        self.matches = []

    def register_pattern(self, pattern_cls):
        self.__patterns.append(pattern_cls)

    def visit_Call(self, node: ast.Call):
        for pattern in self.__patterns:
            possible_match = pattern.check(node)
            if possible_match is not None:
                self.matches.append(possible_match)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        for pattern in self.__patterns:
            possible_match = pattern.check(node)
            if possible_match is not None:
                self.matches.append(possible_match)
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        for pattern in self.__patterns:
            possible_match = pattern.check(node)
            if possible_match is not None:
                self.matches.append(possible_match)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        for pattern in self.__patterns:
            possible_match = pattern.check(node)
            if possible_match is not None:
                self.matches.append(possible_match)
        self.generic_visit(node)


def main():
    """
    This function is only used to check out how this AST parser works.
    """
    file_location = "../../../tests/files/python_ast_test_file.py"

    r = open(file_location, 'r')
    tree = ast.parse(r.read())

    pv = PatternVisitor()
    pv.register_pattern(MagicalWaitingNumber)
    pv.register_pattern(HardCodedFineTuning)

    pv.visit(tree)
    for match in pv.matches:
        print(f"{match}")

    r.close()


if __name__ == '__main__':
    main()
