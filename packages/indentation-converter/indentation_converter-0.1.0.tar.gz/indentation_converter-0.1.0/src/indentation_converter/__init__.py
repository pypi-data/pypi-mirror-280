"""
Indentation Converter Package

A Python package for converting indentation styles between spaces and tabs in text files and directories.

Features:
- Convert leading spaces to tabs
- Convert leading tabs to spaces
- Customize tab width and spaces per tab
- Respect .gitignore exclusions

Usage:
1. Import and use functions:
   - convert_leading_spaces_to_tabs
   - convert_leading_tabs_to_spaces
   - process_file

2. Supports both individual files and directories.

"""

# Copyright (c) 2024 mobile-strings-converter
# @license: http://www.opensource.org/licenses/mit-license.php

from .indentation_converter import (
    convert_leading_spaces_to_tabs,
    convert_leading_tabs_to_spaces,
    get_ignored_files,
    has_hidden_attribute_on_windows,
    is_binary,
    is_hidden,
    process_directory,
    process_file,
)

__all__ = [
    "convert_leading_spaces_to_tabs",
    "convert_leading_tabs_to_spaces",
    "process_file",
    "get_ignored_files",
    "is_hidden",
    "has_hidden_attribute_on_windows",
    "is_binary",
    "process_directory",
]

__version__ = "0.1.0"
__author__ = "José Carlos López Henestrosa"
__license = "MIT"
__author_email__ = "henestrosadev@gmail.com"
__maintainer_email__ = "henestrosadev@gmail.com"
