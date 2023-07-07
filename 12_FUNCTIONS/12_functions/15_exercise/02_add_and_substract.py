""" You will receive three integer numbers.
Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.
"""


def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_ot_two, num_3):
    return sum_ot_two - num_3


def add_and_subtract(num_1, num_2, num_3):
    sum_of_first_and_second = sum_numbers(num_1, num_2)
    result = subtract(sum_of_first_and_second, num_3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))