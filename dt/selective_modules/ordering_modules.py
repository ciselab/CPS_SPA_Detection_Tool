#!/usr/bin/env python
import csv
import os.path
import re
from os import path, walk
import subprocess
import json
from collections import Counter
import dt.main as dt_main

file = "../../analysis/results.csv"
base_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules"


def checkout_commit(commit_hash_files):
    local = "/home/imara/GitHub/pxprojects/PX4-Autopilot/"
    sel_modules = False     # Do not want to go through a pre-selection set of modules, this is handled differently.
    for each_hash in commit_hash_files:
        print(f"{each_hash=}")
        switching_branch(each_hash, local)
        removing_files(local)
        dt_main.main("PX4-Autopilot", "mwn", each_hash, sel_modules)
    print("END")


def gathering_pxresults_list_aps():
    fieldnames = ['project', 'commit', 'hash', 'message', 'antipattern', 'keyword']
    # list_hash = []
    list_ap = set()
    with open(file, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"', fieldnames=fieldnames)
        for row in reader:
            project = row['project'].strip()
            if project == "PX4-Autopilot":
                antipattern = row['antipattern']
                split_aps = antipattern.splitlines()
                for each in split_aps:
                    list_ap.add(each)
                # if "New:Hard-coded-timing" in antipattern or "New:Hard-coded-fine-tuning" in antipattern:
                #     commit_hash = row['hash']
                #     # hash_link = re.findall(r"\[[a-zA-Z0-9]+]\(([a-zA-Z0-9/.\-:=?]+)\)", commit_hash)
                #     hash_code = re.findall(r"\[([0-9a-z]+)", commit_hash)
                #     # print(f"{hash_code}")
                #     list_hash.append(hash_code[0])
    return list_ap


def gathering_pxresults():
    fieldnames = ['project', 'commit', 'hash', 'message', 'antipattern', 'keyword']
    list_hash = []
    set_hash = set()
    with open(file, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"', fieldnames=fieldnames)
        for row in reader:
            project = row['project'].strip()
            if project == "PX4-Autopilot":
                antipattern = row['antipattern']
                split_antipattern = antipattern.splitlines()
                for each in split_antipattern:
                    if "New:Hard-coded-timing" in each or "New:Hard-coded-fine-tuning" in each:
                        commit_hash = row['hash']
                        # hash_link = re.findall(r"\[[a-zA-Z0-9]+]\(([a-zA-Z0-9/.\-:=?]+)\)", commit_hash)
                        hash_code = re.findall(r"\[([0-9a-z]+)", commit_hash)
                        # print(f"{hash_code}")
                        # list_hash.append(hash_code[0])
                        set_hash.add(hash_code[0])
    ## List returns 299, which is the same results as from study I part 1.
    # return list_hash
    return set_hash


def read_json():
    # json_file = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4.json"
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    print(f"{res}")

    list_files = []

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            data_file = data['files']
            for i in data_file:
                list_files.append(i['filename'])
    print(Counter(list_files).most_common())


def read_json_commit_files():
    # json_file = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4.json"
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)

    list_files = []
    dict_sha_files = {}

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            data_file = data['files']
            sha_file = data['sha']
            commit_files = []
            for i in data_file:
                list_files.append(i['filename'])
                commit_files.append(i['filename'])
            dict_sha_files[sha_file] = commit_files
    # print(Counter(list_files).most_common())
    return dict_sha_files


def read_json_dates():
    # json_file = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4.json"
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    print(f"{res}")

    list_files = []
    dict_files = {}

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            data_file = data['commit']['author']['date']
            list_files.append(data_file)
            dict_files[data_file] = data['sha']
            # print(data_file)
            # for i in data_file:
            #     print(i)
            #     list_files.append(i['date'])
    # print(Counter(list_files).most_common())
    list_files.sort()
    # print(list_files)
    # print(dict_files)
    for date in list_files:
        print(f"{date} : {dict_files[date]}")


def single_read_json(filename='src/modules/mavlink/mavlink_main.cpp'):
    # json_file = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4.json"
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    print(f"{res}")

    # list_files = []

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            data_file = data['files']
            sha_current = data['sha']
            for i in data_file:
                if filename in i['filename']:
                    print(sha_current)
    #             list_files.append(i['filename'])
    # print(Counter(list_files).most_common())


def single_read_sha_json(sha_search):
    # json_file = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4.json"
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    # print(f"{res}")

    # list_files = []

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            # data_file = data['files']
            sha_current = data['sha']
            if sha_search == sha_current:
                date_sha = data['commit']['author']['date']
                # print(f"{sha_current} {date_sha}")
                return date_sha


def gather_hash_from_files():
    filename_base = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_part2_aps/"
    filename_one = "hcft_adjusted.txt"
    filename_two = "mwn_adjusted.txt"
    filename_list = [os.path.join(filename_base, filename_one), os.path.join(filename_base, filename_two)]
    for file_res in filename_list:
        with open(file_res) as f:
            lines = f.readlines()
            for line in lines:
                hash_commit_pt = line.strip()
                # print(hash_commit_pt)
                gather_files(hash_commit_pt)


def gather_files(each_hash):
    script_workflow = path.join(base_path, "gather_files.sh")
    subprocess.run([script_workflow, each_hash])


def switching_branch(each_hash, dir_project):
    script_workflow = path.join(base_path, "switching_branch.sh")
    # subprocess.run([script_workflow, each_hash, dir_project])
    # sb_process = subprocess.Popen([script_workflow, each_hash, dir_project])
    # sb_process.wait()
    sb_process = subprocess.check_call([script_workflow, each_hash, dir_project])
    print(f"{sb_process=}")


def removing_files(dir_project):
    script_workflow = path.join(base_path, "remove_files.sh")
    # subprocess.run([script_workflow, dir_project])
    # rf_process = subprocess.Popen([script_workflow, dir_project])
    # rf_process.wait()
    rf_process = subprocess.check_call([script_workflow, dir_project])
    print(f"{rf_process=}")


def compare_lists():
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    # print(f"{res}")

    dict_sha = {}

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            list_files = []
            data_file = data['files']
            for i in data_file:
                data_filename = i['filename']
                # list_files.append(data_filename.strip())
                list_files.append(data_filename)
            dict_sha[data['sha']] = list_files
    print(dict_sha)
    print(f"{len(dict_sha)=}")

    file_results_hcft_mwn = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4_server/PX4-Autopilot/results_hcft_mwn_px4.csv"

    # remove_keys = []
    remove_keys = set()

    with open(file_results_hcft_mwn) as fr:
        lines = fr.readlines()
        for line in lines:
            for key in dict_sha:
                for each in dict_sha[key]:
                    if each == line.strip():
                        # print(key)
                        # remove_keys.append(key)
                        remove_keys.add(key)
    print(remove_keys)

    for each_key in remove_keys:
        del dict_sha[each_key]
    print(dict_sha)
    print(f"{len(dict_sha)=}")

    list_dates = []
    for each_sha_result in dict_sha:
        result_date = single_read_sha_json(each_sha_result)
        list_dates.append(result_date)

    list_dates.sort()
    print(list_dates)


def check_line_file_commit(lines_lf, dict_sha, commit):
    # print(f"{dict_sha[commit]=}")
    # print(f"{commit=}")
    # print(f"{lines_lf=}")
    for each_file in dict_sha[commit]:
        each_file_adjusted = "./"+each_file
        # print(each_file_adjusted)
        # print(lines_lf)
        if each_file_adjusted in lines_lf:
            return commit, dict_sha[commit]
    return None


def final_compare_lists():
    dir_path = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results"
    res = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        dir_file = file_names
        res.extend(dir_file)
    # print(f"{res}")

    dict_sha = {}

    for file_from_dir in res:
        file_path = os.path.join(dir_path, file_from_dir)
        with open(file_path) as f:
            data = json.loads(f.read())
            list_files = []
            data_file = data['files']
            for i in data_file:
                data_filename = i['filename']
                # list_files.append(data_filename.strip())
                list_files.append(data_filename)
            dict_sha[data['sha']] = list_files
    # print(dict_sha)
    # print(f"{len(dict_sha)=}")
    # This is a dict with all commits, including non-C++ files projects

    dict_considered_commits = {}

    # dir_path_list_files = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/list_files_keep_v3.txt"
    dir_path_list_files = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4_server/PX4-Autopilot/files_in_project.txt"
    with open(dir_path_list_files) as lf:
        lines_lf = lf.readlines()
        list_llf = []
        for llf in lines_lf:
            list_llf.append(llf.strip())
        for each_commit_all in dict_sha:
            # print(f"{dict_sha[each_commit_all]=}")
            # print(f"{lines_lf=}")
            comparison_res = check_line_file_commit(list_llf, dict_sha, each_commit_all)
            if comparison_res is not None:
                comparison_res_hash, comparison_res_files = comparison_res
                # print(f"{comparison_res=}")
                # print(f"{comparison_res_hash=} {comparison_res_files=}")
                dict_considered_commits[comparison_res_hash] = comparison_res_files
    print(f"{dict_considered_commits=}")

    file_results_hcft_mwn = "/home/imara/GitHub/CPS_SPA_Detection_Tool/dt/selective_modules/results_px4_server/PX4-Autopilot/results_hcft_mwn_px4.csv"

    # remove_keys = []
    remove_keys = set()

    with open(file_results_hcft_mwn) as fr:
        lines = fr.readlines()
        for line in lines:
            for key in dict_considered_commits:
                for each in dict_considered_commits[key]:
                    if each == line.strip():
                        # print(key)
                        # remove_keys.append(key)
                        remove_keys.add(key)
    print(remove_keys)

    print(f"{len(dict_considered_commits)=}")
    for each_key in remove_keys:
        del dict_considered_commits[each_key]
    print(dict_considered_commits)
    print(f"{len(dict_considered_commits)=}")

    list_dates = []
    for each_sha_result in dict_considered_commits:
        result_date = single_read_sha_json(each_sha_result)
        list_dates.append(result_date)

    list_dates.sort()
    print(list_dates)


def main():
    # Gathering all hashes
    list_hash = gathering_pxresults()
    print(f"Commits to analyse: {len(list_hash)}")

    # Gather hashes, from study 1 part 1
    for each in list_hash:
        gather_files(each)

    # [OPTIONAL] Ordering from most common to the least common (s1p1)
    # read_json()

    # [OPTIONAL] Print hash for single file. (s1p1)
    # single_read_json()

    # [OPTIONAL] Print ordering by date. (s1p1)
    # read_json_dates()

    # [OPTIONAL] Print out all occurring aps (s1p1)
    # results = gathering_pxresults_list_aps()
    # print(results)

    # [OPTIONAL] gather files from file of hashes, study 1 part 2
    # includes gather_files()
    gather_hash_from_files()

    # nr.6) commit hash with files list
    res_hash_files = read_json_commit_files()
    print(f"{res_hash_files=}")
    checkout_commit(res_hash_files)

    # [NEEDS ADJUSTMENTS] Compare lists
    # compare_lists()
    # final_compare_lists()


if __name__ == "__main__":
    main()
