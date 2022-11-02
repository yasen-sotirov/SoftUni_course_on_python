"NUMBERS"    # from math import ceil, floor

num_1, num_2, num_3 = 1, 2, 3

"НАЙ-МАЛКО, НАЙ-ГОЛЯМО"
# print(min(num_1, num_2, num_3))
# print(max(num_1, num_2, num_3))

"ФОРМАТИРА СТОЙНОСТТА НА ПРОМЕНЛИВА"
# num_as_float = num_3 / num_2
# print("{:.3f}".format(num_as_float))

"СЛАГА ЗАПЕТАЯ МЕЖДУ НУЛИТЕ НА ГОЛЕМИ ЧИСЛА"
# num = 1000000
# print(f"{num:,}")

"ЗАКРЪГЛЯ"
num = 3.1415926
print(f'{num:+.2f}')
print(round(num, 1))


"СЛАГА НУЛИ ПРЕД ЧИСЛОТО"
# num = 4
# print(f"{num:03d}")

"ПРЕОБРАЗУВА В ПРОЦЕНТИ"
# num = 0.35
# print(f"{num:.2%}")

"МАП"
# def double_num(number):
#     if number % 2 == 0:
#         return number * 2
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# result = map(double_num, num_list)
# print(list(result))

