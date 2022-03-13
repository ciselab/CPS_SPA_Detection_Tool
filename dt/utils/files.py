import os
from typing import Optional, List, Dict
from chardet import UniversalDetector

import dt.dict_repo_list


def remove_file_if_exists(file: os.path) -> None:
    """
    Removes the file given by the `file` param if it exists.
    :param file: The file to remove.
    :return: None
    """
    if os.path.exists(file):
        print(f"File {file} exists, removing file.")
        os.remove(file)


def get_file_encoding(file: os.path, _encoding: str = 'utf-8') -> str:
    """
    Read a file and apply the correct encoding to read the file.

    Args:
        file: Path to the file to be read.
        _encoding: encoding to match against.

    Returns:
        encoding: Returns the file's encoding.
    """
    common_encodings = ['utf-8', 'Windows-1252']
    encoding_index = common_encodings.index(_encoding)

    try:
        with open(file, 'r', encoding=_encoding):
            pass
    except UnicodeDecodeError:
        """
        Some files are using an encoding that cannot be immediately read.
        Most of these files, seem to be using Windows-1252 followed by utf-8 encoding.
        To keep the duration of this script as short as possible, this encoding will be tried first.
        """
        if encoding_index == len(common_encodings) - 1:
            # we tried the last one
            return __detect_file_encoding(file)
        else:
            return get_file_encoding(file, common_encodings[encoding_index + 1])
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    return _encoding


def __detect_file_encoding(file: os.path) -> Optional[str]:
    """
    When the default, Windows-1252 and utf-8 encoding is not correct, chardet is being used.
    This tool tries to detect which encoding is used.

    Args:
        file: Location of the file to find type of encoding used.

    Returns:
        Encoding used in the file, detected by chardet.
    """
    try:
        with open(file, "rb") as rd_file:
            raw_data = rd_file.readlines()
            detector = UniversalDetector()
            for rd_line in raw_data:
                detector.feed(rd_line)
                if detector.done:
                    break
            detector.close()
        if detector.result:
            encoding = detector.result["encoding"]
            if encoding:
                print(f"[ENCODING]: {encoding}")
                return encoding
            else:
                print("[ENCODING]: No encoding result.")
        else:
            print("[ENCODING]:No Result from detector.")
    except UnicodeDecodeError:
        """
        In case chardet is not able to detect which encoding was used.
        """
        print(f"UnicodeDecodeError: {file}")


def get_project_files(project_name: str, language: str = 'cpp') -> set:
    """
    Goes through the dirs, noted in dt.dict_repo_list.projects_modules, and returns the files of interest.

    Args:
        project_name: Name (key) of the project.
        language: the programming language to find files for.

    Returns:
        Set of the files (full path).
    """
    file_set = set()
    # noinspection SpellCheckingInspection
    file_extensions: Dict[str, List[str]] = {
        'cpp': ['.c', '.cpp', '.h', '.hpp', '.cxx', '.cc', '.hh', '.h++'],
    }
    # search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
    #                  '.ipp', '.inl', '.txx', '.tpp', '.tpl',
    #                  '.c++m', '.cppm', '.cxxm', '.kt',
    #                  '.java', '.go', '.py', '.rb', '.rs',
    #                  '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']
    project_directory = dt.dict_repo_list.projects[project_name]["local"]

    for top_level, recursive in dt.dict_repo_list.projects_modules[project_name]:
        directory_path = os.path.join(project_directory, top_level)
        for root, dirs, files in os.walk(directory_path, topdown=True):
            if not recursive:
                dirs.clear()
            for filename in files:
                file_path = os.path.join(root, filename)
                _, filename_ext = os.path.splitext(filename)
                if filename_ext.lower() in file_extensions[language]:
                    file_set.add(file_path)

    return file_set


def intermediary_results_filename(project_name: str, pattern_name: str) -> str:
    return f"{pattern_name}_{project_name}_results.csv"

