""" 1.	Flatten Lists
Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix sub-lists and
their values from left to right as shown below

    Examples
    Input
1 2 3 |4 5 6 |  7  88
    Output
7 88 4 5 6 1 2 3
"""

line = input().split("|")
result = []

while line:
    sublist = line.pop().split()
    for el in sublist:
        result.append(el)

print(*result, sep=" ")