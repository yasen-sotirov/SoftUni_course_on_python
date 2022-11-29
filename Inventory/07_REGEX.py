"REGULAR EXPRESIONS"  # https://regex101.com/   https://pythex.org/
import re


"ВРЪЩА ЛИСТ СЪС ВСИЧКИ МАЧОВЕ"  # дава ги под ред   връща само групите
# input_text = "Hello, I'm 22 yeas old and you are 26 years old, not 136."
# pattern = r"\b\d{2}\b"
# print(re.findall(pattern, input_text))


"ВРЪЩА ИНДЕКСИ САМО НА ПЪРВИЯ МАЧ"
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = "peter smith, Peter Smith, Peter Smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett"
# result = re.search(pattern, text)
# print(result.start(), result.end())
# print(result.group())



"FINDITER - при групи в регекса"
# pattern = r"(\+359 2 \d{3} \d{4})\b|(\+359-2-\d{3}-\d{4}\b)"
# text = "+359/2/222/2222, +359-2 222 2222 +359 2 222 2222 +359-2-222-2222 +359 2-222-2222"
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match.group())

# print([match.group() for match in matches])


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


"POSITIVE LOOKBEHIND мачва ако има нещо конкретно преди това"
# text = "BGN 200 RUS 2000 USD 3000"
# result = re.search('(?<=RUS)\s(\d+)', text)
# print(result.group())


"NEGATIVE LOOKBEHIND мачва ако няма конкретно нещо преди това"
# text = "BGN 200 RUS 2000 USD 3000"
# result = re.search('(?<!BGN)\s(\d+)', text)
# print(result.group())


"ЗАМЕНЯ ФЛАГА В FINDALL (?i)"
# sentence = "The waterfall was so high, that the child couldn't see its peak"
# searched_word = "The"
# pattern = fr'(?i)\b{searched_word}\b'       # ignorecase
# matches = re.findall(pattern, sentence)
# print(len(matches))


""" СИНТАКСИС

МАЧВА ЧИСЛА, ЦИФРИ
    \d      мачва цифрите
    \d+     мачва ена цифра или всичките последващи
        01q23wt4hh5ABCD


МАЧВА ВСИЧКО БЕЗ ЧИСЛА
    \D      мачва поединични
    \D+     мачва на низове - първата и последващите
        012345ABCD
    
    
ОКАЗВА НАЧАЛОТО И/ИЛИ КРАЯ НА МАЧА
    \b      
        F[a-z]{3}\b
    \bFord\b
        Ford Ford5 PFord
    \+359\d{9}\b     ще мачне ако завършва до числото в {}
        +359886123456888123456   +359886123456 


МАЧВА SPACES-а      може и само чрез спейс
    \s
        А   Б   x
    
    
МАЧВА ВСИЧКО ОСВЕН СПЕЙСА
    \S
    
    
"ГРУПА"
    \d{2}([/ -])[A-Z][a-z]{2}(\1)\d{4}
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
