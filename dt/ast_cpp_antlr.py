#!/usr/bin/env python
"""
Using Antlr4.
"""
import json
import os
import pathlib
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
# from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream
from dt.antlr.CPP14Lexer import CPP14Lexer
from dt.antlr.CPP14Parser import CPP14Parser
from dt.utils import write_row, write_row_final
from dt.utils import file_encoding
import dt.antlr.CPP14ParserListener as CPP14ParserListener
# try out
# from dt.antlr.CPP14ParserVisitor import CPP14ParserVisitor
# try out 2
from antlr4 import ParseTreeWalker
# Option 3 build out, so option 4
from dt.ProjectListener import ProjectParserListener, TranslationUnit
from typing import Optional
from datetime import datetime
import dt.dict_repo_list

list_interest = ["usleep", "sleep", "Sleep", "MSleep", "sleep_for", "sleep_until", "thrd_sleep"]
dict_sleep = {}
# location_file_default = "D:\\GitHub\\AirSim\\MavLinkCom\\src\\impl\\MavLinkConnectionImpl.cpp"
location_file_default = os.path.join("..", "tests", "files", "ast_test_file_6.cpp")
# location_file_default = os.path.join("..", "tests", "files", "ast_test_file_3.cpp")
# location_file_default = "C:\\Users\\Imara\\Documents\\GitHub\\AirSim\\GazeboDrone\\src\\main.cpp"
current_statement = {}
current_number = {}
sleep_found = ""
delim_stand = u"\u25A0"
location_log_files = os.path.join(dt.dict_repo_list.location_github, "CPS_SPA_Detection_Tool", "results")


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
    rule_name = f"{class_name[0].lower()}{class_name[1:]}"
    arr = []
    obj[rule_name] = arr

    if node.children:
        for child_node in node.children:
            child_obj = {}
            arr.append(child_obj)
            _fill(child_obj, child_node)


def reading_tree(tree: CPP14Parser.TranslationUnitContext) -> TranslationUnit:
    """
    Option number 4

    Args:
        tree:
    """
    walker = ParseTreeWalker()
    listener = ProjectParserListener()
    walker.walk(listener, tree)
    return listener.get_translation_unit()


def reading_ast(tree: CPP14Parser.TranslationUnitContext):
    """
    Option number 3

    Args:
        tree:
    """
    walker = ParseTreeWalker()
    w = walker.walk(CPP14ParserListener.CPP14ParserListener(), tree)  # correct
    print(f"{w=}")
    # visit = CPP14ParserVisitor()
    # v = visit.visit(tree)
    # v = CPP14ParserVisitor()
    # print(f"{v=}")


def traverse_rock(node: ParserRuleContext, stack_lst: list = None):
    """
    Option number 2

    Args:
        node:
        stack_lst:
    """
    if stack_lst is None:
        stack_lst = []
    # ## Recursion stop condition
    if isinstance(node, TerminalNodeImpl):
        obj: dict = {"type": node.symbol.type, "name": node.getText(), "line": node.symbol.line}
        stack_lst.append(obj)
        return

    # ## START OF CONTEXTS
    if isinstance(node, CPP14Parser.BlockDeclarationContext):
        # # PUSH MARKER TO STACK
        # print(f'{type(node)=} {node.getChildCount()=}')
        # print(f'\t{type(node.children[0])=} {node.children[0].getChildCount()=}')
        print(f"{type(node).__name__} start: {id(node)=}")
    elif isinstance(node, CPP14Parser.UnqualifiedIdContext):
        print(f"{type(node).__name__} start: {id(node)=}")
    elif isinstance(node, CPP14Parser.SimpleTypeSpecifierContext):
        print(f"{type(node).__name__} start: {id(node)=}")
    elif isinstance(node, CPP14Parser.FunctionDefinitionContext):
        print(f"{type(node).__name__} start: {id(node)=}")
    else:
        # print(f'{type(node)=}')
        pass
    # print(f'{type(node).__name__} {node.getChildren()}')
    # print(node.getTokens(CPP14Parser.IntegerLiteral))
    # print(node.getTokens(CPP14Parser.FloatingLiteral))

    # ## CONTEXT CHILD CONTEXTS DEEPENING
    for child_node in node.getChildren():
        traverse_rock(child_node, stack_lst)

    # ## END OF CONTEXTS
    # # Pop stack until correct context is found
    if isinstance(node, CPP14Parser.BlockDeclarationContext):
        print(f"{type(node).__name__} end: {id(node)=}")
    elif isinstance(node, CPP14Parser.UnqualifiedIdContext):
        print(f"{type(node).__name__} end: {id(node)=}")
        # print(f'{stack_lst.pop()}')
    elif isinstance(node, CPP14Parser.SimpleTypeSpecifierContext):
        print(f"{type(node).__name__} end: {id(node)=}")
    #     for _ in range(node.getChildCount()):
    #         print(f'{stack_lst.pop()}')
    elif isinstance(node, CPP14Parser.FunctionDefinitionContext):
        print(f"{type(node).__name__} end: {id(node)=}")
        for _ in range(node.getChildCount()):
            print(f'{stack_lst.pop()}')


