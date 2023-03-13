"MODULES"   # модули и библиотеки
            #


"СЪЗДАВАНЕ НА МОДУЛ"
""" 
- създаваме new package
- в тази директория правим файл с логиката: core.py - там отиват функциите
- правим основен файл: main - там отива главното действие
- в main.py извикваме с alt + enter

"""

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

# player = "WER"
# result = figlet_format(f"{player} won!")
# print(result)


"REDUCE - РЕДУЦИРА СПИСЪК С ЧИСЛА ЧРЕЗ УМНОЖЕНИЕ, ДЕЛЕНИЕ И т.н."
# from functools import reduce
# data = (2, 3, 5, 7, 3)
# print(reduce(lambda x, y: x + y, data))



"RANDOM"
# import random
# num = range(1, 100)
# print(random.choice(num))
# print(random.shuffle(nums))




# print([x if x =="e" else -1 for x in "sometext"])

# ma = [[1], [2], [3]]
# print(ma[3][0])
