"""Unit tests for t_bug_catcher flake8 plugin."""
import pytest
from flake8_thoughtful import ThoughtfulHook
import os


@pytest.fixture
def THO001():
    """Code with config issues."""
    return """
import t_bug_catcher

try:
    pass
except Exception:
    t_bug_catcher.report_error()
"""


@pytest.fixture
def THO002():
    """Code with reporting issues."""
    return """
from t_bug_catcher.configure import jira, bugsnag

jira()
bugsnag()

try:
    pass
except Exception:
    print('error')
"""


def run_flake8_on_code(code):
    """Run flake8 on code and return the number of errors."""
    with open("task.py", "w") as temp_file:
        temp_file.write(code)
        temp_file.flush()

    hook = ThoughtfulHook(tree=None, filename="task.py")
    warnings = list(hook.run())
    codes = [warning[2].split(":")[0] for warning in warnings]
    os.remove("task.py")
    return codes


def test_THO001(THO001):
    """Check that the code without issues is not detected."""
    errors = run_flake8_on_code(THO001)
    assert "THO001" in errors


def test_THO002(THO002):
    """Check that the code without issues is not detected."""
    errors = run_flake8_on_code(THO002)
    assert "THO002" in errors
