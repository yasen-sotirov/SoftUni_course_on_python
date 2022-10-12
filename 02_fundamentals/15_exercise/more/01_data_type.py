"""" Write a function that, depending on the first line of the input,
reads one of the following strings: "int", "real", or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5
and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.
"""


def data_type(command, line):
    result = 0
    if command == "int":
        result = int(line) * 2
    elif command == 'real':
        result = f'{int(line) * 1.5:.2f}'
    elif command == 'string':
        result = line.join('$$')
    return result


line_1, line_2 = input(), input()
print(data_type(line_1, line_2))
