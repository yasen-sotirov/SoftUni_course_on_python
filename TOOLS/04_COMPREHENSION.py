"""COMPREHENSION"""   # извадка


number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
number_list_2 = [4, 8, 2, 6, 9]


# print([el ** 2 for el in number_list if el % 2 == 0])
#
# print(["even" if el % 2 == 0 else "odd" for el in number_list])



"ОБХОЖДА ЛИСТА И ПРЕВРЪЩА ЕЛЕМЕНТИТЕ"
# print(number_list)
# print([str(el) for el in number_list])


"ОБХОЖДА ЛИСТА И СРАВНЯВА ДАЛИ ГИ ИМА В ДРУГИЯ ЛИСТ"
# print([item for item in number_list if item in number_list_2])


"ДАВА СТОЙНОСТИ НА ПРОМЕНЛИВИТЕ ОТ ЛИСТ"
# command = ["Sofia", "2", "10"]
# num_1, num_2 = [int(x) for x in command if x.isdigit()]
# print(f"{num_1}, {num_2}")
# print(num_1, num_2)

# data = ["5", "Sofia"]
# digit, string = [int(x) if x.isdigit() else x for x in data]
# print(digit, string)