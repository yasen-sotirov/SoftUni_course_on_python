""" 4.	Directory Traversal
Write a program that traverses a given directory for all files.
Search through the first level of the directory only and write information
about each found file in report.txt. The files should be grouped by their extension.
Extensions should be ordered by name alphabetically. The files with extensions
should also be sorted by name. report.txt should be saved on the Desktop.
Ensure the desktop path is always valid, regardless of the user.
"""

from os import listdir, path


def traverse_dir(current_path):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element))
        else:
            print("file: ", element)



traverse_dir('.')
