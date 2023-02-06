""" 4.	File Delete
Create a program that deletes the file you created in the previous task.
If you try to delete the file multiple times, print the message:
'File already deleted!'.
"""

import os

if os.path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")
else:
    print('File already deleted!')


# вариант 2
# try:
#     os.remove("my_first_file.txt")
# except FileNotFoundError:
#     print("File already deleted!")