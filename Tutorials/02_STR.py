"""STRING"""    # колекция, низ от символи, които могат да бъдат обходени


txt = "- I like bananas !!"
txt_2 = 'Very much!'
txt_3 = "123456"

"РАЗДРОБЯВА СТРИНГ НА ЕЛЕМЕНТИ"
# edit = txt.split()

"ЗАМЕНЯ ЕЛЕМЕНТ"
# edit = txt.replace("bananas", "apples")

"ПРЕМАХВА ЕЛЕМЕНТ ОТ НАЧАЛОТО И КРАЯ НА ТЕКСТА"
# edit = txt.strip("-!")

"ДОБАВЯ ЕЛЕМЕНТ ОТ НАЧАЛОТО И КРАЯ НА ТЕКСТА"
# edit = txt.join('#@')

"РАЗДРОБЯВА СТРИНГ НА ЕЛЕМЕНТИ"
# edit = txt.split()

"БРОЙ ЕЛЕМЕНТИ В СТРИНГА"
# edit = txt.count('n')

"СЛАЙСИНГ"              # работи и за лист
# edit = txt[2]         # показва кой символ е на индекс
# edit = txt[1:9:2]     # показва символи от индекс до индекс със стъпка

"ГЛАВНИ и МАЛКИ БУКВИ"
# edit = txt.lower()
# edit = txt.upper()

# edit = txt.islower()
# edit = txt.isupper()

"ЧИСЛА ЛИ СА"
# edit = txt_3.isalnum()
# edit = txt_3.isdigit()

"ПОСТАВЯ СЕПАРАТОР МЕЖДУ СТРИНГОВЕТЕ"
# print(txt, txt_2, sep='. . .')

print(edit)
