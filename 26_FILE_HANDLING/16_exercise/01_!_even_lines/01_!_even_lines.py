""" 1.	Even Lines
Write a program that reads a text file and prints on the console
its even lines. Line numbers start from 0. Before you print the result,
replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

Examples
text.txt
output
"""

chars_to_replace = ['-', ',', '.', '!', '?']

with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = " ".join(reversed(line.strip().split()))
            for char in chars_to_replace:
                result = result.replace(char, "@")
            print(result)
