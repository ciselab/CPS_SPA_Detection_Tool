#!/usr/bin/env python
import pytest
from dt.search_current_git_blame import cleanup_results_to_list_v2 as rtl

# noinspection SpellCheckingInspection


@pytest.mark.parametrize("input_line_nr, result", [
    pytest.param(0,
                 [('sleep', '30', '151', '# Wait a bit longer after bootup, before copying binaries to the target.')],
                 id="Short input test 1."),
    pytest.param(1,
                 [('sleep', '5', '186', '${minidmPath}/mini-dm > minidm.log &')],
                 id="Short input test 2."),
    pytest.param(2,
                 [('sleep', '20', '205', 'fi')],
                 id="Short input test 3."),
    pytest.param(3,
                 [('sleep', '5', '215', 'adb shell "ps -eaf | grep px4 | grep -v grep | awk \'{print $2}\' | tr -s \' \' | cut -d\' \' -f2 | xargs kill"')],
                 id="Short input test 4."),
    pytest.param(4,
                 [('sleep', '30', '151', '# Wait a bit longer after bootup, before copying binaries to the target.'),
                  ('sleep', '5', '186', '${minidmPath}/mini-dm > minidm.log &'),
                  ('sleep', '20', '205', 'fi'),
                  ('sleep', '5', '215', 'adb shell "ps -eaf | grep px4 | grep -v grep | awk \'{print $2}\' | tr -s \' \' | cut -d\' \' -f2 | xargs kill"')],
                 id="Multiple inputs test."),
    pytest.param(5,
                 [('sleep', '0.1', '42', 'while (true) {')],
                 id="Short input test with var 0.1."),
    pytest.param(6,
                 [('sleep', '0.3', '151', '# Wait a bit longer after bootup, before copying binaries to the target.'),
                  ('sleep', '0.5', '186', '${minidmPath}/mini-dm > minidm.log &'),
                  ('sleep', '1.2', '205', 'fi'),
                  ('sleep', '4.5', '215',
                   'adb shell "ps -eaf | grep px4 | grep -v grep | awk \'{print $2}\' | tr -s \' \' | cut -d\' \' -f2 | xargs kill"')],
                 id="Multiple inputs test with vars x.x."),
    pytest.param(7,
                 [('sleep_for', '0.5', '92', '//Get into position')],
                 id="Short sleep_for test with 0.5 var.")
])
def test_string_results_to_list(input_line_nr: int, result: list):
    with open("data_strings.txt", 'r', encoding='utf-8') as input_file:
        for line_number, each in enumerate(input_file):
            if line_number == input_line_nr:
                result_func = rtl(each)
                assert result_func == result
                break
