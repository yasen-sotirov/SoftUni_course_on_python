"OOP"   #


"SCOPE"     # парчето код оформено от идентацията (tab-a навътре)
# build-in scope - парчетата код вградени в самия python
# global scope - кода в целият ни файл
# encloseing scope - кода във функцяи съдържаща други функции
# local scope - кодa във функцията, която ние съм написал def...

x = "x = 15"
def enclose_scope():
    x = "x = 10"
    print(x)
    def local_scope():
        x = "x = 5"
        print(x)
    return local_scope()

print(x)
enclose_scope()






"GLOBAL"        # ДА НЕ СЕ ПОЛЗВА! Чупи кода лошо
# a = 100         # приравнява global scope към local scope
# print(a)
#
# def sum_nums():
#     global a
#     a = 5
#     b = 10
#     return a + b
#
# print(sum_nums())
# print(a)


"NONLOCAL"
# ако ползваме nonlocal върху променлива в local функция,
# променливата се променя и в encloseing-a