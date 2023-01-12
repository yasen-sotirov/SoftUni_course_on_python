"""
Write a function that receives two characters and returns a single string
with all the characters in between them (according to the ASCII code), separated by a single space.
Print the result on the console.
"""


# def char_in_range(first, second):
#     char_list = []
#     for current_char_as_num in range(ord(first) + 1, ord(second)):
#         char_list.append(chr(current_char_as_num))
#     return char_list
#
#
# first_char = input()
# second_char = input()
# result = char_in_range(first_char, second_char)
# print(' '.join(result))


def chr_in_between_function(char_1, char_2):
    char_list = []
    for current_char in range(ord(char_1) + 1, ord(char_2)):
        char_list.append(chr(current_char))
    return char_list


def input_functions():
    first_char = input('first char: ')
    second_char = input('second char: ')
    return first_char, second_char


start_char, end_char = input_functions()
result = chr_in_between_function(start_char, end_char)
print(', '.join(result))
