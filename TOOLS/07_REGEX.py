"REGULAR EXPRESIONS"     #
import re

# https://regex101.com
# https://pythex.org
# https://www.w3schools.com/python/python_regex.asp

text = "Hello, I'm @22 yeas old, and you are @26 years old, not the @136. " \
       "The waterfall was so high, that the child couldn't see its peak"



"re.findall - ВРЪЩА ЛИСТ СЪС ВСИЧКИ СЪВППАДЕНИЯ"
# text = "@22, 154, 235, 33"
# print(re.findall("\d{2}", text))

# print(len(re.findall("the", text, re.IGNORECASE)))    # игнорира главни букви



"re.finditer - при групи в регекса"
# pattern = r"(\+359 2 \d{3} \d{4})\b|(\+359-2-\d{3}-\d{4}\b)"
# text = "+359/2/222/2222, +359-2 222 2222 +359 2 222 2222 +359-2-222-2222 +359 2-222-2222"
# results = re.finditer(pattern, text)
# for x in results:
#     print(x.group())
#
# print([x.group() for x in results])



"ЗАМЕНЯ ФЛАГА В FINDALL (?i)"
# searched_word = "The"
# pattern = fr'(?i)\b{searched_word}\b'       # ignorecase
# print(re.findall(pattern, text))




"re.search - ВРЪЩА ПЪРВИЯ МАЧ ОТ ТЕКСТ С МНОГО РЕДОВЕ"
# text = "peter smith, peter Smith, peter Smith, " \
#        "PEter Smith, Ivan Peshov, Lily Everett"
# result = re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
# result = result.group()
# print(result)
# print(type(result))



"re.match - ВРЪЩА АКО ИМА МАЧ В НАЧАЛОТО НА ПЪРВИЯ РЕД ОТ ТЕКСТА"
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = "Peter Smith, peter Smith, " \
#        "PEter Smith, Peter SmIth, Lily Everett"
# print(re.match(pattern, text))
# result = re.match(pattern, text)
# print(result.group())



"result.start(), result.end() - ВРЪЩА НАЧАЛЕН И КРАЕН ИНДЕКС НА ОБЕКТА ОТ МАЧА"
# text = "peter smith, Peter Smith, Lilly"
# result = re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
# print(result.start(), result.end())


"f string ФОРМАТИРАНЕ В REGEX"
# searched_word = "the"
# pattern = fr'{searched_word}'
# print(re.findall(pattern, text))



"result.group()"        # връща резултатите от обект
"result.groups()"       # връща списък с тюпъли с всички групи


"ГРУПИ И ИЗВИКВАНЕ"     # каквото мачне на едното място, такова мачва и на другото място, а не „или“
"РЕЧНИК OT ГРУПИ"         # връща ги именовани или като цифри
# pattern = r"(?P<Day>\d{2})(?P<separator>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
# text = "13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016"
# valid_dates = re.finditer(pattern, text)
# for date in valid_dates:
#     current_date = date.groupdict()
#     print(f"Day: {current_date['Day']}, Month:  {current_date['Month']}, Year:  {current_date['Year']}")


"СМЕНЯ ЕЛЕМЕНТИ В СТРИНГА"
# txt = "The rain in Spain"
# print(re.sub("\s", "--", txt))


"СПЛИТ"                 # връща списък на всички елементи
# text = "The rain in Spain"
# print(re.split("\s", text))
# print(re.split("\s", text, 1))      # разделя замо при първото съвпадение


"POSITIVE LOOKBEHIND мачва ако има нещо конкретно преди това"
# text = "BGN 200 RUS 2000 USD 3000"
# result = re.search('(?<=RUS)\s(\d+)', text)
# print(result.group())


"NEGATIVE LOOKBEHIND мачва ако няма конкретно нещо преди това"
# text = "BGN 200 RUS 2000 USD 3000"
# result = re.search('(?<!BGN)\s(\d+)', text)
# print(result.group())



