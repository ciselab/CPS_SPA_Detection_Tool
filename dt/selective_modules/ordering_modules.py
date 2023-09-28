#!/usr/bin/env python
import csv
import re
from os import path, walk
import subprocess
import json
import dt.main as dt_main
from typing import List, Dict
import dt.selective_modules.results_part_one.analysis_results as ro
from dt.dict_repo_list import projects as dpr
import shutil
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context

file = path.abspath(ro.get_results_file_path())
base_path = path.dirname(path.realpath(__file__))

file_extensions: Dict[str, List[str]] = {
            'cpp': ['.c', '.cpp', '.h', '.hpp', '.cxx', '.cc', '.hh', '.h++'],
        }

MAX_WORKERS = 27        # For Docker usage.
# MAX_WORKERS = 2       # For home usage.


def cp_mv_project(each_hash, local):
    split_path_project = path.split(local)
    new_tail = f"{split_path_project[1]}_{each_hash}"
    new_path = path.join(split_path_project[0], new_tail)
    print(f"{new_path=}")
    if not path.exists(new_path):
        shutil.copytree(local, new_path)
    return new_path


def checkout_commit(dict_sel_commits: dict):
    local = path.join(path.expanduser("~"), "GitHub", "pxprojects", "PX4-Autopilot")
    sel_modules = False     # Do not want to go through a pre-selection set of modules, this is handled differently.
    context = get_context('spawn')
    print("START POOL")
    with ProcessPoolExecutor(max_workers=MAX_WORKERS, mp_context=context) as executor:
        future_to_file = {executor.submit(
            start_dt, each_hash, local, dict_sel_commits, sel_modules): each_hash for each_hash in dict_sel_commits}
    print("Finished Detection Tool.")


def start_dt(each_hash, local, dict_sel_commits, sel_modules):
    new_local = cp_mv_project(each_hash, local)
    switching_branch(each_hash, new_local)
    list_files_keep = dict_sel_commits[each_hash]['commit_files']
    removing_files(new_local, list_files_keep, each_hash)
    dpr["PX4-Autopilot"]['local'] = new_local
    dpr["PX4-Autopilot"]['sha'] = each_hash
    print(f"New local: {new_local}, same as:")
    print(dpr["PX4-Autopilot"]['local'])
    history_project = False
    if 'mwn' in dict_sel_commits[each_hash]['antipatterns']:
        dt_main.main("PX4-Autopilot", "mwn", each_hash, sel_modules, history_project)
    if 'hcft' in dict_sel_commits[each_hash]['antipatterns']:
        dt_main.main("PX4-Autopilot", "hcft", each_hash, sel_modules, history_project)


def gathering_pxresults():
    fieldnames = ['project', 'commit', 'hash', 'message', 'antipattern', 'keyword']
    set_hash_hcft = set()
    set_hash_mwn = set()
    with open(file, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"', fieldnames=fieldnames)
        for row in reader:
            project = row['project'].strip()
            if project == "PX4-Autopilot":
                antipattern = row['antipattern']
                split_antipattern = antipattern.splitlines()
                for each in split_antipattern:
                    if "New:Hard-coded-timing" in each:
                        commit_hash = row['hash']
                        hash_code = re.findall(r"\[([0-9a-z]+)", commit_hash)
                        set_hash_mwn.add(hash_code[0])
                    if "New:Hard-coded-fine-tuning" in each:
                        commit_hash = row['hash']
                        hash_code = re.findall(r"\[([0-9a-z]+)", commit_hash)
                        set_hash_hcft.add(hash_code[0])
    return set_hash_mwn, set_hash_hcft


def read_json_commit_files():
    dir_path = path.join(base_path, "px_commit_results")
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)

    dict_sha_files = {}
    for file_from_dir in res:
        file_path = path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            data_file = data['files']
            sha_file = data['sha']
            commit_files = []
            found_cpp_type_file = False
            for i in data_file:
                filename = i['filename']
                _, filename_ext = path.splitext(filename)
                if filename_ext.lower() in file_extensions["cpp"]:
                    found_cpp_type_file = True
                commit_files.append(filename)
            if found_cpp_type_file:
                dict_sha_files[sha_file] = {'commit_files': commit_files, 'antipatterns': []}
    return dict_sha_files


