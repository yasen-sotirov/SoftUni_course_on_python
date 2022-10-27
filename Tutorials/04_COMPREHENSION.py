"""COMPREHENSION"""   # извадка


number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
number_list_2 = [4, 8, 2, 6, 9]


# print([el ** 2 for el in number_list if el % 2 == 0])
#
# print(["even" if el % 2 == 0 else "odd" for el in number_list])
#
# print([int(el) for el in input().split(', ')])

print([item for item in number_list if item in number_list_2])

