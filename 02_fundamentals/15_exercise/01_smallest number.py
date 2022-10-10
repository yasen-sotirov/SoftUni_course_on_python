""" Write a function that receives three integer numbers and returns the smallest.
Print the result on the console.
Use an appropriate name for the function."""


def smallest_num(numbers):
    return min(numbers)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
all_numbers = [num_1, num_2, num_3]

min_number = smallest_num(all_numbers)
print(min_number)