def added_aps_to_res(dict_commits, a_hash_mwn, a_hash_hcft, b_hash_hcft, b_hash_mwn):
    for key in dict_commits:
        if key in a_hash_mwn or key in b_hash_mwn:
            current_list_antipatterns = dict_commits[key]['antipatterns']
            current_list_antipatterns.append('mwn')
            dict_commits[key]['antipatterns'] = current_list_antipatterns
        if key in a_hash_hcft or key in b_hash_hcft:
            current_list_antipatterns = dict_commits[key]['antipatterns']
            current_list_antipatterns.append('hcft')
            dict_commits[key]['antipatterns'] = current_list_antipatterns
    return dict_commits


def single_read_sha_json(sha_search):
    dir_path = path.join(base_path, "px_commit_results")
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)

    for file_from_dir in res:
        file_path = path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            sha_current = data['sha']
            if sha_search == sha_current:
                date_sha = data['commit']['author']['date']
                return date_sha


def gather_hash_from_files():
    filename_base = path.join(base_path, "px_part2_aps")
    filename_one = "hcft_adjusted.txt"
    filename_two = "mwn_adjusted.txt"
    list_hcft = set()
    list_mwn = set()
    list_aps = [list_hcft, list_mwn]
    list_total_aps = set()
    filename_list = [path.join(filename_base, filename_one), path.join(filename_base, filename_two)]
    for number, file_res in enumerate(filename_list):
        with open(file_res) as f:
            lines = f.readlines()
            for line in lines:
                hash_commit_pt = line.strip()
                list_aps[number].add(hash_commit_pt)
                list_total_aps.add(hash_commit_pt)
    for each_hash in list_total_aps:
        gather_files(each_hash)
    return list_total_aps, list_hcft, list_mwn


def gather_files(each_hash):
    script_workflow = path.join(base_path, "gather_files.sh")
    subprocess.run([script_workflow, each_hash])


def switching_branch(each_hash, dir_project):
    script_workflow = path.join(base_path, "switching_branch.sh")
    sb_process = subprocess.check_call([script_workflow, each_hash, dir_project])
    print(f"{sb_process=}")


def prep_keep_list(list_files_keep):
    prepped_keep_list = ""
    for each_file in list_files_keep:
        prepped_keep_list = r"./"f"{each_file}"f"\|"
    return prepped_keep_list


def removing_files(dir_project, list_files_keep, each_hash):
    keep_list = prep_keep_list(list_files_keep)
    script_workflow = path.join(base_path, "remove_files.sh")
    rf_process = subprocess.check_call([script_workflow, dir_project, keep_list, each_hash])
    print(f"{rf_process=}")


# def compare_lists():
#     dir_path = path.join(base_path, "px_commit_results")
#     res = []
#     for (dir_path, dir_names, file_names) in walk(dir_path):
#         dir_file = file_names
#         res.extend(dir_file)
#
#     dict_sha = {}
#     for file_from_dir in res:
#         file_path = path.join(dir_path, file_from_dir)
#         with open(file_path) as f:
#             data = json.loads(f.read())
#             list_files = []
#             data_file = data['files']
#             for i in data_file:
#                 data_filename = i['filename']
#                 list_files.append(data_filename)
#             dict_sha[data['sha']] = list_files
#     print(dict_sha)
#     print(f"{len(dict_sha)=}")
#
#     file_results_hcft_mwn = path.join(base_path, "results_px4_server", "PX4-Autopilot", "results_hcft_mwn_px4.csv")
#
#     remove_keys = set()
#     with open(file_results_hcft_mwn) as fr:
#         lines = fr.readlines()
#         for line in lines:
#             for key in dict_sha:
#                 for each in dict_sha[key]:
#                     if each == line.strip():
#                         remove_keys.add(key)
#     print(remove_keys)
#
#     for each_key in remove_keys:
#         del dict_sha[each_key]
#     print(dict_sha)
#     print(f"{len(dict_sha)=}")
#
#     list_dates = []
#     for each_sha_result in dict_sha:
#         result_date = single_read_sha_json(each_sha_result)
#         list_dates.append(result_date)
#
#     list_dates.sort()
#     print(list_dates)


# def check_line_file_commit(lines_lf, dict_sha, commit):
#     for each_file in dict_sha[commit]:
#         each_file_adjusted = "./"+each_file
#         if each_file_adjusted in lines_lf:
#             return commit, dict_sha[commit]
#     return None


