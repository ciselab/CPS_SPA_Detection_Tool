import os

import dt


def make_dir_if_not_exists(path_name: os.path) -> None:
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def dt_data_path() -> os.path:
    _data_base_path = os.path.join(os.path.expanduser("~"), "CPS_SPA_Detection_Tool")
    make_dir_if_not_exists(_data_base_path)
    return _data_base_path


def results_base_path() -> os.path:
    path = os.path.join(dt_data_path(), "results")
    make_dir_if_not_exists(path)
    return path


def logs_base_path() -> os.path:
    path = os.path.join(dt_data_path(), "logs")
    make_dir_if_not_exists(path)
    return path


def project_results_path(project_name: str) -> os.path:
    _project_results_path = os.path.join(results_base_path(), project_name)
    make_dir_if_not_exists(_project_results_path)
    return _project_results_path
