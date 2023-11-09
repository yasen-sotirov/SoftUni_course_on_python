"""" Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print the min and max values of the given numbers and the sum of all the numbers
 in the list. Use min(), max() and sum().
The output should be as follows:
•	On the first line: "The minimum number is {minimum number}"
•	On the second line: The maximum number is {maximum number}"
•	On the third line: "The sum number is: {sum of all numbers}"
"""


def min_max_sum(number):
    list_of_numbers = []

    for element in number:
        digit = int(element)
        list_of_numbers.append(digit)
    return list_of_numbers


number_list = input().split()

print(f"The minimum number is {min(min_max_sum(number_list))}")
print(f"The maximum number is {max(min_max_sum(number_list))}")
print(f"The sum number is: {sum(min_max_sum(number_list))}")