# def final_compare_lists():
#     dir_path = path.join(base_path, "px_commit_results")
#     res = []
#     for (dir_path, dir_names, file_names) in walk(dir_path):
#         dir_file = file_names
#         res.extend(dir_file)
#
#     dict_sha = {}
#     for file_from_dir in res:
#         file_path = path.join(dir_path, file_from_dir)
#         with open(file_path) as f:
#             data = json.loads(f.read())
#             list_files = []
#             data_file = data['files']
#             for i in data_file:
#                 data_filename = i['filename']
#                 list_files.append(data_filename)
#             dict_sha[data['sha']] = list_files
#
#     dict_considered_commits = {}
#     dir_path_list_files = path.join(base_path, "results_px4_server", "PX4-Autopilot", "files_in_project.txt")
#     with open(dir_path_list_files) as lf:
#         lines_lf = lf.readlines()
#         list_llf = []
#         for llf in lines_lf:
#             list_llf.append(llf.strip())
#         for each_commit_all in dict_sha:
#             comparison_res = check_line_file_commit(list_llf, dict_sha, each_commit_all)
#             if comparison_res is not None:
#                 comparison_res_hash, comparison_res_files = comparison_res
#                 dict_considered_commits[comparison_res_hash] = comparison_res_files
#     print(f"{dict_considered_commits=}")
#
#     file_results_hcft_mwn = path.join(base_path, "results_px4_server", "PX4-Autopilot", "results_hcft_mwn_px4.csv")
#
#     remove_keys = set()
#     with open(file_results_hcft_mwn) as fr:
#         lines = fr.readlines()
#         for line in lines:
#             for key in dict_considered_commits:
#                 for each in dict_considered_commits[key]:
#                     if each == line.strip():
#                         remove_keys.add(key)
#     print(remove_keys)
#
#     print(f"{len(dict_considered_commits)=}")
#     for each_key in remove_keys:
#         del dict_considered_commits[each_key]
#     print(dict_considered_commits)
#     print(f"{len(dict_considered_commits)=}")
#
#     list_dates = []
#     for each_sha_result in dict_considered_commits:
#         result_date = single_read_sha_json(each_sha_result)
#         list_dates.append(result_date)
#
#     list_dates.sort()
#     print(list_dates)


def main():
    print("START")
    start_time = datetime.now()
    current_time = start_time.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    # Gathering all hashes
    list_hash_mwn, list_hash_hcft = gathering_pxresults()
    list_hash = set()
    for each_mwn in list_hash_mwn:
        list_hash.add(each_mwn)
    for each_hcft in list_hash_hcft:
        list_hash.add(each_hcft)
    print(f"Commits to analyse, mwn: {len(list_hash_mwn)}, hcft: {len(list_hash_hcft)}")
    print(f"Unique commits to analyse in total: {len(list_hash)}")

    # Gather hashes, from study 1 part 1
    for each in list_hash:
        gather_files(each)

    # Gather files from file of hashes, study 1 part 2
    # includes the gather_files() function
    res_list_total_aps, res_list_hcft, res_list_mwn = gather_hash_from_files()
    print(f"Number of unique commits to analyse (of part 2): hcft={len(res_list_hcft)} mwn={len(res_list_mwn)}")
    print(f"Total number of unique commits to analyse (of part 2): {len(res_list_total_aps)}")

    # nr.6) commit hash with files list, and at least 1 C++ type file in commit.
    res_hash_files = read_json_commit_files()
    print(f"{res_hash_files=}")

    # APs into commits
    # part 1: list_hash_mwn, list_hash_hcft
    # part 2: res_list_hcft, res_list_mwn
    res_hash_files_aps = added_aps_to_res(res_hash_files, list_hash_mwn, list_hash_hcft, res_list_hcft, res_list_mwn)
    print(f"Number of commits for analyses (both APs): {len(res_hash_files_aps)=}")
    print(f"{res_hash_files_aps=}")

    # nr.6) running
    checkout_commit(res_hash_files_aps)

    # [NEEDS ADJUSTMENTS] Compare lists
    # compare_lists()
    # final_compare_lists()

    end_time = datetime.now()
    diff_time = end_time - start_time
    print("END")
    current_time = end_time.strftime("%H:%M:%S")
    print(f"End time: {current_time}")
    print(f"Duration of the script: {diff_time=}")


if __name__ == "__main__":
    main()
