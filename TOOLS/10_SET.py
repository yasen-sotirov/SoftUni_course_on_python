"SET {} "       # IMmutable - НЕпроменлив, въпреки че може да добавяме нови елементи
            # само уникални елементи
            # не подрежда елементите!

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
set_3 = {3, 4}



"СЪЗДАВАНЕ SET"
# a = set()          # иначе се бърка с речник
# a = {}             # питона го мисли за дикшанъри


"ДОБАВЯ ЕЛЕМЕНТИ"
# print(set_1)
# set_1.add(12)
# print(set_1)


"ДОБАВЯ ЕЛЕМЕНТИ"
# print(set_1)
# set_1.add(12)
# print(set_1)


"ДЪЛЖИНАТА НА СЕТА"
# print(len(set_1))


"ПРЕМАХВА КОНКРЕТЕН ЕЛЕМЕНТИ - гърми ако ел го няма"
# print(set_1)
# set_1.remove(3)
# print(set_1)


"ПРЕМАХВА КОНКРЕТЕН ЕЛЕМЕНТИ - НЕ гърми ако ел го няма"
# print(set_1)
# set_1.discard(3)
# print(set_1)

# print(set_2)
# set_2.discard(1000)
# print(set_2)


"ПРЕМАХВА ПСОЛЕДНИЯ ЕЛЕМЕНТ" # !! АМА КОЙ ТОЧНО??
# print(set_1)
# set_1.pop()
# set_1.pop()
# print(set_1)


"ДАВА ЕЛЕМЕНТИТЕ, КОИТО ГИ НЯМА ВЪВ ВТОРИЯ СЕТ"     # Difference
# print(set_1)
# print(set_2)
# print(set_1 - set_2)
# print(set_2 - set_1)


"ДАВА ЕДНАКВИТЕ ЕЛЕМЕНТИ В ДВА СЕТА"        # Intersection
# print(set_1)
# print(set_2)
# print(set_1 & set_2)
# print(set_1.intersection(set_2))


"ДАВА ЕЛЕМЕНТИ, КОИТО СА УНИКАЛНИ ЗА ДВАТА СЕТА"     # Symmetric Difference
# print(set_1)
# print(set_2)
# print(set_1 ^ set_2)
# print(set_1.symmetric_difference(set_2))


"ОБЕДИНЯВА ДВА СЕТА"
# print(set_1)
# print(set_2)
# print(set_1 | set_2)
# print(set_1.union(set_2))


"ВСИЧКИ ЕЛЕМЕНТИ НА ЕДИНИ ИМА ЛИ ГИ В ДРУГИЯ"   # Subset
# print(set_2)
# print(set_3)
# print(set_2 > set_3)        # всички елементи на set_3 има ли ги в set_2
# print(set_3 > set_2)        # всички елементи на set_2 има ли ги в set_3
# print()
# print(set_1.issubset(set_2))        # set_1 <= set_2
# print(set_1.issuperset(set_2))      # set_1 >= set_2


"SET COMPREHENSION"
# nums = [1, 2, 3, 4, 5, 5, 6, 6, 2, 1]
# set_comprehension = {el for el in nums}
# print(set_comprehension)
# print(set(nums))            # или на кратко

"СОРТИРАНЕ - превръща в лист и сортира"
# set_1.add(-2)
# set_1.add(-12)
# set_1.add(-1)
# print(set_1)
# print(sorted(set_1))


"ГЕНЕРИРА SET C RANGE ОТ ЧИСЛА"
# print(set(range(1, 10 + 1)))


"НЕПРОМЕНЛИВ СЕТ"       # сет, който не можем да променяме
# a = frozenset([1, 2, 3, 3])
# print(a)
# print(type(a))
#
# a = {1, 2, 3}       # или сета го правим на тюпъл
# b = tuple(a)
