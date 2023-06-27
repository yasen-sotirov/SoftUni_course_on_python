"FUNCTIONS"  # лекция с Инес Иванова  https://softuni.bg/trainings/resources/video/61350/video-09-june-2021-ines-ivanova-python-fundamentals-may-2021/3368

# Параметъ = променливите, с които работи функцията
# Аргумент = променливите, които подаваме на функцията
# позиционни аргументи - ненаименовани аргументи
# позиционни аргументи - „param_1 = 25“   по четимо е

"ПОКАЗBА ДОКУМЕНТАЦИШТА ЗА ДАДЕНА ФУНКЦИШ"
# def example_func():
#     """This function just say Hello"""
#     return "Hello"
# print(example_func.__doc__)


"LAMBDA"        # анонимна функция (не я декларираме с def) - ползва се само на едно място в кода
                # синтаксис:    lambda променлива: израз

# lam_func = lambda a, b : a * b
# print(lam_func(5, 6))

# name_year = {"ABCC": 4, "CABB": 7, "ABB": 3, "BB": 5, "AB": 2, "AABBB": 1, "BBC": 6}
#
# askii = sorted(name_year, key=lambda x: x)
# print(f"нараства азбучно {askii}")
# print(f"ascending ???   {sorted(name_year, key=lambda x: x[0])}")
# print(f"ascending ???   {sorted(name_year, key=lambda x: x[1])}")
# print(f"нараства азбучно и по дължина {sorted(name_year, key=lambda x: len(x))}")
#
# num_list = []
# for el in askii:
#     char_sum = 0
#     for char in el:
#         char_sum += ord(char)
#     num_list.append(char_sum)
#
# print(num_list)

# print(f"ascending by name length {sorted(name_year, key=lambda x: len(x))}")


"БРОЙ ЕЛЕМЕНТИТЕ НА ФУНКЦИЯТА"
# def custom_reduce(func, elements):
#     argument_count = func.__code__.co_argcount
#     print(argument_count)
#
# print(custom_reduce(lambda a, b: a + b, [1, 2, 3]))


"CUSTOM REDUCE"
# from collections import deque
# def custom_reduce(func, elements):
#     elements = deque(elements)
#
#     argument_count = func.__code__.co_argcount
#     while len(elements) > 1:
#         argument = [elements.popleft() for _ in range(argument_count)]
#         elements.appendleft(func(*argument))
#     return elements[0]
# print(custom_reduce(lambda a, b: a + b, [1, 2, 3, 1, 2, 3]))


# List of Tuples Declaration
# planets = [("Earth", 3),("Jupiter",5),("Mercury",1), ("Mars",4), ("Neptune",8), ("Saturn", 6), ("Uranus",7), ("Venus",2)]
# print(planets)
#
# new_list = sorted(planets, key=lambda x: x[1], reverse=True)
# print("Sorted List: {new_list}")
# print("original List: ", planets)
#
# # Sorts the list by the item value of the second element of the Tuple
# SelectPlanets = sorted(planets, key = lambda x : x[1])
#
# print(SelectPlanets)





# list_1 = [4, 2, 13, 21, 5]
# final_list = []
#
# for i in list_1:
#     temp = lambda i: i ** 2
#     final_list.append(temp(i))
#
# print(final_list)
