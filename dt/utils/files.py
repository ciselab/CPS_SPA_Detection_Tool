import os
from typing import Optional
from chardet import UniversalDetector


def file_encoding(file: os.path, enc_select: str = 'utf-8', enc=None) -> str:
    """
    Read a file and apply the correct encoding to read the file.

    Args:
        file: Path to the file to be read.
        enc_select: current encoding.
        enc: encoding in list location.

    Returns:
        enc: Returns the file's encoding.
    """
    encodings_options = ['Windows-1252', 'ascii']

    if isinstance(enc, int):
        if enc >= len(encodings_options):
            """
            Tried encodings still not correct, continue to use chardet.
            """
            det_enc = no_encoding_found(file)
            if det_enc:
                enc_select = det_enc
        elif enc < len(encodings_options):
            enc_select = encodings_options[enc]
    try:
        with open(file, 'r', encoding=enc_select):
            print(f"encoding: {enc_select}")
    except UnicodeDecodeError:
        """
        Some files are using an encoding that cannot be immediately read.
        Most of these files, seem to be using Windows-1252 followed by utf-8 encoding.
        To keep the duration of this script as short as possible, this encoding will be tried first.
        """
        if not isinstance(enc, int):
            enc = 0
        elif not enc >= len(encodings_options):
            enc = encodings_options.index(enc_select) + 1
        if not enc >= len(encodings_options):
            file_encoding(file, enc_select, enc)
    except Exception as e:
        print(f"Different error encountered: {file}, error: {e}")
    return enc_select


def no_encoding_found(file: os.path) -> Optional[str]:
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
            enc = detector.result["encoding"]
            if enc:
                print(f"[ENCODING]: {enc}")
                return enc
            else:
                print("[ENCODING]: No encoding result.")
        else:
            print("[ENCODING]:No Result from detector.")
    except UnicodeDecodeError:
        """
        In case chardet is not able to detect which encoding was used.
        """
        print(f"UnicodeDecodeError: {file}")