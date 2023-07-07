"""" Write a program that reads usernames on a single line (separated by ", ")
and prints all valid usernames on separate lines.
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between
"""


def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_is_valid(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def username_validation(name):
    if length_is_valid(name) and characters_is_valid(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)
