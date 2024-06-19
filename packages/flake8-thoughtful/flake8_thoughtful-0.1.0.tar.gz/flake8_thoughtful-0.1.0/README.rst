Flake9 Thoughtful Hook
======================

Description
-----------
A pre-commit hook that runs Thoughtful pre-commit checks for common errors in the codebase. It is built as a flake8 plugin to ensure code quality and consistency.

Documentation
-------------
For more detailed information, refer to the `T Bug Catcher Documentation <https://www.notion.so/thoughtfulautomation/T-Bug-Catcher-Hook-fb96897875ce4a0fa689911aea35af3d?pm=c>`_.

Automations
-----------
The following automations are integrated with the Flake8 Thoughtful Hook:
- **flake8**: Used for linting and enforcing coding standards.

Preflight
---------
To configure the Flake8 Thoughtful Hook, follow these steps:

1. Add the Flake8 Thoughtful Hook to the ``additional_dependencies`` in the ``flake8`` hook section of your ``pre-commit-config.yaml`` file.

File Descriptions
-----------------
The following table describes the purpose of each file included in the project:

.. list-table:: 
   :header-rows: 1

   * - File
     - Purpose
   * - `flake8_thoughtful.py`
     - The main plugin file providing the entry point for flake8.
   * - `.pre-commit-config.yaml`
     - Configuration file that defines the checks performed during pre-commit.
   * - `bitbucket-pipelines.yaml`
     - Configuration file for Bitbucket pipelines; runs pre-commit checks and handles deployment to PyPI.
   * - `setup.py`
     - Contains the package metadata and dependencies for the T Bug Catcher Hook.
   * - `README.md`
     - The documentation file for the plugin, providing usage instructions and other relevant information.
