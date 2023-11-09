"""" A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False.
Print the result."""


# def palindrome(num_list):
#     list_of_numbers = num_list.split(', ')
#     for element in list_of_numbers:
#         straight_num = int(element)
#         backward_num = int(element[::-1])
#         if straight_num == backward_num:
#             result = True
#         else:
#             result = False
#         return result
#
#
# number_list = input()
# function_result = palindrome(number_list)
#
# print(function_result)


number_list = input().split(', ')
for element in number_list:
    straight_num = int(element)
    backward_num = int(element[::-1])
    if straight_num == backward_num:
        print(True)
    else:
        print(False)
