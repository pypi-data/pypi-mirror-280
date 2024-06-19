"""Visitor to check for correct configuration calls to t_bug_catcher."""
import ast


class ConfigureCallVisitor(ast.NodeVisitor):
    """A visitor that checks for correct configuration calls to t_bug_catcher."""

    def __init__(self):
        """Initializes the ConfigureCallVisitor class."""
        self.imported_t_bug_catcher = False
        self.imported_configure = False
        self.imported_jira = False
        self.imported_bugsnag = False
        self.jira_called_base = False
        self.bugsnag_called_base = False
        self.jira_called_attr = False
        self.bugsnag_called_attr = False

    def visit_Import(self, node):
        """Visits import statements."""
        for alias in node.names:
            if alias.name == "t_bug_catcher":
                self.imported_t_bug_catcher = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        """Visits from import statements."""
        if node.module == "t_bug_catcher":
            for alias in node.names:
                if alias.name == "configure":
                    self.imported_configure = True
        elif node.module == "t_bug_catcher.configure":
            for alias in node.names:
                if alias.name == "jira":
                    self.imported_jira = True
                elif alias.name == "bugsnag":
                    self.imported_bugsnag = True
        self.generic_visit(node)

    def visit_Call(self, node):
        """Visits function calls."""
        if isinstance(node.func, ast.Name):
            if node.func.id == "jira":
                self.jira_called_base = True
            elif node.func.id == "bugsnag":
                self.bugsnag_called_base = True
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "jira":
                self.jira_called_attr = True
            elif node.func.attr == "bugsnag":
                self.bugsnag_called_attr = True
        self.generic_visit(node)

    def get_errors(self):
        """Returns a single error if the configuration calls are not correct."""
        if (
            (self.imported_t_bug_catcher or self.imported_configure)
            and (self.jira_called_attr and self.bugsnag_called_attr)
        ) or (self.imported_bugsnag and self.imported_jira and self.jira_called_base and self.bugsnag_called_base):
            return {}
        return {0: "Missing required configure calls for jira and bugsnag."}
