"DICTIONARIES"      # values - mutable - променлив. може да се добавя променя ...
                    # keys - immutable
                    # референтен тип данни

classes = {'1A': ["Ines", "Georgi", "Pesho"], '1B': [1, 2, 3, 4]}   # един ключ може да садържа множество велюта
my_dict = {'a': 25, 'b': "Pesho", 2: 33}
num_dict = {'a': 1, 'b': 2, 'c': 3}



"ИЗВИКВАНЕ НА КЛЮЧ"
# print(my_dict["b"])       # вика ключ 2, тук индекси няма, гарми ако индекса го няма
#
# print(my_dict.get(2))
# print(my_dict.get(3))


"ДОБАВЯНЕ и ПРОМЯНА В РЕЧНИКА"
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

# for key in num_dict:
#     num_dict[key] *= 2
# print(num_dict)


"ИЗВИКВАНЕ ПО ИНДЕКС ОТ VALUE"
# names = classes['1A']
# print(names[0])
# print(names[0][0])
# print(type(names))


"ОБХОЖДАНЕ - ИТЕРИРАНЕ"
# print(classes.keys())
# print(classes.values())
# print(my_dict.values())
# print(my_dict.items())      # връща tupple

# for key in my_dict:
    # print(key)

# for _ in my_dict.values():
#     print(_)
# for key, value in classes.items():
#     print(key)
#     print(value)


"ПРЕВЪРЩА СПИСЪЦИ В РЕЧНИК"     #
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# print(dict(zip(values, keys)))

# my_dict = {}        # листовете трябва да са еднакво дълги
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


"ТЪРСИ В РЕЧНИКА"
print("a" in num_dict)      # търси в ключа
print("f" in num_dict)

print(3 in num_dict.values())   # търси в value

