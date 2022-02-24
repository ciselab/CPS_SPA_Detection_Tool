#!/usr/bin/env python
"""
Using Antlr4.
"""
# import json
import os
import pathlib
from antlr4.tree.Tree import TerminalNodeImpl
# from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser
from dt.utils import write_row
from dt.utils import file_encoding

list_interest = ["usleep", "sleep", "MSleep", "sleep_for", "qualifiedId"]
dict_sleep = {}
location_file_default = os.path.join("..", "tests", "files", "ast_test_file_3.cpp")
current_statement = {}
current_number = {}
sleep_found = ""


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

    if node.children:
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
    global current_statement
    global current_number
    global sleep_found

    for i in nodes.keys():
        for j in nodes[i]:
            if "statement" in j:
                sleep_found = ""
            if "literal" in j:
                if sleep_found:
                    if j['literal'][0]['type'] == 1 or j['literal'][0]['type'] == 3:
                        # print(f"number! {j['literal'][0]}")
                        dict_sleep[j['literal'][0]["line"]] = (sleep_found, j['literal'][0]["name"])
            if "type" in j:
                for each_sleep in list_interest:
                    if each_sleep in j["name"]:
                        # print(f"FOUND: {j}")
                        sleep_found = j["name"]
                        dict_sleep[j["line"]] = j["name"]
                        break
            else:
                traverse(j)


def print_json_to_file(json_str: str) -> None:
    """
    Print JSON to file.
    Args:
        json_str: JSON structure in string form.
    """
    if os.path.exists("json_data.json"):
        print(f"File json_data.json exists, removing file.")
        os.remove("json_data.json")
    with open('json_data.json', 'w') as outfile:
        print(f"Creating new json_data.json.")
        outfile.write(json_str)


def main(csv_writer=None, location_file: str = location_file_default) -> int:
    if pathlib.Path(location_file).suffix == '.cpp':
        print(f"file name: {location_file}")
        current_statement.clear()
        current_number.clear()
        dict_sleep.clear()
        enc = ""

        try:
            enc = file_encoding(location_file)
            source = FileStream(location_file, encoding=enc)
            lexer = CPP14Lexer(source)
            stream = CommonTokenStream(lexer)
            parser = CPP14Parser(stream)
            tree = parser.translationUnit()

            # convert the parse tree to JSON file
            tree_dict = to_dict(tree)
            traverse(tree_dict)

            """ Temporarily until #5 has been implemented. """
            for each in dict_sleep:
                if type(dict_sleep[each]) != tuple:
                    dict_sleep[each] = (dict_sleep[each], "UNKOWN")
            """ End temp. """

            # print results
            # print(dict_sleep)

            if csv_writer:
                write_row(csv_writer, location_file, str(dict_sleep), "None")
        except UnicodeDecodeError:
            print(f"[ERROR] UnicodeDecodeError: {location_file} encoding={enc}")
            pass

        # print the JSON output
        # json_str = json.dumps(tree_dict, indent=1)
        # print(json_str)
        # print the JSON output to file
        # print_json_to_file(json_str)

        # print the parse tree as lisp
        # print(Trees.toStringTree(tree, parser.ruleNames, parser))
        return len(dict_sleep)
    else:
        return 0


if __name__ == "__main__":
    main()
