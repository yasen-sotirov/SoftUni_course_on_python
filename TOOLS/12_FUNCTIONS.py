"ФУНКЦИИ"       # за да приключи функцията трябва да имаме return
                # задължителните, наименованите, args, kwargs
                # променлива, която е дефинирана във функция не е видима извън нея



"ОПАКОВАНЕ В ЛИСТ *ARGS"        # поема неограничен брой аргументи и ги опакова в масив
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
# nums = [1, 2, 3]
# print_nums(*nums)

# def even_odd(*args):
#     *numbers, command = args
#     party = 0 if command == "even" else 1
#     return [el for el in numbers if el % 2 == party]
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))



"**KVARGS"  # key-word args, поема неограничен бр наименувани елементи
# def info_functtion(**kwargs):                     # ОПАКОВА В РЕЧНИК
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} " \
#            f"and he is {kwargs.get('age')} years old"
#
# print(info_functtion(**{"name": "George", "town": "Sofia", "age": 20}))  # РАЗОПАКОВА РЕЧНИК И ГО ПОДАВА КАТО ПАРАМЕТЪР
# print(info_functtion(name="George", town="Sofia", age=20))



"ДОБАВЯНЕ МАХАНЕ И ДР. ОТ **KWARGS"  # работи със всички методи на речници дето си знаем
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
#     print(example_func([1, 2, 3], {"a": 1, "b": 2}, 1, 2, 3, name="Test"))



"РЕКУРСИЯ"
""" Пример:
Влизаш в папка и броиш колко папки има в нея,
после влизаш в съб папката и броиш колко папки иам в нея.
И така докато стигнеш дъното, където няма повече папки.
Когато започваш, няма как да знаеш колко папки има надолу."""

# def say_hello(n=5):
#     if n == 0:
#         return
#     print("Hello")
#     say_hello(n - 1)
#
# say_hello()



"ОБЕДИНЯВА *ARGS"
# def concatenate(*args):
#     return ''.join(args)
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!"))

