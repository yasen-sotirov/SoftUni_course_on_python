"REGULAR EXPRESIONS"    #https://pythex.org/
import re


"ВРЪЩА ЛИСТ СЪС ВСИЧКИ МАЧОВЕ"      # дава ги под ред
# input_text = "Hello, I'm 22 yeas old and you are 26 years old, not 136."
# pattern = r"\b\d{2}\b"
# print(re.findall(pattern, input_text))

"ВРЪЩА ИНДЕКСИ САМО НА ПЪРВИЯ МАЧ"
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = "peter smith, Peter Smith, Peter Smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett"
# result = re.search(pattern, text)
# print(result.start(), result.end())
# print(result.group())


"FINDITER"
pattern = r"(\+359 2 \d{3} \d{4})\b|(\+359-2-\d{3}-\d{4}\b)"
# text = "+359/2/222/2222, +359-2 222 2222 +359 2 222 2222 +359-2-222-2222 +359 2-222-2222"
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match.group())

# print([match.group() for match in matches])


""" СИНТАКСИС

МАЧВА ЧИСЛА, ЦИФРИ
    \d      мачва цифрите
    \d+     мачва числата
        01q23wt4hh5ABCD


МАЧВА ВСИЧКО БЕЗ ЧИСЛА
    \D      мачва поединични
    \D+     мачва на низове
        012345ABCD
    
    
ОКАЗВА НАЧАЛОТО И/ИЛИ КРАЯ НА СЕЛЕКЦИЯТА
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


„ _ “, ЧИСЛА и БУКВИ
    \w
        PFord 555 22___ @@!#
    \W      мачва всичко освен числа, „_“ и букви


„ + “  СПЕЦИАЛЕН СИМВОЛ - ТРЯБВА ДА СЕ ESCAPE-не
    \+
        +359


„ . “  МАЧВА СИМВОЛА СЛЕД НЕЯ
    +359.
    +359.+      мачва всички символи до края на реда
        TEL: +359123456 0888123456


„ * “  СИМВОЛЪТ КЪМ КОЙТО Е ПРИКРЕПЕНА МОЖЕ ДА ГО ИМА ИЛИ ДА ГО НЯМА
    asd\d
    asd\d*
        weerasd5addhh76
        weerasdaddhh76
          

„ | “  ВРЪЩА ЕДИН И/ИЛИ ДВАТА СИМВОЛА
    a|x
        abvgz wertx waxing
    
    
„ ^ “  МАЧВА, АКО РЕДА ЗАПОЧВА С ВАЛИДЕН REGEX
    ^Ford
        Ford Ford Ford5 PFord
        Ford Ford Ford5 PFord
        
        
„ $ “ МАЧВА АКО РЕДА ЗАВЪРШВА С ВАЛИДЕН REGEX
    Ford$
        Ford Ford Ford5 PFord  Ford5 Ford
        Ford Ford Ford5 PFord  Ford5 Ford


„ () “  ГРУПИРА И ВРЪЩА МАЧ ГРУПА
    (+359|0)\d+
        +359886123456    0886123456


„ {} “  МАЧВА ДО ОПРЕДЕДЛЕН БРОЙ СИМВОЛИ В ГРУПА
    \d{9}
        +359123456888123456
    \+359\d{9}\b     ще мачне ако завършва до числото в {}
        +359886123456888123456   +359886123456 
        
        
„ [] “ МАЧВА СИМВОЛИТЕ В СКОБИТЕ
    [Ffar]
    [Ffa]+      ако има низ го показва
    [a-n]       мачва всичко от-до
    [a-zA-Z]    мчава всички букви
    1[0-9]      мачва от 10 до 19
    [^ar]
        Ford fart15 21        
        
   

"""