def traverse(nodes: dict):
    """
    Option number 1

    Traversing through the nodes in search for any type that matches the list_interest.

    Args:
        nodes: Containing the (next) branch to search through.
    """
    global current_statement
    global current_number
    global sleep_found
    global dict_sleep

    for i in nodes.keys():
        for j in nodes[i]:
            if "statement" in j.keys():    # is a line
                sleep_found = ""
            if "literal" in j.keys():
                if sleep_found:
                    for end_node in j['literal']:
                        if end_node['type'] == CPP14Parser.IntegerLiteral or \
                                end_node['type'] == CPP14Parser.FloatingLiteral:
                            dict_sleep[end_node["line"]] = (sleep_found, end_node["name"])
            if "type" in j.keys():
                if j["name"] in list_interest:
                    sleep_found = j["name"]
                    dict_sleep[j["line"]] = j["name"]
                    break
            else:
                traverse(j)


def traverse_types(nodes: dict):
    """
    Option number 1, types implementation

    Traversing through the nodes in search for any type that matches the list_interest.

    Args:
        nodes: Containing the (next) branch to search through.
    """
    global current_statement
    global current_number
    global sleep_found
    global dict_sleep

    for i in nodes.keys():
        for j in nodes[i]:
            if "statement" in j.keys():    # is a line
                sleep_found = ""
            if "unqualifiedId" in j.keys():
                if sleep_found:
                    # for end_node in j['unqualifiedId']:
                    #     dict_sleep[end_node["line"]] = (sleep_found, end_node["name"])
                    dict_sleep[j['unqualifiedId']["line"]] = (sleep_found, j['unqualifiedId']["name"])
            if "simpleTypeSpecifier" in j.keys():
                for end_node in j['simpleTypeSpecifier']:
                    print(f"{end_node=}")
                    if "type" in end_node.keys():
                        sleep_found = end_node["line"]
                        previous = dict_sleep[end_node["line"]]
                        dict_sleep[end_node["line"]] = previous + end_node["name"]
                        print(f"{dict_sleep[end_node['line']]=}")
                        break
                else:
                    continue
                break
            else:
                traverse_types(j)
            break


def print_json_to_file(json_str: str) -> None:
    """
    Print JSON to file.
    Args:
        json_str: JSON structure in string form.
    """
    file_name = "json_data_4.json"
    if os.path.exists(file_name):
        print(f"File {file_name} exists, removing file.")
        os.remove(file_name)
    with open(file_name, 'w') as outfile:
        print(f"Creating new {file_name}.")
        outfile.write(json_str)


