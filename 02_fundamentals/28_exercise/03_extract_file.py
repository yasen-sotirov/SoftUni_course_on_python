"""" Write a program that reads the path to a file and subtracts the file name and its extension."""


file_path = input().split('\\')
file, extension = file_path[-1].split('.')
print(f"File name: {file}")
print(f"File extension: {extension}")
