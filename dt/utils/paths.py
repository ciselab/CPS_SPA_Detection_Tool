import os
from typing import Optional

from dt.utils import location


def build_results_path(project: str) -> Optional[str]:
    """
    Building the path to where the results file should be, checks if exists.

    Args:
        project: Name of the project.

    Returns:
        - Path to the project results file (containing commit hashes).
        - None if path does not exists.

    """
    project_name = str(project + '.txt')
    hash_file_location = os.path.join(location, project_name)
    if os.path.exists(hash_file_location):
        return hash_file_location
    else:
        return None
    