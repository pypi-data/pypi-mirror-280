"""
Utility functions for the pylint_runner module.
"""

import os
import re


def get_files_from_dir(current_dir, ignore_folders=None):
    """
    Recursively walk through a directory and get all python files and then
    walk through any potential directories that are found off current
    directory, so long as not within self.IGNORE_FOLDERS
    :return: all python files that were found off current_dir
    """
    if ignore_folders is None:
        ignore_folders = []

    if current_dir[-1] != "/" and current_dir != ".":
        current_dir += "/"

    files = []

    for dir_file in os.listdir(current_dir):
        if current_dir != ".":
            file_path = current_dir + dir_file
        else:
            file_path = dir_file

        if os.path.isfile(file_path):
            file_split = os.path.splitext(dir_file)
            if len(file_split) == 2 and file_split[0] != "" \
                    and file_split[1] == ".py":
                files.append(file_path)
        elif (os.path.isdir(dir_file) or os.path.isdir(file_path)) \
                and dir_file not in ignore_folders:
            path = dir_file + os.path.sep
            if current_dir not in ["", "."]:
                path = os.path.join(current_dir.rstrip(os.path.sep), path)
            files += get_files_from_dir(path)
    return files


def get_pylint_kwargs(pylint_version):
    """ Get the correct keyword arguments for the pylint runner. """
    pylint_version = pylint_version.split('.')[:3]
    pylint_version[2] = re.sub(r'[a-z-].*', '', pylint_version[2])
    pylint_version = [int(x) for x in pylint_version]
    if pylint_version < [2, 5, 1]:
        return {"do_exit": False}
    return {"exit": False}
