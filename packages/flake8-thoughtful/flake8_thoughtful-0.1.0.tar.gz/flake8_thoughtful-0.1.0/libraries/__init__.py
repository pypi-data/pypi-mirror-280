"""All Thoughtful warning checks."""

import logging

validation_logger = logging.getLogger("flake8_thoughtful")

validation_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s - %(name)s - %(message)s")
validation_logger.addHandler(console_handler)

from .base_warning import BaseWarning  # noqa
