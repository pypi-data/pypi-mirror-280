#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

install_requirements = open("requirements.txt").readlines()

setup(
    author="Thoughtful",
    author_email="support@thoughtful.ai",
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    description="Pre Commit hook for all Thoughtful checks.",
    long_description=readme,
    keywords="flake8_thoughtful",
    name="flake8_thoughtful",
    test_suite="tests",
    url="https://www.thoughtful.ai/",
    version="0.1.0",
    zip_safe=False,
    install_requires=install_requirements,
    packages=find_packages(),
    entry_points={"flake8.extension": ["THO = flake8_thoughtful:ThoughtfulHook"]},
)
