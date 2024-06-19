"""Main module."""
import os
import ast
from libraries.t_bug_catcher import ConfigureCallVisitor, IncorrectTryBlockVisitor
from libraries import BaseWarning, validation_logger

MAIN_FILENAMES = ["task.py", "main.py"]


class ThoughtfulHook:
    """Main class for the plugin."""

    name = "flake8-thoughtful"
    version = "0.1.0"

    def __init__(self, tree, filename):
        """Initialize the checker."""
        self.filename = filename
        self.warnings: list[BaseWarning] = []

    def check_for_warnings(self, visitor: ast.NodeVisitor, warning_code: str):
        """Inspects file's ast tree using visitor and collect warnings."""
        with open(self.filename, "r", encoding="utf8") as source:
            source_code = source.read()

            try:
                tree = ast.parse(source_code, filename=self.filename)
            except SyntaxError:
                return
            except Exception as ex:
                validation_logger.error(f"Unable to validate: {self.filename} - {ex}")
                return

            visitor = visitor()
            visitor.visit(tree)

        for line, message in visitor.get_errors().items():
            warn = BaseWarning(self.filename, line, message, source_code=source_code, warning_code=warning_code)
            self.warnings.append(warn)

    def run(self):
        """Checks for warnings in the file."""
        self.check_for_warnings(IncorrectTryBlockVisitor, "THO002")
        if os.path.basename(self.filename) in MAIN_FILENAMES:
            self.check_for_warnings(ConfigureCallVisitor, "THO001")

        for warning in self.warnings:
            yield warning.lineno, 0, f"{warning.warning_code}: {warning.message}", type(self)
