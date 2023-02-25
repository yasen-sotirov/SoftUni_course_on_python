"""" Using a list comprehension, write a program that receives numbers,
separated by comma and space ", ", and prints all the positive, negative, even,
and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
"""


def positive_num(some_nums):
    return [number for number in some_nums if int(number) >= 0]


def negative_num(some_nums):
    return [number for number in some_nums if int(number) < 0]


def even_num(some_nums):
    return [number for number in some_nums if int(number) % 2 == 0]


def odd_num(some_nums):
    return [number for number in some_nums if not int(number) % 2 == 0]


numbers = input().split(', ')
print(f"Positive: {', '.join(positive_num(numbers))}")
print(f"Negative: {', '.join(negative_num(numbers))}")
print(f"Even: {', '.join(even_num(numbers))}")
print(f"Odd: {', '.join(odd_num(numbers))}")
