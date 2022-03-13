#!/usr/bin/env python
import re

from antlr4.tree.Tree import TerminalNodeImpl

from dt.antlr.CPP14ParserListener import CPP14ParserListener
from dt.antlr.CPP14Parser import *
from dt.ast_impl.cpp.types import *
from typing import Union, List, Tuple, Any


class DtCppParserListener(CPP14ParserListener):
    __slots__ = ('stack_list', 'functions')

    def __init__(self):
        self.stack_list = []
        self.tu = TranslationUnit()

    def get_translation_unit(self) -> TranslationUnit:
        return self.tu

    def __unwind_stack__(self) -> List[Any]:
        """
        A helper function to unwind the stack.
        :return: a list of all the remaining values on stack
        """
        value_list = []
        while self.stack_list:
            value_list.append(self.stack_list.pop())
        return value_list

    def __unwind_stack_until__(self, type_to_find: type) -> Tuple[type, List[Any]]:
        """
        A helper function to unwind the stack until a value of the type `type_to_find` is found.
        :param type_to_find: the marker type that was previously pushed onto the stack.
        :return: a tuple of the found type as well as all the other values on stack possibly related to it.
        """
        value_list = []
        current = None
        while not isinstance(current, type_to_find):
            current = self.stack_list.pop()
            value_list.append(current)
        value_list.pop()  # removes the found type from the list
        return current, value_list

    def exitTranslationUnit(self, ctx: CPP14Parser.TranslationUnitContext):
        values = self.__unwind_stack__()

    def enterFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext) -> None:
        """
        Once we enter a FunctionBodyContext, we push data onto the stack that we can identify and come back to.
        :param ctx: The ParseTree node that we're visiting.
        :return: None
        """
        self.stack_list.append(FunctionBody())

    def exitFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext) -> None:
        """
        Once we exit a FunctionBodyContext,
        we unwind the stack until we find the matching marker and assemble the data.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        func_body: FunctionBody
        func_body, values = self.__unwind_stack_until__(FunctionBody)
        for value in values:
            if isinstance(value, BlockDeclaration):
                func_body.add_statement(value)
        self.stack_list.append(func_body)

    def enterFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext) -> None:
        """
        Once we enter a FunctionDefinitionContext, we push data onto the stack that we can identify and come back to.
        :param ctx: The ParseTree node that we're visiting.
        :return: None
        """
        self.stack_list.append(FunctionDefinition())

    def exitFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext) -> None:
        """
        Once we exit a FunctionDefinitionContext,
        we unwind the stack until we find the matching marker and assemble the data.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        func_def: FunctionDefinition
        func_def, values = self.__unwind_stack_until__(FunctionDefinition)
        if len(values) > 0:
            func_def.func_body = values[0]
            values = values[1:]
            for num, value in enumerate(values[::-1]):
                if num == 0:
                    line, name = value
                    func_def.name = name
                    func_def.start_line = line
                else:
                    _, arg_name = value
                    func_def.add_arg(arg_name)
            self.tu.add_function(func_def.name, func_def)

    def enterBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext) -> None:
        """
        Once we enter a BlockDeclarationContext, we push data onto the stack that we can identify and come back to.
        :param ctx: The ParseTree node that we're visiting.
        :return: None
        """
        self.stack_list.append(BlockDeclaration())

    def exitBlockDeclaration(self, ctx: CPP14Parser.BlockDeclarationContext) -> None:
        """
        Once we exit a BlockDeclarationContext,
        we unwind the stack until we find the matching marker and assemble the data.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        block: BlockDeclaration
        block, values = self.__unwind_stack_until__(BlockDeclaration)
        if len(values) == 0:
            return
        elif len(values) > 1:
            line, value = values[0]
            _, value_name = values[1]
        else:
            line, value_name = values[0]
            value = 'unknown'
        block.set_value(line, value_name, value)
        self.stack_list.append(block)

    def exitClassName(self, ctx: CPP14Parser.ClassNameContext) -> None:
        """
        Once we've found and are about to leave an ClassNameContext,
        make sure to extract the necessary information and push it onto our local stack.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        nodes = ctx.getTokens(CPP14Parser.Identifier)
        for node in nodes:
            self.stack_list.append((node.symbol.line, node.getText()))

    def exitUnqualifiedId(self, ctx: CPP14Parser.UnqualifiedIdContext) -> None:
        """
        Once we've found and are about to leave an UnqualifiedIdContext,
        make sure to extract the necessary information and push it onto our local stack.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        token_nodes = ctx.getTokens(CPP14Parser.Identifier)
        for node in token_nodes:
            self.stack_list.append((node.symbol.line, node.getText()))

    def exitLiteral(self, ctx: CPP14Parser.LiteralContext) -> None:
        """
        Once we've found and are about to leave a LiteralContext,
        make sure to extract the necessary information and push it onto our local stack.
        :param ctx: The ParseTree node that we've just visited.
        :return: None
        """
        token_nodes: List[TerminalNodeImpl] = ctx.getTokens(CPP14Parser.IntegerLiteral)
        token_nodes.extend(ctx.getTokens(CPP14Parser.FloatingLiteral))

        for node in token_nodes:
            parsed_value: Union[int, float] = 0
            node_value: str = node.getText()
            node_value = node_value.replace("\'", "")  # remove quote digit separator
            if node.symbol.type == CPP14Parser.IntegerLiteral:
                # Remove type specifier suffixes, see:
                # https://en.cppreference.com/w/cpp/language/integer_literal
                node_value = re.sub("[lLuUzZ]+$", "", node_value)
                number_base = 10
                if node_value.startswith("0x") or node_value.startswith("0X"):
                    number_base = 16
                elif node_value.startswith("0b"):
                    number_base = 2
                elif node_value.startswith("0") and len(node_value) > 1:
                    number_base = 8

                parsed_value = int(node_value, base=number_base)
            elif node.symbol.type == CPP14Parser.FloatingLiteral:
                # Remove type specifier suffixes, see:
                # https://en.cppreference.com/w/cpp/language/floating_literal
                node_value = re.sub("[lLfF]+$", "", node_value)
                if node_value.startswith("0x") or node_value.startswith("0X"):
                    parsed_value = float.fromhex(node_value)
                else:
                    parsed_value = float(node_value)

            self.stack_list.append((node.symbol.line, parsed_value))
