#!/usr/bin/env python
"""
Using Antlr4.
"""
from antlr4.tree.Tree import TerminalNodeImpl
# from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream
# import json
import os

# import CPP14Lexer, CPP14Parser, ...
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser

list_interest = ["usleep", "sleep", "MSleep", "sleep_for", "qualifiedId"]


def to_dict(root) -> dict:
    obj = {}
    _fill(obj, root)
    return obj


def _fill(obj: dict, node):
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


def traverse(nodes: dict):
    """
    Traversing through the nodes in search for any type that matches the list_interest.

    Args:
        nodes: Containing the (next) branch to search through.
    """
    for i in nodes.keys():
        for j in nodes[i]:
            if "type" in j:
                for each_sleep in list_interest:
                    if each_sleep in j["name"]:
                        print(f"FOUND: {j}")
                        break
            else:
                traverse(j)


if __name__ == '__main__':
    location_file = os.path.join("..", "tests", "files", "ast_test_file_2.cpp")
    source = FileStream(location_file)
    lexer = CPP14Lexer(source)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationUnit()

    # convert the parse tree to JSON file
    tree_dict = to_dict(tree)
    traverse(tree_dict)
    # json_str = json.dumps(tree_dict, indent=1)

    # print the JSON output
    # print(json_str)
    # with open('json_data.json', 'w') as outfile:
    #     outfile.write(json_str)

    # print the parse tree as lisp
    # print(Trees.toStringTree(tree, parser.ruleNames, parser))
