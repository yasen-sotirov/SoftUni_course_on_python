"LISTS"     # съхранява различни типове данни на едно място

mix_list = [1, 3, 2, "a", "b", 4, 2, 2]
number_list = [1, 5, 3, 8, 4, 2, 7, 6, 2]
letters_list = ["k", "a", "c", "m"]

"ДОБАВЯ В ЛИСТА"
# new_var ='new'
# letters_list.append(new_var)
# print(letters_list)

"ПОДРЕЖДА ПО АЗБУЧЕН РЕД"
# letters_list.sort()
# print(letters_list)

# number_list.sort()
# print(number_list)

# letters_list.sort(reverse=True) # обръщане на реда

# print(sorted(letters_list))     # или в принта
# print(sorted([5, 1, 6, 3, 8, 4, 2, 7]))

"ПРОЧИТА ЛИСТА НАОБРАТНО"
# mix_list.reverse()
# print(mix_list)

"ПРОЧИТА ЛИСТА ОТ ИНДЕКС ДО ИНДЕКС СЪС СТЪПКА"
# edited = mix_list[2:5:2]
# print(edited)

"ПРОЧИТА ЛИСТА НАОБРАТНО"
# edited = mix_list[::-1]
# print(edited)

"ВАДИ ПОСЛЕДНИЯ (или по индекс) СИМВОЛ ОТ ЛИСТА"
# char = mix_list.pop()
# print(mix_list)
# print(char)

"ПРЕМАХВА ПЪРВОТО СЪВПАДЕНИЕ В ЛИСТА"
# mix_list.remove(2)
# print(mix_list)

"ТРИЕ ЕЛЕМЕНТ ПО ИНДЕКС"
# del mix_list[0]
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
if 'a' in mix_list:
    print('ok')