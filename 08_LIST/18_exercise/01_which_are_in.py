""" You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line."""


first_line = input().split(", ")
second_line = input().split(', ')
new_list = []

for first_word in first_line:
    for second_word in second_line:
        if first_word in second_word:
            new_list.append(first_word)
            break

print(new_list)