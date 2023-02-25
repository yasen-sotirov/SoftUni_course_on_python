""" Write a program that receives a single string
containing positive and negative numbers separated by a single space.
Print a list containing the opposite of each number."""

list_of_number = input().split()
list_opposite_num = []

for element in list_of_number:
    current_num = - int(element)
    list_opposite_num.append(current_num)

print(list_opposite_num)
