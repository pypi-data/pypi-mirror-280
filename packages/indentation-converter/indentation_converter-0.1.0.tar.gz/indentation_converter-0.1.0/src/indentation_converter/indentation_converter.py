import argparse
import os
import sys
from collections.abc import Callable
from typing import List

import binaryornot.check as bincheck
import pathspec


def convert_leading_spaces_to_tabs(line: str, spaces_per_tab: int) -> str:
    """
    Convert leading spaces in a line to tabs.

    :param line: The line to convert.
    :type line: str
    :param spaces_per_tab: The number of spaces per tab.
    :type spaces_per_tab: int
    :return: The line with leading spaces converted to tabs.
    :rtype: str
    """
    leading_spaces = len(line) - len(line.lstrip(" "))
    tabs = leading_spaces // spaces_per_tab
    remaining_spaces = leading_spaces % spaces_per_tab
    return "\t" * tabs + " " * remaining_spaces + line.lstrip(" ")


def convert_leading_tabs_to_spaces(line: str, spaces_per_tab: int) -> str:
    """
    Convert leading tabs in a line to spaces.

    :param line: The line to convert.
    :type line: str
    :param spaces_per_tab: The number of spaces per tab.
    :type spaces_per_tab: int
    :return: The line with leading spaces converted to tabs.
    :rtype: str
    """
    leading_tabs = len(line) - len(line.lstrip("\t"))
    spaces = " " * spaces_per_tab * leading_tabs
    return spaces + line.lstrip("\t")


def process_file(
    file_path: str, conversion_function: Callable[[str, int], str], spaces_per_tab: int
):
    """
    Process a single file to convert its leading spaces or tabs.

    :param file_path: The path of the file to process.
    :type file_path: str
    :param conversion_function: The function to use for conversion.
    :type conversion_function: Callable[[str, int], str]
    :param spaces_per_tab: The number of spaces per tab.
    :type spaces_per_tab: int
    """
    if is_binary(file_path):
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        for line in lines:
            file.write(conversion_function(line, spaces_per_tab))


def get_ignored_files(directory_path: str) -> List:
    """
    Get a list of files to ignore based on .gitignore patterns.

    :param directory_path: The directory to search for .gitignore.
    :type directory_path: str
    :return: A list of files to ignore.
    :rtype: List
    """
    gitignore_path = os.path.join(directory_path, ".gitignore")
    if not os.path.exists(gitignore_path):
        return []

    with open(gitignore_path, "r", encoding="utf-8", errors="ignore") as file:
        gitignore_patterns = file.read().splitlines()

    spec = pathspec.PathSpec.from_lines("gitwildmatch", gitignore_patterns)

    all_files = []
    for root, dirs, files in os.walk(directory_path):
        for name in files:
            all_files.append(os.path.relpath(os.path.join(root, name), directory_path))
        for name in dirs:
            all_files.append(os.path.relpath(os.path.join(root, name), directory_path))

    ignored_files = spec.match_files(all_files)
    return [os.path.join(directory_path, path) for path in ignored_files]


def is_hidden(filepath: str) -> bool:
    """
    Check if a file or directory is hidden.

    :param filepath: The path to the file or directory.
    :type filepath: str
    :return: True if the file or directory is hidden, False otherwise.
    :rtype: bool
    """
    name = os.path.basename(filepath)
    if name.startswith("."):
        return True
    elif os.name == "nt":  # Windows
        return has_hidden_attribute_on_windows(filepath)

    return False


def has_hidden_attribute_on_windows(filepath: str) -> bool:
    """
    Check if a file has the hidden attribute (Windows only).

    :param filepath: The path to the file.
    :type filepath: str
    :return: True if the file has the hidden attribute, False otherwise.
    :rtype: bool
    """
    import ctypes

    attrs = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
    return attrs != -1 and (attrs & 2) != 0


def is_binary(file_path: str) -> bool:
    """
    Check if a file is binary.

    :param file_path: The path to the file.
    :type file_path: str
    :return: True if the file is binary, False otherwise.
    :rtype: bool
    """
    return bincheck.is_binary(file_path)


def process_directory(
    directory_path: str,
    conversion_function: Callable[[str, int], str],
    spaces_per_tab: int,
):
    """
    Process all files in a directory to convert leading spaces or tabs.

    :param directory_path: The directory to process.
    :type directory_path: str
    :param conversion_function: The function to use for conversion.
    :type conversion_function: Callable[[str, int], str]
    :param spaces_per_tab: The number of spaces per tab.
    :type spaces_per_tab: int
    """
    ignored_files = get_ignored_files(directory_path)
    for root, dirs, files in os.walk(directory_path):
        files[:] = [f for f in files if not is_hidden(os.path.join(root, f))]
        dirs[:] = [d for d in dirs if not is_hidden(os.path.join(root, d))]

        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path not in ignored_files:
                process_file(file_path, conversion_function, spaces_per_tab)


def main():
    """
    Main function to handle argument parsing and conversion processing.
    """
    parser = argparse.ArgumentParser(
        description="Convert leading whitespace and tabs in files."
    )
    parser.add_argument("path", help="File or directory path to process")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["spaces-to-tabs", "st", "tabs-to-spaces", "ts"],
        help="Conversion mode. `st` is the short form of `spaces-to-tabs` and `ts` is "
        "the short form of `tabs-to-spaces`",
    )
    parser.add_argument(
        "-s",
        "--spaces-per-tab",
        type=int,
        default=4,
        help="Number of spaces per tab. The default value is 4.",
    )

    args = parser.parse_args()

    conversion_mode_map = {
        "spaces-to-tabs": "st",
        "tabs-to-spaces": "ts",
    }
    conversion_mode = conversion_mode_map.get(args.mode, args.mode)

    if conversion_mode == "st":
        conversion_function = convert_leading_spaces_to_tabs
    elif conversion_mode == "ts":
        conversion_function = convert_leading_tabs_to_spaces
    else:
        print("Invalid mode specified.")
        sys.exit(1)

    if os.path.isdir(args.path):
        process_directory(args.path, conversion_function, args.spaces_per_tab)
    elif os.path.isfile(args.path) and not is_hidden(args.path):
        process_file(args.path, conversion_function, args.spaces_per_tab)
    else:
        print(f"The path {args.path} is not valid.")
        sys.exit(1)

    if conversion_mode == "st":
        print(
            f"Leading spaces have been successfully converted to tabs in '{args.path}'"
        )
    else:
        print(
            f"Leading tabs have been successfully converted to spaces in '{args.path}'"
        )


if __name__ == "__main__":
    main()
