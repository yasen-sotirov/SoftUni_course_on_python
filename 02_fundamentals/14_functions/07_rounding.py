"""" Write a program that rounds all the given numbers,
separated by a single space, and prints the result as a list.
Use round()."""


def rounding_num(num):
    return round(num,)


line_of_numbers = input().split()
number_list = []

for current_num in line_of_numbers:
    edited_num = rounding_num(float(current_num))
    number_list.append(edited_num)

print(number_list)