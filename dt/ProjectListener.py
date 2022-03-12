#!/usr/bin/env python
import re
from dt.antlr.CPP14ParserListener import CPP14ParserListener
from dt.antlr.CPP14Parser import CPP14Parser
from typing import Optional

delim_stand = u"\u25A0"


class TranslationUnit:
    __slots__ = 'functions'

    def __init__(self):
        self.functions = {}

    def add_function(self, func_name, func_def):
        self.functions[func_name] = func_def

    def find_identifier(self, id_name):
        results = []
        for func_name, func_def in self.functions.items():
            func_body = func_def.func_body
            for identifier in func_body.find_identifier(id_name):
                # results.append((func_name, identifier))
                # print(f"{identifier=}")
                # line, val_name, val = BlockDeclaration.get_value(identifier)
                line, val_name, val = identifier.get_value()
                results.append((val_name, str(val), str(line), delim_stand, func_name, delim_stand))
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
                results.append((val_name, str(val), str(line), delim_stand, current_func_name, delim_stand))
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


class ProjectParserListener(CPP14ParserListener):
    __slots__ = ('stack_list', 'functions')

    def __init__(self):
        self.stack_list = []
        self.tu = TranslationUnit()

    def get_translation_unit(self) -> TranslationUnit:
        return self.tu

    def __unwind_stack__(self):
        value_list = []
        while self.stack_list:
            value_list.append(self.stack_list.pop())
        return value_list

    def __unwind_stack_until__(self, type_to_find: type):
        value_list = []
        current = None
        while not isinstance(current, type_to_find):
            current = self.stack_list.pop()
            value_list.append(current)
        value_list.pop()  # removes the found type from the list
        return current, value_list

    # Begin
    # def exitTranslationUnit(self, ctx: CPP14Parser.TranslationUnitContext):
    #     values = self.__unwind_stack__()
    #     # print(f'{values=}')
    #     # print(f'{self.tu.functions.keys()=}')

    def enterFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext):
        self.stack_list.append(FunctionBody())

    def exitFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext):
        fb, values = self.__unwind_stack_until__(FunctionBody)
        for val in values:
            if isinstance(val, BlockDeclaration):
                fb.add_statement(val)
        self.stack_list.append(fb)

    # Full Function Definition
    # 1st is return type
    # 2nd the function name etc
    # 3rd is the body
    def enterFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        self.stack_list.append(FunctionDefinition())

    def exitFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        func_def, values = self.__unwind_stack_until__(FunctionDefinition)
        if len(values) > 0:
            func_def.func_body = values[0]
            values = values[1:]
            for num, val in enumerate(values[::-1]):
                if num == 0:
                    line, name = val
                    func_def.name = name
                    func_def.start_line = line
                else:
                    _, arg_name = val
                    func_def.add_arg(arg_name)
            self.tu.add_function(func_def.name, func_def)
            # print(f'{func_def}')

    # Complete block
    def enterBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext):
        self.stack_list.append(BlockDeclaration())

    def exitBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext):
        block, values = self.__unwind_stack_until__(BlockDeclaration)
        if values:
            if len(values) > 1:
                line, value = values[0]
                _, value_name = values[1]
            else:
                # print(f"{values=}")
                line, value_name = values[0]
                value = 'unknown'
            block.set_value(line, value_name, value)
            self.stack_list.append(block)

    # Name of the class
    def exitClassName(self, ctx: CPP14Parser.ClassNameContext):
        nodes = ctx.getTokens(132)
        for node in nodes:
            self.stack_list.append((node.symbol.line, node.getText()))

    def exitUnqualifiedId(self, ctx: CPP14Parser.UnqualifiedIdContext):
        nodes = ctx.getTokens(132)
        for node in nodes:
            self.stack_list.append((node.symbol.line, node.getText()))

    def exitLiteral(self, ctx: CPP14Parser.LiteralContext):
        nodes = ctx.getTokens(1) + ctx.getTokens(3)
        for node in nodes:
            parsed_val = 0
            if node.symbol.type == 1:  # Integer literal
                # parsed_val = int(node.getText())

                # maybe different later?
                txt_node = node.getText()
                print(f"INT:{txt_node}")
                # print(f"before:{txt_node=}")

                txt_node = re.sub("[lLuUzZ]+$", "", txt_node)
                if txt_node.startswith("0x") or txt_node.startswith("0X"):
                    parsed_val = int(txt_node, base=16)
                elif txt_node.startswith("0b"):
                    parsed_val = int(txt_node, base=2)
                elif txt_node.startswith("0") and len(txt_node) > 1:
                    parsed_val = int(txt_node, base=8)
                else:
                    parsed_val = int(txt_node)

                # print(f"{txt_node=}")
                # parsed_val = int(txt_node)

            elif node.symbol.type == 3:  # Float literal
                # parsed_val = float(node.getText())

                # maybe different later?
                txt_node = node.getText()
                print(f"FLOAT: {txt_node}")
                # print(f"before:{txt_node=}")

                txt_node = re.sub("[lLfF]+$", "", txt_node)
                if txt_node.startswith("0x") or txt_node.startswith("0X"):
                    parsed_val = float.fromhex(txt_node)
                else:
                    parsed_val = float(txt_node)

                # print(f"{txt_node=}")

                # parsed_val = float(txt_node)

            self.stack_list.append((node.symbol.line, parsed_val))
