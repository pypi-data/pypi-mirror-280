"""This module contains the BaseWarning class, which is the base class for all validation warnings."""
import os


class BaseWarning:
    """The Base class to represent any type of validation warning."""

    def __init__(self, file_path: str, lineno: int, message: str, source_code: str, warning_code: str):
        """Initializes the BaseWarning class."""
        self.lineno = lineno
        self.message = message
        self.__source_code_lines = source_code.split("\n")
        self.code_line = self.__source_code_lines[lineno - 1]
        self.code_lines = "\n".join(self.__source_code_lines[lineno - 3 : lineno + 2])
        self.file_path = file_path.replace(os.getcwd(), "").strip(os.sep)
        self.warning_code = warning_code
