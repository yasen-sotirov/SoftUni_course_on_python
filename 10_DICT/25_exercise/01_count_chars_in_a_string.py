"""" Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"
"""


current_input = input().split()
symbols = ''.join(current_input)
letters_dict = {}

for symbol in symbols:
    if symbol not in letters_dict.keys():
        letters_dict[symbol] = 0
    letters_dict[symbol] += 1

for char, occurrences in letters_dict.items():
    print(f"{char} -> {occurrences}")
