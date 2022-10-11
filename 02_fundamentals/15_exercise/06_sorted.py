""" Write a program that receives a sequence of numbers (integers)
separated by a single space. It should print a sorted list of numbers in ascending order.
Use sorted()."""


numbers = input().split()
list_numbers = []
for element in numbers:
    digit = int(element)
    list_numbers.append(digit)
print(sorted(list_numbers))
