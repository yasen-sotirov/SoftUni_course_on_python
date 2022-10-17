"""STRING"""    # колекция, низ от символи, които могат да бъдат обходени


txt = "- I like bananas !!"
txt_2 = 'Very much!'
txt_3 = "123456"
txt_4 = "1 2 3 4 5 6"

"ПРЕВРЪЩА STR В ЛИСТ ОТ ЧИСЛА"
nums = [int(el) for el in input().split(', ')]

"РАЗДРОБЯВА СТРИНГ НА ЕЛЕМЕНТИ"
# print(txt.split())        # винаги връща лист

"ОТ STR ПРАВИ ЛИСТ ОТ ЧИСЛА"
# list_of_ints = [int(x) for x in txt_3]
# print(list_of_ints)

# list_of_strings = txt_4.split(' ')
# print(list(map(int, list_of_strings)))

"ЗАМЕНЯ ЕЛЕМЕНТ"
print(txt.replace("bananas", "apples"))

"ПРЕМАХВА ЕЛЕМЕНТ ОТ НАЧАЛОТО И КРАЯ НА ТЕКСТА"
print(txt.strip("-!"))

"ДОБАВЯ ЕЛЕМЕНТ ОТ НАЧАЛОТО И КРАЯ НА ТЕКСТА"
print(txt.join('!@'))

"БРОЙ ЕЛЕМЕНТИ В СТРИНГА"
# print(txt.count('n'))

"ASCII ТАБЛИЦА"
# print(f'Кодът на буквата е: {ord("A")}')
# print(f'Буквата е: {chr(100)}')

"СЛАЙСИНГ"              # работи и за лист
# print(txt[2])           # показва кой символ е на индекс
# print(txt[1:9:2])       # показва символи от индекс до индекс със стъпка

"ГЛАВНИ и МАЛКИ БУКВИ"
# print(txt.lower())
# print(txt.upper())

# print(txt.islower())
# print(txt.isupper())

"ЧИСЛА ЛИ СА"
# print(txt_3.isalnum())
# print(txt_3.isdigit())

"ПОСТАВЯ СЕПАРАТОР МЕЖДУ СТРИНГОВЕТЕ"
# print(txt, txt_2, sep='. . .')


