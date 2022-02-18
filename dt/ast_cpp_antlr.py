import ast

import antlr4
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream
import json
import sys

# import CPP14Lexer, CPP14Parser, ...
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser


def to_dict(root):
    obj = {}
    _fill(obj, root)
    return obj


def _fill(obj, node):

    if isinstance(node, TerminalNodeImpl):
        obj["type"] = node.symbol.type
        obj["name"] = node.getText()
        obj["line"] = node.symbol.line
        return

    class_name = type(node).__name__.replace('Context', '')
    rule_name = '{}{}'.format(class_name[0].lower(), class_name[1:])
    arr = []
    obj[rule_name] = arr

    for child_node in node.children:
        child_obj = {}
        arr.append(child_obj)
        _fill(child_obj, child_node)


if __name__ == '__main__':
    source = FileStream("../tests/files/ast_test_file_2.cpp")
    lexer = CPP14Lexer(source)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationUnit()

    # convert the parse tree to JSON file
    tree_dict = to_dict(tree)
    json_str = json.dumps(tree_dict, indent=1)

    # print the JSON output
    print(json_str)

    # print the parse tree as lisp
    print(Trees.toStringTree(tree, parser.ruleNames, parser))
    print(lexer.ruleNames)