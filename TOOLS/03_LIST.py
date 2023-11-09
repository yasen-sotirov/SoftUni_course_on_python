"LISTS"         # съхранява различни типове данни на едно място
                # референтен тип данни:  names = [1, 2, 3]  asd = names - едно и също са
                # лист с методите  https://www.w3schools.com/python/python_ref_list.asp
                # mutable - променлив

mix_list = [1, 3, 2, "a", "b", 4, 88, 2, 2]
number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
number_list_2 = [10, 20, 30, 40, 50, 60]
number_list_3 = [1, 2, 3, 4, 5]
letters_list = ["cat", "dog", "mouse", "hello", 'world']
nested_list = [[1, 2, 3], [4, 5, 6]]

"ДОБАВЯ НОВИ ЕЛЕМЕНТИ В ЛИСТА"
# print(mix_list)
# mix_list.append("new_var")
# mix_list.append(-int(2) * 2)
# print(mix_list)


"ДОБАВЯ КЪМ СЪЩ ЕЛЕМЕНТИ В ЛИСТА"
# print(number_list)
# number_list[0] += 100
# print(number_list)

# print(letters_list)
# letters_list[0] += '_MO'
# print(letters_list)


"ЗАМЕНЯ СЪЩ ЕЛЕМЕНТИ В ЛИСТА"
# print(letters_list)
# letters_list[0] = "TOM"
# print(letters_list)


"ОБЕДИНЯВА ДВА ЛИСТА"       #или само един string
# print(number_list)
# number_list.extend(letters_list)
# print(number_list)
#
# print(number_list + letters_list)


"ОБЕДИНЯВА ЛИСТА В STRING"            # само за str;  *number_list за int
# print('-'.join(letters_list))       # винаги връща лист
# print(' '.join(letters_list))       # при "" все едно конкатенираме текста
# print('\n'.join(letters_list))      # печати всеки елемент на нов ред

# print(", ".join([str(x) for x in number_list]))     # ако са числа


"РАЗОПАКОВА ЛИСТА"      # вместо " ".join(), защото той работи само с str
# print(number_list)
# print(*number_list)
# print(*number_list, sep=", ")

# commands = "bg:sofia:varna:burgas"
# commands, *data = commands.split(":")
# print(commands)
# print(data)


"sliceing - ПРОЧИТА ЛИСТА ОТ ИНДЕКС ДО ИНДЕКС СЪС СТЪПКА"      # като слайснг-а на стринг
# edited = mix_list[2:5:2]
# print(edited)
# print(mix_list[4])
# print(mix_list[-2])
# print(mix_list[::-1])   # чете листа на обратно


"НАЙ-МАЛКО И НАЙ-ГОЛЯМО ЧИСЛО"
# print(min(number_list))
# print(max(number_list))


"РАЗМЕСТВАНЕ В ЛИСТА"
# letters_list[1], letters_list[0] = letters_list[0], letters_list[1]     # swapping
# print(letters_list)


"ТРИЕ / ВАДИ ПО ИНДЕКС (или последния) СИМВОЛ ОТ ЛИСТА"
# char = mix_list.pop(-3)
# print(mix_list)
# print(char)


"ИЗВЕЖДА ЕЛЕМЕНТ ОТ ЛИСТА"      # броя на променливите трябва да отговаря на дължината на листа
# num_1, num_2, num_3, num_4, num_5 = number_list_3
# print(num_1)
# print(num_5)


"ПРЕМАХВА ЕЛЕМЕНТ/И В ЛИСТА (от ляво на дясно) "
# print(mix_list)
# mix_list.remove(2)      # ако елемента го няма връща грешка
# print(mix_list)

# while "dog" in letters_list:
#     letters_list.remove("dog")
# print(letters_list)


"ТРИЕ ЕЛЕМЕНТ ПО ИНДЕКС"
# print(mix_list)
# del mix_list[1]
# print(mix_list)


"СУМИРА ЛИСТА"
# print(sum(number_list))
# print("{:.2f}".format(sum(number_list)))



"ВМЪКВА (нещо) ПО ИНДЕКС"
# mix_list.insert(3, "Pesho")
# print(mix_list)


"ПЪЛНЕНЕ НА ЛИСТ"
# number_of_wagon = int(input())
# train = [0] * number_of_wagon
# print(train)


"НА КОЙ ИНДЕКС СЕ НАМИРА (нещо)"
# number = mix_list.index('b')
# print(number)


"БРОЙ КОЛКО (неща) ИМА В ЛИСТА"
# print(letters_list.count('o'))
# print(mix_list.count("b"))


