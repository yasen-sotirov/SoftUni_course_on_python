"""
Write a function that receives two characters and returns a single string
with all the characters in between them (according to the ASCII code), separated by a single space.
Print the result on the console.
"""


def char_in_range(first, second):
    char_list = []
    for current_char_as_num in range(ord(first) + 1, ord(second)):
        char_list.append(chr(current_char_as_num))
    return char_list


first_char = input()
second_char = input()
result = char_in_range(first_char, second_char)
print(' '.join(result))
