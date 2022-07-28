#!/usr/bin/env python
"""
Cleanup of HCFT collected data.
"""

import os
import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
cleanup_analysis = os.path.join(ROOT_DIR, "..", "analysis")
cleanup_analysis_done = os.path.join(ROOT_DIR, "..", "cleanup_analysis_done")


def read_file(filename: str) -> None:
    first_result = True
    results_found = 0
    flag_found = False
    file_name = False
    project_name = os.path.splitext(os.path.basename(filename))[0]
    new_filename = os.path.join(cleanup_analysis_done, project_name+"_cleaned.md")
    with open(filename, 'r', encoding='utf-8') as f:
        with open(new_filename, 'a', encoding='utf-8') as nf:
            # print(f"{filename=}")

            print(f"# {project_name}\n")
            nf.write(f"# {project_name}\n")

            result_set = {'filenames': [], 'changes': 0}
            change_set = []
            for line in f:
                line = line.strip()

                if line.startswith("## Result number"):
                    flag_found = False
                    file_name = False
                    if first_result:
                        first_result = False
                        continue
                    # Starting a new resultset
                    # -> Dumping old resultset out.
                    if result_set['changes'] == 0:
                        result_set['filenames'].clear()
                        change_set.clear()
                        continue
                    # print(f"{result_set=}")
                    # print(f"{change_set=}")
                    results_found += 1

                    print(f"## Result number #{results_found}\n")
                    nf.write(f"\n## Result number #{results_found}\n")

                    print("### File name(s):")
                    nf.write("### File name(s):")

                    print('\n'.join(result_set['filenames']), '\n')
                    nf.write('\n'.join(result_set['filenames'])+'\n')

                    print('\n'.join(change_set))
                    nf.write('\n'.join(change_set))

                    # -> Clearing old resultset.
                    result_set['filenames'].clear()
                    result_set['changes'] = 0
                    change_set.clear()
                if file_name:
                    if line == "":
                        file_name = False
                        continue
                    result_set['filenames'].append(line)

                if line == "####Values changed":
                    flag_found = True
                    result_set['changes'] = result_set.get('changes', 0) + 1
                elif line == "####Values removed":
                    flag_found = False
                elif line == "####Values added":
                    flag_found = False
                elif line == "### File name(s)":
                    file_name = True

                if flag_found:
                    if line.startswith("NEW:"):
                        # parse new value
                        new_val = line[4:]
                        try:
                            parsed_new_val = eval(new_val)
                        except NameError as e:
                            result_set['changes'] -= 1
                            change_set.pop()
                            flag_found = False
                            continue
                    elif line.startswith("OLD:"):
                        # parse old value
                        old_val = line[4:]
                        try:
                            parsed_old_val = eval(old_val)
                        except NameError as e:
                            print(f"[ERROR]: {e}; {old_val=}")
                            result_set['changes'] -= 1
                            change_set.pop()
                            change_set.pop()
                            flag_found = False
                            continue
                    elif line.startswith("CHANGED:"):
                        # parse changed value
                        changed_val = line[8:]
                        try:
                            parsed_changed_val = eval(changed_val)
                        except NameError as e:
                            print(f"[ERROR]: {e}; {changed_val=}")
                            continue

                        try:
                            compare_val = int(parsed_changed_val[1])
                        except ValueError:
                            compare_val = float(parsed_changed_val[1])

                        if type(parsed_old_val) is tuple:
                            try:
                                compare_old_val = int(parsed_old_val[1])
                            except ValueError:
                                compare_old_val = float(parsed_old_val[1])
                            old_val_name = parsed_old_val[0]
                        else:
                            compare_old_val = parsed_old_val
                            old_val_name = ""

                        if type(parsed_new_val) is tuple:
                            try:
                                compare_new_val = int(parsed_new_val[1])
                            except ValueError:
                                compare_new_val = float(parsed_new_val[1])
                            new_val_name = parsed_new_val[0]
                        else:
                            compare_new_val = parsed_new_val
                            new_val_name = ""

                        val_not_equal = False
                        if type(compare_old_val) != type(compare_new_val) or compare_old_val != compare_new_val:
                            val_not_equal = True

                        if compare_old_val == compare_val and val_not_equal and new_val_name == old_val_name:
                            # test_res_1 = bool(compare_old_val == compare_val)
                            # test_res_2 = bool(compare_old_val != compare_new_val)
                            # test_res_3 = bool(new_val_name == old_val_name)
                            pass
                        else:
                            # test_res_1 = bool(compare_old_val == compare_val)
                            # test_res_2 = bool(compare_old_val != compare_new_val)
                            # test_res_3 = bool(new_val_name == old_val_name)
                            result_set['changes'] -= 1
                            change_set.pop()
                            change_set.pop()
                            change_set.pop()
                            flag_found = False
                            continue

                    if line == "":
                        flag_found = False
                    change_set.append(line)
            if result_set['changes'] != 0:
                results_found += 1

                print(f"## Result number #{results_found}\n")
                nf.write(f"\n## Result number #{results_found}\n")

                print("### File name(s):")
                nf.write("### File name(s):")

                print('\n'.join(result_set['filenames']), '\n')
                nf.write('\n'.join(result_set['filenames'])+'\n')

                print('\n'.join(change_set))
                nf.write('\n'.join(change_set))


def main() -> None:
    print("Starting Cleanup\n")
    if os.path.exists(os.path.abspath(cleanup_analysis)):

        if not os.path.exists(os.path.abspath(cleanup_analysis_done)):
            os.makedirs(cleanup_analysis_done)
        else:
            for fd in glob.glob(cleanup_analysis_done + "/*.md"):
                os.remove(fd)

        for f in glob.glob(cleanup_analysis + "/*.md"):
            read_file(f)
        # read_file(os.path.join(cleanup_analysis, "ardupilot.md"))
        # read_file(os.path.join(cleanup_analysis, "Arduino.md"))
        # read_file(os.path.join(cleanup_analysis, "Arduino-IRremote.md"))
        # read_file(os.path.join(cleanup_analysis, "ardumower.md"))
    else:
        print("Directory does not exist.")

    # For testing purposes.
    # read_file(os.path.join(ROOT_DIR, "..", "tests", "files", "file_test_analysis_cleanup.md"))


if __name__ == '__main__':
    main()
