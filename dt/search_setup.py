#!/usr/bin/env python
"""
Patterns used.
"""
import re

var_name_pattern = r'^.*?([a-z_A-Z][a-z_0-9A-Z.]*)(?:\s*=\s*|\s)(?:[a-zA-Z_][a-zA-Z_0-9]*[\s|\(])?([-0-9][0-9.]*)'
var_number_pattern = r'^-*[0-9]+[0-9.]*$'


def use_search_pattern(pattern: str) -> str:
    """
    Collection of patterns to be used.
    Note: Pattern name needs to be without spaces

    Args:
        pattern: Pattern name to be used.
    Returns:
         Regex pattern connected to the pattern name.
    """
    # noinspection SpellCheckingInspection
    dict_search_patterns = {
        "setTimeout": r'^(.*)(setTimeout)',
        "var_with_number": r'([a-z_A-Z][a-z_0-9A-Z.]*)\s*=\s*([-0-9.]+)',
        "numeric_function_within": r"\s*\s*[a-zA-Z_]+\(([a-zA-Z_]+),\s([-0-9.]+)",
        "sleeps": r"^.*?(u*[sS]leep[_for]*)\s*\(*([0-9.]+)",
        "sleeps_var_name": r"^.*?(u*[sS]leep[_for]*)(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)",
    }
    return dict_search_patterns[pattern]


def use_regex_pattern(pattern_name: str, var_name: str) -> str:
    """
    Adjusted regex pattern to include the specific variable name.
    First group is the variable name, second group catches all the numbers.

    Args:
        pattern_name: Pattern name to be used.
        var_name: Var name found in results, needed to add to the pattern.
    Returns:
         Regex patterns connected to the pattern name with the variable name added.
    """
    regex_pattern = ""
    if pattern_name == "var_with_number":
        """var_with_number"""
        regex_pattern = r"\s+" + re.escape(var_name) + r"\s*=\s*([-0-9.]+)"
    elif pattern_name == "numeric_function_within":
        """numeric_function_within"""
        regex_pattern = r"\s*\s*[a-zA-Z_]+\(" + re.escape(var_name) + r",\s([-0-9.]+)"
    elif pattern_name == "sleeps":
        """sleeps"""
        regex_pattern = r"^.*?" + re.escape(var_name) + r"\s*\(*([0-9.]+)"
    elif pattern_name == "sleeps_var_name":
        """sleeps_var_name"""
        regex_pattern = r"^.*?" + re.escape(var_name) + r"(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)"
    else:
        print(f"[ERROR] unknown pattern_name: {pattern_name}")
    return regex_pattern
