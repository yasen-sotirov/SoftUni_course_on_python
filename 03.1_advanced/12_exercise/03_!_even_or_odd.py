""" Create a function called even_odd() that can receive a different
quantity of numbers and a command at the end. The command can be "even" or "odd".
 Filter the numbers depending on the command and return them in a list.
 Submit only the function in the judge system.
Submit only your function in the judge system.

Examples

Test Code
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

Output
[2, 4, 6]
[1, 3, 5, 7, 9]

"""


# def even_odd(*args):
#     command = args[-1]
#     parity = 0 if command == "even" else 1
#     return [el for el in args[0:len(args) - 1] if el % 2 == parity]


def even_odd(*args):
    *numbers, command = args
    parity = 0 if command == "even" else 1
    return [el for el in numbers if el % 2 == parity]   # паритет - равенство


# def even_odd(*args):
#     *numbers, command = args
#     if command == "even":
#         return [x for x in numbers if x % 2 == 0]
#     return [x for x in numbers if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
