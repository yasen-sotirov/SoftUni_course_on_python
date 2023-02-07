""" 4.	Directory Traversal
Write a program that traverses a given directory for all files.
Search through the first level of the directory only and write information
about each found file in report.txt. The files should be grouped by their extension.
Extensions should be ordered by name alphabetically. The files with extensions
should also be sorted by name. report.txt should be saved on the Desktop.
Ensure the desktop path is always valid, regardless of the user.
"""

from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element), files_by_ext)
        else:
            extension = element.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_ext = {}
traverse_dir('.', files_by_ext)

for ext, files in sorted(files_by_ext.items()):
    print(f".{ext}")
    for file in sorted(files):
        print(f"--- {file}")
