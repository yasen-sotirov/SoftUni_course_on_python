"""" Write a program that receives a list of integer numbers (separated by a single space)
and a number n. The number n represents the count of numbers to remove from the list.
You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
 separated by a comma and a space ", ". """


list_of_numbers = input().split()
number = int(input())
edited_list = []
list_as_str = ''

for current_num in list_of_numbers:
    num_as_digit = int(current_num)
    edited_list.append(num_as_digit)

for _ in range(number):
    edited_list.remove(min(edited_list))

for element in edited_list:
    new_element = str(element)
    list_as_str += new_element

list_as_str = list_as_str[-1]

print(list_as_str)