"ОКАЗВА НАЧАЛОТО И/ИЛИ КРАЯ НА МАЧА"
# text = "The rain in Spain"
# print(re.findall("in", text))
# print(re.findall("\bin", text))         # не знам защо не работи



""" СИНТАКСИС

МАЧВА ЧИСЛА, ЦИФРИ
    \d      мачва цифрите
    \d+     мачва ена цифра или всичките последващи
        01q23wt4hh5ABCD


МАЧВА ВСИЧКО БЕЗ ЧИСЛА
    \D      мачва поединични
    \D+     мачва на низове - първата и последващите
        012345ABCD
    
    



МАЧВА SPACES-а      може и само чрез спейс
    \s
        А   Б   x
    
    
МАЧВА ВСИЧКО ОСВЕН СПЕЙСА
    \S
    
    
"ГРУПА"
    \d{2}([/ [-])[A-Z][a-z]{2}(\1)\d{4}
        13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 01/Feb/2016


"ИМЕНОВАНА ГРУПА"
    \d{2}(?P<separator>[/ -])[A-Z][a-z]{2}(\1)\d{4}
        13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 01/Feb/2016


„ ? “ МОЖЕ ДА ГО ИМА ИЛИ ДА ГО НЯМА
    -?\d
        -11 22



ЧИСЛА, „ _ “ и БУКВИ
    \w
        PFord 555 22___ @@!#
    \W      мачва всичко освен числа, „_“ и букви


„ + “  МАЧВА ЕДИН ИЛИ ПОВЕЧЕ СИМВОЛИ ПОСТАВЕН СЛЕД \d, \b ....
    \+           когато се търси точно + трябва да се ескейпе
        +359


„ . “  МАЧВА СИМВОЛА СЛЕД НЕЯ
    +359.
    +359.+      мачва всички символи до края на реда
        TEL: +359123456 0888123456


„ * “  МАЧВА 0 ИЛИ ПОВЕЧЕ СИМВОЛИ, когато е поставена след нещо
    asd\d
    asd\d*
        weerasd5addhh76
        weerasdaddhh76
          

„ | “  ВРЪЩА ЕДИН И/ИЛИ ДВАТА СИМВОЛА
    a|x
        abvgz wertx waxing
    
    
„ ^ “ МАЧВА AKO АБЗАЦА ЗАПОЧВА С ВАЛИДЕН РЕГЕКС
    ^Ford       всичко без Ford
        Ford Ford Ford5 PFord
        Ford Ford Ford5 PFord
        
        
„ ^[]“ МАЧВА ВСИЧКО БЕЗ НЕЩОТО в []
        
        
„ $ “ МАЧВА АКО РЕДА ЗАВЪРШВА С ВАЛИДЕН REGEX
    Ford$
        Ford Ford Ford5 PFord  Ford5 Ford
        Ford Ford Ford5 PFord  Ford5 Ford
        
        
„ ? “ СИМВОЛА ДЕТО ТЪРСИМ МОЖЕ ДА ГО ИМА, МОЖЕ И ДА ГО НЯМА, когато ? е поставен след нещо
    sentence = "Bread и Ice cream"
    pattern = r"\b([A-Za-z]+\s?[A-Za-z]+)\b"
    print(re.findall(pattern, sentence))

    
„ () “  ГРУПИРА И ВРЪЩА МАЧ ГРУПА
    (+359|0)\d+
        +359886123456    0886123456


„ {} “  МАЧВА ДО ОПРЕДЕДЛЕН БРОЙ СИМВОЛИ В ГРУПА
    \d{9}
        +359123456888123456
    \+359\d{9}\b     ще мачне ако завършва до числото в {}
        +359886123456888123456   +359886123456 
    \d{3,}      3 или повече числа
        
„ [] “ МАЧВА СИМВОЛИТЕ В СКОБИТЕ
    [Ffar]
    [Ffa]+      ако има низ го показва
    [a-n]       мачва всичко от-до
    [a-zA-Z]    мчава всички букви
    1[0-9]      мачва от 10 до 19
    [^ar]
        Ford fart15 21        
        
   
   

"""
