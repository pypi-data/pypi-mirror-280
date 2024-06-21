"""
This module provides the Input class for handling input data.

The Input class is designed as a singleton to ensure only one instance
manages the input data throughout the application. It supports loading
data from a specified JSON file.
"""

import json
import os
from .constants import INPUT_FILE_NAME

__all__ = ["Input"]


class Input:
    """
    This class represents the input module.
    It provides methods to load data from an input file and retrieve specific values from the loaded data.
   
    Attributes:
        data (dict): A dictionary to store input data.
    
    """

    _instance = None 
    data: dict = {}

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of the Input class if it doesn't already exist.
        """
        if cls._instance is None:
            cls._instance = super(Input, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initialize the Input class by loading data from the input file.
        """
        if not self.data:
            self.load_data()

    def input_file_path(self) -> str:
        """
        Constructs the file path to the input data file.

        Returns:
            str: The file path to the input data file.
        """
        return os.path.join(os.getcwd(), INPUT_FILE_NAME)

    def load_data(self, file_path: str = None):
        """
        Load data from the input file.
        Args:
            file_path: The path of the input file. If not provided, the default input file path will be used.
        Raises:
            FileNotFoundError: If the input file is not found.
            json.JSONDecodeError: If there is an error while decoding JSON from the input file.
            Exception: If there is an error while loading data from the input file.
        """
        try:
            file_path = file_path or self.input_file_path()
            with open(file_path, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Input file {file_path} not found, error: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error while decoding JSON from input file {file_path}, error: {e}", e.doc, e.pos)
        except Exception as e:
            raise Exception(f"Error while loading data from input file {file_path}, error: {e}")

    def get_value(self, key):
        """
        Get the value associated with the given key from the loaded data.
        Args:
            key: The key to retrieve the value for.
        Returns:
            The value associated with the given key, or None if the key is not found.
        """
        return self.data.get(key)

    def get_open_api_url(self):
        """
        Get the Open API URL from the loaded data.
        Returns:
            The Open API URL.
        """
        return self.get_value("cwOpenAPIURL")
