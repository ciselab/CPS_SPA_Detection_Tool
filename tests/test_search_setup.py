#!/usr/bin/env python
import pytest
import re
from dt.search_setup import var_name_pattern, use_search_pattern, use_regex_pattern


@pytest.mark.parametrize("line, result", [
    pytest.param('sleep(t_in)',
                 [('sleep', 't_in')],
                 id="sleep(t_in)"),
    pytest.param('sleep_for(t_in)',
                 [('sleep_for', 't_in')],
                 id="sleep_for(t_in)"),
    pytest.param('sleep = t_in',
                 [('sleep', 't_in')],
                 id="sleep = t_in"),
    pytest.param('Sleep(t_in)',
                 [('Sleep', 't_in')],
                 id="Sleep(t_in)"),
    pytest.param('sleep(unit32 t_in)',
                 [('sleep', 't_in')],
                 id="sleep(unit32 t_in)"),
    pytest.param('usleep(t_in)',
                 [('usleep', 't_in')],
                 id="usleep(t_in)"),
])
def test_use_search_pattern(line: str, result: list):
    pattern = use_search_pattern("sleeps_var_name")
    check = list(re.findall(pattern, line))
    assert check == result


@pytest.mark.parametrize("var_name, result", [
    pytest.param('sleep',
                 r"^.*?sleep(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)",
                 id="sleep"),
    pytest.param('sleep_for',
                 r"^.*?sleep_for(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)",
                 id="sleep_for"),
    pytest.param('Sleep',
                 r"^.*?Sleep(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)",
                 id="Sleep"),
    pytest.param('usleep',
                 r"^.*?usleep(?:\s*[=|\(|]\s*|\s+)(?:[a-zA-Z_][a-zA-Z_0-9]*\s)?([a-zA-Z_][a-zA-Z0-9_]*)",
                 id="usleep"),
])
def test_use_regex_pattern(var_name: str, result: list):
    pattern = use_regex_pattern("sleeps_var_name", var_name)
    assert pattern == result


@pytest.mark.parametrize("line, result", [
    pytest.param('time = 84000',
                 [("time", "84000")],
                 id="time = 84000"),
    pytest.param('time 84000',
                 [("time", "84000")],
                 id="time 84000"),
    pytest.param('t_in = 84000',
                 [("t_in", "84000")],
                 id="t_in = 84000"),
    pytest.param('_time 84000',
                 [("_time", "84000")],
                 id="_time 84000"),
    pytest.param('TIME = 84000',
                 [("TIME", "84000")],
                 id="TIME = 84000"),
    pytest.param('T_64 = 64',
                 [("T_64", "64")],
                 id="T_64 = 64"),
    pytest.param('t_in = 8',
                 [("t_in", "8")],
                 id="t_in = 8"),
    pytest.param('t_in = -8',
                 [("t_in", "-8")],
                 id="t_in = -8"),
    pytest.param('t_in = 20',
                 [("t_in", "20")],
                 id="t_in = 20"),
    pytest.param('t_in = 8.0',
                 [("t_in", "8.0")],
                 id="t_in = 8.0"),
    pytest.param('t_in = -20',
                 [("t_in", "-20")],
                 id="t_in = -20"),
    pytest.param('t_in = -2.0',
                 [("t_in", "-2.0")],
                 id="t_in = -2.0"),
    pytest.param('t_in = int 42',
                 [("t_in", "42")],
                 id="t_in = int 42"),
    pytest.param('t_in = uint32 42',
                 [("t_in", "42")],
                 id="t_in = uint32 42"),
    pytest.param('int t_in = 84000',
                 [("t_in", "84000")],
                 id="int t_in = 84000"),
    pytest.param('uint32 t_in = 84000',
                 [("t_in", "84000")],
                 id="uint32 t_in = 84000"),
    pytest.param('uint_32 t_in = 84000',
                 [("t_in", "84000")],
                 id="uint_32 t_in = 84000"),
    pytest.param('time uint32 84000',
                 [("time", "84000")],
                 id="time uint32 84000"),
    # pytest.param('uint32 time 84000',     # Not possible with the current setup
    #              [("time", "84000")],
    #              id="uint32 time 84000"),
    pytest.param('time uint32(84000)',
                 [("time", "84000")],
                 id="time uint32(84000)"),
])
def test_var_name_pattern(line: str, result: list):
    check = list(re.findall(var_name_pattern, line))
    assert check == result
