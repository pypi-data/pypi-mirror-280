"""Visitor to check for incorrectly handled try-except blocks."""

import ast


class IncorrectTryBlockVisitor(ast.NodeVisitor):
    """A visitor that checks for incorrect try-except blocks."""

    def __init__(self):
        """Initializes the IncorrectTryBlockVisitor class."""
        self.errors = {}

    def visit_Try(self, node):
        """Visits the try-except block in the AST."""
        message = (
            "Error not handled: specify the error type or re-raise exception or "
            "report it with `t_bug_catcher.report_error()`"
        )
        for handler in node.handlers:
            if isinstance(handler.type, ast.Name) and handler.type.id == "Exception":
                if not self._contains_raise(handler.body) and not self._contains_correct_error_handling(handler.body):
                    self.errors[handler.lineno] = message
            elif handler.type is None:  # 'except:' that catches everything
                if not any(isinstance(x, ast.Raise) for x in handler.body):
                    self.errors[handler.lineno] = message
        self.generic_visit(node)

    @staticmethod
    def _contains_correct_error_handling(statements):
        for stmt in statements:
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                func = stmt.value.func
                if (isinstance(func, ast.Name) and func.id == "report_error") or (
                    isinstance(func, ast.Attribute) and func.attr == "report_error"
                ):
                    return True
        return False

    @staticmethod
    def _contains_raise(statements):
        return any(isinstance(stmt, ast.Raise) for stmt in statements)

    def get_errors(self):
        """Returns the errors found in the try-except blocks."""
        return self.errors
