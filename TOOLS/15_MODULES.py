"MODULES"   # модули и библиотеки
            #




"ИНСТАЛИРАНЕ ВЪНШНИ БИБЛИОТЕКИ ПРЕЗ ТЕРМИНАЛ"      # PIP - python manger, който ни позволява да сваляме пакет от интернет
# в терминала на pycharm, при активен „venf“ (в началото на адреса), пишем: pip install ....
# за да ги инсталира във venf, а не глобално на компютъра
# инсталира пакета в „External Libraries“ в „Site-packages“ и „venf“


"ИНСТАЛИРАНЕ ВЪНШНИ БИБЛИОТЕКИ ПРЕЗ PYCHARM"       # по-добре е през терминала, за да се види дали е активен venf
# file>settings>Project:...>Project:...Interpreter> „+“ и търсим



"ПОКАЗВА ВСИЧКИ БИБЛИОТЕКИ, КОИТО СЕ ПОЛЗВАТ В ПРОЕКТА"
# в терминала
# pip freeze



"ЗАПАЗВА ВСИЧКИ ИЗИСКВАНИЯ КЪМ ФАЙЛ"
# в терминала
# pip freeze > requirements.txt         # слага го във venf
                                        # хубаво е новите библиотеки, които инсталираме,
                                        # да се дописват на ръка в requirements.txt


"ИНСТАЛИРА НЕОБХОДИМИТЕ ЗА ПРОЕКТА БИБЛИОТЕКИТЕ, КАТО ГИ ВЗЕМА ОТ ФАЙЛА"
# в терминала
# pip install -r requirements.txt



"ЪПГРЕИД НА БИБЛИОТЕКА"     # Важно! Да се свери дали кода работи с новия пакет, има ли разлики в командите
# pip install <package_name> --upgrade



"ВИДОВЕ ИМПОРТ"
# import math
# print(math.sqrt(25))

# from math import sqrt     # добър вариант
# print(sqrt(25))

# from math import *      # кофти вариант



"ПОПУЛЯРНИ ALIAS - ПСЕВДОНИМИ НА БИБЛИОТЕКИТЕ"  # Казва се alias - използваш библиотеката чрез прякор
# import numpy as np
# import pandas as pd
# from math import floor as fl, ceil as ce



"БИБЛИОТЕКИ"
# datetime  -   дати

# functools -   функционалности

# math      -   математически изрази

# pyfiglet  -   принтира текста с арт визия от тирета и слашове

player = "WER"
result = figlet_format(f"{player} won!")
print(result)


# email validator       # pip install email_validator
# import random
# num = range(1, 100)
# print(random.choice(num))
# print(random.shuffle(nums))