# def main(csv_writer=None, location_file: str = location_file_default, search_ap: str = "hcft") -> Optional[int]:
def main(csv_writer=None, location_file: str = location_file_default, search_ap: str = "hcft", previous_result: list = [], current_hash: str = "", previous_hash: str = ""):
    if pathlib.Path(location_file).suffix == '.cpp':
        print(f"file name: {location_file}")
        current_statement.clear()
        current_number.clear()
        dict_sleep.clear()
        enc = ""
        # tree_dict = {}
        total_results = 0
        t_res = []

        try:
            enc = file_encoding(location_file)
            source = FileStream(location_file, encoding=enc)
            lexer = CPP14Lexer(source)
            stream = CommonTokenStream(lexer)
            parser = CPP14Parser(stream)
            tree = parser.translationUnit()

            # Option number 4
            t_unit = reading_tree(tree)
            # print(f'{t_unit.functions=}')
            if search_ap == "sleeps":
                for term in list_interest:
                    # t_res.append(t_unit.find_identifier(term))
                    result_interest, number_results = t_unit.find_identifier(term)
                    if result_interest:
                        # t_res.append(result_interest)
                        t_res.extend(result_interest)
                    total_results = total_results + number_results
                # print(f'{t_res=}')
            elif search_ap == "hcft":
                result_interest, number_results = t_unit.get_identifiers_with_numeric_values()
                # print(f"{result_interest=}, {number_results=}")
                if result_interest:
                    t_res.extend(result_interest)
                total_results = total_results + number_results
                # print(f'{t_res=}')
            else:
                print("NOT IMPLEMENTED")
            # print(f"{total_results=}")

            # Possible usage
            # function_of_interest = 'main'
            # func_body = t_unit.get_function_body_for_name(function_of_interest)
            # results = func_body.find_identifier('usleep')
            # print(f'{results=}')

            # Option number 3
            # reading_ast(tree)
            # # walker = ParseTreeWalker()
            # # w = walker.walk(CPP14ParserListener.CPP14ParserListener(), tree)  # correct
            # # print(f"{w=}")
            # # # visit = CPP14ParserVisitor()
            # # # v = visit.visit(tree)
            # # v = CPP14ParserVisitor()not
            # # print(f"{v=}")

            # Option number 2
            # traverse_rock(tree)

            # try out
            # bla = CPP14ParserVisitor()
            # print(f"{bla.visitTranslationUnit(tree)=}")

            # print(f"{tree=}")

            # convert the parse tree to JSON file
            # tree_dict = to_dict(tree)

            # Option number 1
            # traverse(tree_dict)
            # print(f"{tree_dict=}")
            # Option 1 RE
            # traverse_types(tree_dict)

            # """ Temporarily until #5 has been implemented. """
            # for each in dict_sleep:
            #     if type(dict_sleep[each]) != tuple:
            #         dict_sleep[each] = (dict_sleep[each], "UNKNOWN")
            # """ End temp. """

            # Option number 1: print results
            # print(dict_sleep)

            if csv_writer and len(t_res) > 0:
                # write_row(csv_writer, location_file, str(dict_sleep), "None")
                # , previous_result, current_hash, previous_hash
                write_row_final(csv_writer, location_file, str(t_res), enc, previous_result, current_hash, previous_hash)
                # write_row(csv_writer, location_file, str(t_res), enc)
        except UnicodeDecodeError:
            print(f"[ERROR] UnicodeDecodeError: {location_file} encoding={enc}")
            pass
        except FileNotFoundError as e:
            error_fnf = os.path.join(location_log_files, "antlr_error_file_not_found.log")
            with open(error_fnf, 'a') as ef_file:
                now = datetime.now()
                current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                ef_file.write(f"[{current_date_time}] {e}")
            pass

        # print the JSON output
        # json_str = json.dumps(tree_dict, indent=1)
        # print(json_str)
        # print the JSON output to file
        # print_json_to_file(json_str)

        # print the parse tree as lisp
        # print(Trees.toStringTree(tree, parser.ruleNames, parser))
        # return len(dict_sleep)
        return total_results, t_res
    else:
        return 0


if __name__ == "__main__":
    main()
