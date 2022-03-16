import os

import dt


def make_dir_if_not_exists(path_name: os.path) -> None:
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def EnsurePathExistence(func):
    def wrapper(*args, **kwargs):
        path = func(*args, **kwargs)
        make_dir_if_not_exists(path)
        return path
    return wrapper


@EnsurePathExistence
def dt_data_path() -> os.path:
    return os.path.join(os.path.expanduser("~"), "cps-spa-detection-tool")


@EnsurePathExistence
def results_base_path() -> os.path:
    return os.path.join(dt_data_path(), "results")


@EnsurePathExistence
def logs_base_path() -> os.path:
    return os.path.join(dt_data_path(), "logs")


@EnsurePathExistence
def project_results_path(project_name: str) -> os.path:
    return os.path.join(results_base_path(), project_name)
