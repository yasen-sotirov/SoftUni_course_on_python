"DICTIONARIES"      # values - mutable - променлив. може да се добавя променя ...
                    # keys - immutable - ключовете са уникални
                    # референтен тип данни
                    # скоростта на търсене в речник е О1

classes = {'1A': ["Ines", "Georgi", "Pesho"], '1B': ["Ivan", "Tosho", "Maria"]}   # един ключ може да садържа множество велюта
students = {'№1': {'name': 'Pesho', 'ages': 12}, '№2': {'name': 'Ivan', 'ages': 11}}
my_dict = {'a': 25, 'b': "Pesho", 2: 33}
num_dict = {'a': 1, 'b': 2, 'c': 3}
letter_dict = {'A': 4, 'C': 3, 'B': 1, 'D': 2}
names_ages = {"Ines": 27,
              "Georgi": 43,
              "Pesho": 40,
              "Marieta": 37,
              "Tosho": 46,
              "Maria": 52}      # така е по PEP стандарт


"ДОБАВЯНЕ В РЕЧНИКА"
# my_dict["eyes color"] = "green"
# print(my_dict)

# names = classes["1A"]             # дава ни достъп до вложения лист
# names.append("appended name")     # както обикновен лист
# print(classes)

# for key in classes:
#     classes[key].append("from the loop")
# print(classes)

# num_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in num_dict:
#     num_dict[key] *= 2
# print(num_dict)
# {'a': 2, 'b': 4, 'c': 6}

"ПРОМЯНА В РЕЧНИКА"
# my_dict["eyes color"] = "green"
# print(my_dict)
# my_dict["b"] = 30
# print(my_dict)

# names = classes["1A"]             # дава ни достъп до листа и вече работим с него
# names.append("appended name")     # както обикновен лист
# print(classes)

# for key in classes:
#     classes[key].append("from the loop")
# print(classes)



"ИЗВИКВАНЕ ПО ВЛОЖЕН РЕЧНИК"
# print(classes['1A'][1])
# print(students['№1']['name'])


"ИЗВИКВАНЕ НА VALUE ПО КЛЮЧ"
# print(my_dict["b"])       # вика ключ 2, тук индекси няма, не гарми ако индекса го няма
#
# print(my_dict.get(2))
# print(my_dict.get(3))


"ВРЪЩА СПИСЪК С VALUE"
# print(list(num_dict.values()))


"ВРЪЩА СПИСЪК СУМАТА НА VALUE"
# print(sum(num_dict.values()))


"ПРЕМАХВА K-V ДВОЙКА"
# print(my_dict)
# my_dict.pop("b")        # премахва по ключ
# print(my_dict)

# my_dict.popitem()       # премахва последната двойка
# print(my_dict)

# print(my_dict)
# del my_dict['a']
# print(my_dict)

# dictionary = my_dict
# del dictionary          # трие цялата променлива


"СОРТИРАНЕ"
# print(sorted(num_dict))         # принтва лист със сортирани само ключовете
#
# print(sorted(letter_dict.items(), key=lambda x: x[0]))   #за sorte с key, lambda прави for-цикъл за всяко „x“ от x[0]
# print(sorted(letter_dict.items(), key=lambda x: x[0], reverse=True))      # подрежда по value
# print(sorted(num_dict.items(), key=lambda x: - x[1]))                     # обръща реда на int

# print(names_ages)
# print(sorted(names_ages.items(), key=lambda x: (x[0], x[1])))     # сортира по два параметъра

# students_2 = {"A": [5, 6], "C": [2, 4], "B": [4, 3, 5]}
# print(sorted(students_2.items(), key=lambda kvpt: len(kvpt[1])))


"С ЛАМБДА"
# a = 4
# b = 3
# c = 2
# dict = {"*": lambda a, b, c: a + b - c}
# print(dict["*"](a, b, c))



"ВРЪЩА VALUE"       # a
# print(my_dict.pop("b"))   # връща value по ключ
# print(my_dict.popitem())    # връща последната двойка като тюпъл


"ИЗВИКВАНЕ VALUE ПО ИНДЕКС"
# names = classes['1A']
# print(names[0])
# print(names[0][0])
# print(type(names))


"ОБХОЖДАНЕ - ИТЕРИРАНЕ"
# print(classes)
# print(classes.keys())

# print(classes)
# print(classes.values())

# print(my_dict)
# print(my_dict.values())
# print(my_dict.items())      # връща tupple

# for key in my_dict:
    # print(key)

# for _ in my_dict.values():
#     print(_)

# for key, value in classes.items():
#     print(f"key is {key}, and value is {value}")

# for x in classes.items():
#     print(f"key is {x[0]}, and value is {x[1]}")


"DICT COMPREHENSION"
# print({value: key for key, value in names_ages.items() if value % 2 == 0})

# data = [("Peter", 22), ("Amy", 18), ("George", 35)]     # връща dict от тюпъли
# print({key: value for (key, value) in data})
# print(dict(data))

# num_list = [1, 2, 3, 4]
# print({num: num ** 3 for num in num_list})    # от лист връща dict със стойноста на 3та степен


# even_years = {}
# for key, value in names_ages.items():
#     if value % 2 == 0:
#         even_years[key] = value
# print(even_years)


"ПРЕВЪРЩА СПИСЪЦИ В РЕЧНИК"     #
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# print(dict(zip(values, keys)))

# my_dict = {}        # листовете трябва да са еднакво дълги
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


"ДАВА БРОЙКАТА НА KEY"
# print(len(my_dict))


"ТЪРСИ В РЕЧНИКА"
# print("a" in num_dict)      # търси в ключа
# print("f" in num_dict)
#
# print(3 in num_dict.values())   # търси в value


"ИЗПРАЗВАНЕ НА РЕЧНИКА"
# print(my_dict.clear())


"КОПИРА РЕЧНИКА"
# b = my_dict.copy()

"ВРЪЩА СПИСЪК С ТЮПЪЛИ"
# print(num_dict.items())


"ЗАМЕНЯ ЕЛЕМЕНТИ "
# def concatenate(*args, **kwargs):
#     main_string = ''.join(args)
#
#     for key, value in kwargs.items():
#         if key in main_string:
#             main_string = main_string.replace(key, value)
#     return main_string
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))



"ПРОВЕРЯВА ДАЛИ ТЪРСЕНИТЕ ЕЛЕМЕНТИ ГИ ИМА В КЛЮЧОВЕТЕ"
# gifts = {"Gemstone": 1, "Porcelain Sculpture": 1, "Gold": 1, "Diamond Jewellery": 1}
#
# if {"Gemstone", "Porcelain Sculpture"}.issubset(set(gifts.keys())) or \
#         {"Gold", "Diamond Jewellery"}.issubset(set(gifts.keys())):
#     print("The wedding presents are made!")



"ВРЪЩА КЛЮЧ ПО ОПРЕДЕЛЕН ДИАПАЗОН"
# score = int(input(f"give me the score between 100 and 499: "))
# gift_list = {
#     "Gemstone": lambda x: x if 100 <= x <= 199 else None,
#     "Porcelain Sculpture": lambda x: x if 200 <= x <= 299 else None,
#     "Gold": lambda x: x if 300 <= x <= 399 else None,
#     "Diamond Jewellery": lambda x: x if 400 <= x <= 499 else None
# }
# crafted_gifts = {}
#
# for key in gift_list:
#     if gift_list[key](score) is not None:
#         if key not in crafted_gifts:
#             crafted_gifts[key] = 0
#         crafted_gifts[key] += 1
# print(crafted_gifts)

