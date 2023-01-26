"ФУНКЦИИ"  # advanced
# задължителните, наименованите, args, kwargs


"ОПАКОВАНЕ В ЛИСТ *ARGS"                         # Pпоема неограничен брой аргументи
# def print_nums_funct(*args):
#     for el in args:
#         print(el)
#
# nums_1 = 1
# nums_2 = 2
# nums_3 = 3
# print_nums_funct(nums_1, nums_2, nums_3)



"РАЗОПАКОВАНЕ НА ЛИСТ"
# def print_nums(a, b, c):
#     print(a, b, c)
#
# nums = [1, 2, 3]
# print_nums(*nums)



"**KVARGS"      # key-word args, поема неограничен бр наименувани елементи
# def info_functtion(**kwargs):                     # ОПАКОВА В РЕЧНИК
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} " \
#            f"and he is {kwargs.get('age')} years old"
#
#
# print(info_functtion(**{"name": "George", "town": "Sofia", "age": 20}))  # РАЗОПАКОВА РЕЧНИК И ГО ПОДАВА КАТО ПАРАМЕТЪР
# print(info_functtion(name="George", town="Sofia", age=20))




"ДОБАВЯНЕ МАХАНЕ И ДР. ОТ **KWARGS"       # работи със всички методи на речници дето си знаем
# def info_functtion(**kwargs):
#     kwargs["example"] = 123
#     print(kwargs)
#     del kwargs["name"]
#     print(kwargs)
#
# info_functtion(**{"name": "George", "town": "Sofia", "age": 20})


"ИТЕРИРАНЕ ПРЕЗ **KWARGS"
# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{value}, {key}")
#
# greet_me(Peter="Hello", George="Bye")


"ВКЛЮЧВАНЕ НА РЕЧНИЦИ И ДРУГИ"
# def example_func(nums, dict, *args, **kwargs):
#
#
#     print(example_func([1, 2, 3], {"a": 1, "b": 2}, 1, 2, 3, name="Test"))