"ДАВА ИНДЕКС И ЕЛЕМЕНТА, КОЙТО Е ТАМ"
# for index, letter in enumerate(mix_list):
#     print(index, letter)



"КОПИРА ЛИСТА"          # и работим върху копието, оригинала се запазва
# second_list = mix_list.copy()
# second_list.append(1000)
# print(mix_list)
# print(f'second list: {second_list}')


"С КАКВО ЗАПОЧВА"
# print(list([item for item in letters_list if item.startswith("d")]))


"ТЪРСЕНЕ В ЛИСТ"
# if 'a' in mix_list:
#     print('ok')


"СОРТИРА СЪЩ. ЛИСТ"
# letters_list.sort()
# print(letters_list)

# number_list.sort()
# print(number_list)

# letters_list.sort(reverse=True) # обръщане на реда


"ПРАВИ НОВ ЛИСТ И СОРТИРА НЕГО"
# print(letters_list)
# print(sorted(letters_list))

# name_list = ["Ali", 'Marry', 'Kim', 'Teddy', 'Monika', 'John']
# sorted_list = sorted(name_list, key=lambda item: (-len(item), item))
# print(sorted_list)


"ОБРЪЩА ЛИСТА ОТЗАНД НАПРЕД"
# mix_list.reverse()
# print(mix_list)


"ПРОМЕНЯ ЕЛЕМЕНТИ ВЪВ ВЛОЖЕНИЯ СПИСЪК"
# print(nested_list)
# nested_list[0][1] = 222
# print(nested_list)


"КОПИРАНЕ НА ВЛОЖЕН СПИСЪК"
# from copy import deepcopy
# nested_list_2 = deepcopy(nested_list)



"ОБХОЖДА ЛИСТА ПО ЕЛЕМЕНТ И ПО ИНДЕКС - итерира"
# for element in mix_list:      # показва елементите в листа
#     print(element)

# for index in range(0, len(mix_list)):       # показва индексите на листа
#     print(index)

# for index in range(0, len(mix_list) - 2):     # извиква елемент по индекса му
#     print(mix_list[index], end=', ')


"ПРЕМАХВА ПОВТАРЯЩИТЕ СЕ ЕЛЕМЕНТИ ОТ ЛИСТА - SET"   # разбърква елементите
# print(list(set(mix_list)))


"СРЕДНА СТОЙНОСТ"
# from statistics import mean
# print(f"средна стойност на листа {mean(number_list):.2f}")


"ФИЛТЪР - елементите, който дават True"
# def only_vowel(variable):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	return variable in letters
# sequence = ['a', 'g', 'e', 'e', 'j', 'u', 'k', 's', 'o', 'p', 'r', 'a']
# print(list(filter(only_vowel, sequence)))

# print(list(filter(lambda x: x % 2 == 0, number_list)))

# print(list(filter(lambda x: len(x) >= 4, letters_list)))


"MAP - работи с итерируеми обекти"
# print(list(map(len, letters_list)))

# def cubed_num(digit):
#     return digit ** 2
# print(list(map(cubed_num, number_list)))

# print(list(map(lambda num: num ** 2, number_list)))

# print(list(map(lambda x, y: x*y, number_list_2, number_list_3)))

# print(list(map(str.upper, letters_list)))

# print(list(map(float, number_list)))

# measurement = [
#     {'length': 2.5, 'width': 2},
#     {'length': 3, 'width': 6},
#     {'length': 5, 'width': 4},
# ]
# print(list(map(lambda x: x.get('length', 0) * x.get('width', 0), measurement)))

"ИЗПРАЗВА ЛИСТА"
# clear_list = mix_list.clear()
# print(clear_list)


"WHILE"
# while letters_list:
#     current_element = letters_list[0]
#     letters_list.remove(current_element)
#     print(letters_list)


"ОБРЪЩА ЛИСТА"                      # или слайсинг result = letters_list[::-1]
# print(letters_list)
# print(list(reversed(letters_list)))     # прави нова колекция, която е обърната
#
#
# letters_list.reverse()      # метод, който обръща оригиналната колекция
# print(letters_list)


"BOOLEAN IN"            # ако го има в листа връща True
# boolean = 5 in number_list_3
# print(boolean)
# print(6 in number_list_3)


"ГЕНЕРИРА ЛИСТ C RANGE ОТ ЧИСЛА"
# print(list(range(1, 10 + 1)))


"ЕДНАКВИ ЛИ СА"              # връща дали всичк в итеръбъла са еднакви
print(all(number_list_2))
# print(all([isinstance(x, int) for x in number_list_2]))
# print(all([isinstance(x, str) for x in letters_list]))
# print(all([isinstance(x, str) for x in mix_list]))
#

