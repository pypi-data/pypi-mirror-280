import os
import json

from .constants import (
    LOG_FILE_NAME,
    OUTPUT_DIR_NAME,
    RESULT_FILE_NAME,
)


def get_logger_file_path():
    """
    Constructs and returns the file path for the log file.
    The log file is located in the OUTPUT_DIR_NAME directory in the current working directory.
    If the directory does not exist, it is created.
    """
    log_file_path = os.path.join(os.getcwd(), OUTPUT_DIR_NAME, LOG_FILE_NAME)
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    return log_file_path


def get_result_file_path():
    """
    Constructs and returns the file path for the result file.
    The result file is located in the OUTPUT_DIR_NAME directory in the current working directory.
    If the directory does not exist, it is created.
    """
    result_file_path = os.path.join(os.getcwd(), OUTPUT_DIR_NAME, RESULT_FILE_NAME)
    os.makedirs(os.path.dirname(result_file_path), exist_ok=True)
    return result_file_path


def write_json_to_file(file_path, data):
    """
    Writes the given data to a file at the given file path.
    The data is written in JSON format with an indentation of 4 spaces.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
