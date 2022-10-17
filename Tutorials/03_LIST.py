"""LISTS"""     # съхранява различни типове данни на едно място
                # лист с методите  https://www.w3schools.com/python/python_ref_list.asp

mix_list = [1, 3, 2, "a", "b", 4, 88, 2, 2]
number_list = [1, 4, 3, 8, 6, 2, 7, 6.59, 2.32]
letters_list = ["cat", "dog", "mouse", "T", 'J']

"COMPREHENSION"
# result_list = []
# for el in number_list:
#     if el % 2 == 0:
#         result_list.append(el ** 2) # или .append(int(el))
# print(result_list)

# print([el ** 2 for el in number_list if el % 2 == 0])
# print(["even" if el % 2 == 0 else "odd" for el in number_list])

"ДОБАВЯ В ЛИСТА"
# new_var = 'new'
# letters_list.append(new_var)
# print(letters_list)

# mix_list.append(-int(2) * 2)
# print(mix_list)

"ДОБАВЯ МНОЖЕСТВО ЕЛЕМЕНТИ В ЛИСТА"       #или само един string
# number_list.extend(letters_list)
# print(number_list)

"ОБЕДИНЯВА ЛИСТА В STRING"
# print('-'.join(letters_list))      # винаги връща лист
# print(''.join(letters_list))       # при "" все едно конкатенираме текста
print('\n'.join(letters_list))       # печати всеки елемент на нов ред

"ПРОЧИТА ЛИСТА ОТ ИНДЕКС ДО ИНДЕКС СЪС СТЪПКА"      # като слайснг-а на стринг
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

"ПРЕМАХВА ЕЛЕМЕНТ/И В ЛИСТА (от ляво на дясно) "
# mix_list.remove(2)      # ако елемента го няма връща грешка
# print(mix_list)

# while 2 in mix_list:
#     mix_list.remove(2)
# print(mix_list)

"ТРИЕ ЕЛЕМЕНТ ПО ИНДЕКС"
# del mix_list[1]
# print(mix_list)

"СУМИРА ЛИСТА"
# print(sum(number_list))
# print("{:.2f}".format(sum(number_list)))

"РАЗДЕЛЯ ЧИСЛАТА В ЛИСТА"
# print(*number_list)             # „ * “ разопакова листа
# print(*number_list, sep="_")    # разопакова листа и слага сепаратор между елементите

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
# edit = mix_list.count('b')
# print(edit)

"ДАВА ИНДЕКС И ЕЛЕМЕНТА, КОЙТО Е ТАМ"
# for index, letter in enumerate(mix_list):
#     print(index, letter)

"КОПИРА ЛИСТА"
# second_list = mix_list.copy()
# print(second_list)

"ТЪРСЕНЕ В ЛИСТ"
# if 'a' in mix_list:
#     print('ok')

"ПОДРЕЖДА ПО АЗБУЧЕН РЕД"
# letters_list.sort()
# print(letters_list)

# number_list.sort()
# print(number_list)

# letters_list.sort(reverse=True) # обръщане на реда

# print(sorted(letters_list))     # или в принта
# print(sorted([5, 1, 6, 3, 8, 4, 2, 7]))

"ОБРЪЩА ЛИСТА ОТЗАНД НАПРЕД"
# mix_list.reverse()
# print(mix_list)

"ОБХОЖДА ЛИСТА ПО ЕЛЕМЕНТ И ПО ИНДЕКС"
# for element in mix_list:      # показва елементите в листа
#     print(element)

# for index in range(0, len(mix_list)):       # показва индексите на листа
#     print(index)

# for index in range(0, len(mix_list) - 2):     # извиква елемент по индекса му
#     print(mix_list[index], end=', ')

"ИЗПРАЗВА ЛИСТА"
# clear_list = mix_list.clear()
# print(clear_list)

"WHILE"
# while letters_list:
#     current_element = letters_list[0]
#     letters_list.remove(current_element)
#     print(letters_list)

