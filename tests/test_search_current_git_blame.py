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
])
def test_string_results_to_list(input_line_nr: int, result: list):
    with open("data_strings.txt", 'r', encoding='utf-8') as input_file:
        for line_number, each in enumerate(input_file):
            if line_number == input_line_nr:
                result_func = rtl(each)
                assert result_func == result
                break
