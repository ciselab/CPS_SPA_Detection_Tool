import glob
import os
from typing import Optional

from chardet import UniversalDetector

from dt.utils.paths import logs_base_path


def remove_file_if_exists(file: os.path) -> None:
    """
    Removes the file given by the `file` param if it exists.
    :param file: The file to remove.
    :return: None
    """
    if os.path.exists(file):
        print(f"File {file} exists, removing file.")
        os.remove(file)


def remove_log_files() -> None:
    """
    Remove all the log files.
    """
    log_files = glob.glob(os.path.join(logs_base_path(), "history_*.log"))
    if log_files:
        print(f"Log files exist, removing {len(log_files)} files.")
    for file in log_files:
        os.remove(file)


def get_file_encoding(file: os.path, _skip_failed_encoding: int = 0, _encoding: str = 'utf-8') -> str:
    """
    Read a file and apply the correct encoding to read the file.

    Args:
        file: Path to the file to be read.
        _encoding: encoding to match against.
        _skip_failed_encoding: Only used when get_file_encoding returns an encoding,
         but Antlr4's FileStream cannot use it.

    Returns:
        encoding: Returns the file's encoding.
    """
    common_encodings = ['utf-8', 'Windows-1252', 'ISO-8859-1', 'cp437']
    encoding_index = common_encodings.index(_encoding)
    _encoding = common_encodings[encoding_index + _skip_failed_encoding]

    try:
        with open(file, 'r', encoding=_encoding):
            pass
    except UnicodeDecodeError:
        """
        Some files are using an encoding that cannot be immediately read.
        To keep the duration of this script as short as possible a selection of encodings
        will be tried first.
        """
        if encoding_index == len(common_encodings) - 1:
            # Tried the last one, chardet will try to detect the encoding
            return __detect_file_encoding(file)
        else:
            return get_file_encoding(file, _skip_failed_encoding, common_encodings[encoding_index + 1])
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
