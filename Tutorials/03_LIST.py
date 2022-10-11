"""LISTS"""     # съхранява различни типове данни на едно място
                # лист с методите  https://www.w3schools.com/python/python_ref_list.asp

mix_list = [1, 3, 2, "a", "b", 4, 88, 2, 2]
number_list = [1, 5, 3, 8, 4, 2, 7, 6.5, 2.3]
letters_list = ["cat", "dog", "mouse", "T", 'J']

"ДОБАВЯ В ЛИСТА"
# new_var ='new'
# letters_list.append(new_var)
# print(letters_list)

# mix_list.append(-int(2) * 2)
# print(mix_list)

"ОБЕДИНЯВА ЛИСТА В STRING"
# string = '-'.join(letters_list)       # при "" все едно конкатенираме текста
# print(string)
# print(type(string))

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

"СУМИРА ЛИСТА"
# print(sum(number_list))
z = (sum(number_list))
y = ("{:.2f}".format(z))
print(y)

"ПРЕМАХВА ПЪРВИЯТ ЕЛЕМЕНТ В ЛИСТА (от ляво на дясно) "
# mix_list.remove(2)
# print(mix_list)

"ТРИЕ ЕЛЕМЕНТ ПО ИНДЕКС"
# del mix_list[1]
# print(mix_list)

"ВМЪКВА (нещо) ПО ИНДЕКС"
# mix_list.insert(3, "Pesho")
# print(mix_list)

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

"ОБХОЖДА ЛИСТА"
# по елемент
# for element in mix_list:      # показва елементите в листа
#     print(element)

# по индекси
# for index in range(0, len(mix_list)):       # показва индексите на листа
#     print(index)

# извиква елемент по индекса му
# for index in range(0, len(mix_list) - 2):
#     print(mix_list[index], end=', ')

"WHILE"
# while letters_list:
#     current_element = letters_list[0]
#     letters_list.remove(current_element)
#     print(letters_list)

