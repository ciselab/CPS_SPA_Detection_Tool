#!/usr/bin/env python
from typing import Optional, Dict


class TranslationUnit:
    __slots__ = 'functions'

    def __init__(self):
        self.functions: Dict[str, "FunctionDefinition"] = {}

    def add_function(self, func_name: str, func_def: "FunctionDefinition"):
        self.functions[func_name] = func_def

    def find_identifier(self, id_name: str):
        results = []
        for func_name, func_def in self.functions.items():
            func_body = func_def.func_body
            for identifier in func_body.find_identifier(id_name):
                line, val_name, val = identifier.get_value()
                results.append((val_name, str(val), str(line), func_name))
        return results, len(results)

    # here

    def get_identifiers_with_numeric_values(self):
        # print("HERE")
        results = []
        for current_func_name, current_func_def in self.functions.items():
            current_func_body = current_func_def.func_body
            for identifier in current_func_body.get_identifiers_with_numeric_values():
                # print(f"{identifier=}")
                line, val_name, val = identifier.get_value()
                results.append((val_name, str(val), str(line), current_func_name))
        return results, len(results)

    def get_function_body_for_name(self, func_name) -> Optional["FunctionBody"]:
        func_def = self.functions.get(func_name, None)
        if func_def is not None:
            return func_def.func_body
        else:
            return None


class BlockDeclaration:
    __slots__ = ('line', 'value_name', 'value')

    def __init__(self):
        self.line = ''
        self.value_name = ''
        self.value = 0

    def set_value(self, line, val_name, val):
        self.line = line
        self.value_name = val_name
        self.value = val

    def get_value(self):
        return self.line, self.value_name, self.value

    def __repr__(self):
        return f'block_declaration({self.line}, {self.value_name}, {self.value})'

    def contains_identifier(self, id_name):
        return self.value_name == id_name

    def has_numeric_value(self):
        v_type = type(self.value)
        return v_type == int or v_type == float


class FunctionDefinition:
    __slots__ = ('name', 'args', 'start_line', 'func_body')

    def __init__(self):
        self.name: str = ''
        self.args: list[str] = []
        self.start_line: int = -1
        self.func_body: Optional[FunctionBody] = None

    def add_arg(self, arg_name):
        self.args.append(arg_name)

    def __repr__(self):
        return f'function_definition({self.name}, args:{self.args})'


class FunctionBody:
    __slots__ = 'statements'

    def __init__(self):
        self.statements = []

    def add_statement(self, stmt):
        self.statements.append(stmt)

    def find_identifier(self, id_name):
        results = [stmt for stmt in self.statements if stmt.contains_identifier(id_name)]
        return results

    def get_identifiers_with_numeric_values(self):
        results = [stmt for stmt in self.statements if stmt.has_numeric_value()]
        return results

    def __repr__(self):
        return f'function_body({len(self.statements)} stmt(s))'
