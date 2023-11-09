"CLASS and OBJECTS"     # Класът вдига инстанции на обект („инстанция“ поредна степен в йерархията на органи)
                        # „Class“ - шаблона, който определя общите характеристики на обекта
# като „типов етаж“ на сграда
# По-сложен тип данни съдържащ характеристики, които ние задаваме
# build-in класовете са с мали букви list(), set(), dict()
# „self“ - грубо казано, поема стойноста на променливата („book_1“, „book_2“)
# различните „self. ...“ се казват property
# всичко което важи за функциите се отнася и за конструктура
# __init__ конструктор на класа
# self. към него се закача името на инстанцията (обекта)
# не е добре да се добавят или премахват атрибути извън класа


class Books:
    market = "Bookstore"        # атрибут на класа, глобален за целия клас. всички инстанции ще го ползват
    min_price = 5                            # достъпват се през името на класа, не през self

    def __init__(self, title, author, price, type_book="paper book"):  # конструктор
        self.title = str(title)        # „атрибут/пропърти/variable“ - дефинира характеристиките на класа
        self.author = author           # атрибут на инстанцията, само тя си го ползва
        self.price = float(price)
        self.type = type_book          # default parameter
        self.notes = []
        self.is_rented: bool = False

    def change_price(self, new_price):      # „метод“ дефинира действията на класа, променя атрибутите
        self.price = new_price              # чрез self достъпваме proprety-та на класа
                                            # метод на класа, поведение на обекта

    def __str__(self):                      # директно принтира обекта
        return f"заглавие: '{self.title}'\n" \
               f"автор: '{self.author.first_name}'\n" \
               f"цена: {self.price} лв\n" \
               f"магазин: {Books.market}"

    @staticmethod       # име на декоратора
    def clean():        # статичен метод - самостоятелна независима функция в класа, не ползва self-a
        return 'Cleaning books'     # добра практика е да се извиква от класа, не от инстанцията(обекта)

    @classmethod           # class/factory метод - създава нова инстанция на класа и променя един или всички параметри
    def promotion(cls, title, author, price, type_book="paper book"):      # зарежда всички атрибути на __init__
        return cls(title, author, 10)

    @classmethod
    def all_from_pratchett(cls, title, author):
        return cls(title, "T.Pratchett", 22)


class Author:       # примерен клас използван в основния клас
    min_price = 4

    def __init__(self, first_name, last_name, *args):
        self.__first_name = first_name      # ако искаме валидация в конструктора, махама „__“
        self.last_name = last_name
        self.args = args

    @property                       # "autor_1.first_name" връща стойността
    def first_name(self):
        return self.__first_name

    @first_name.setter                  # autor_1.first_name = "..." пуска setter-a
    def first_name(self, value):        # служи за валидация и „ограничаване“ на достъпа
        if len(value) < 3:
            raise ValueError("Name must be more than 3 chars")
        self.__first_name = value

    @property
    def last_name(self):
        return

    @last_name.setter
    def last_name(self, value):
        pass

    @classmethod
    def validate_min_price(cls, value):
        if cls.min_price > value:
            raise ValueError(f"The price must be min {cls.min_price}")


author_1 = Author("Уолтър", "Айзъксън", 'заглавие 1', 'заглавие 2', 'заглавие 3')
author_2 = Author("Иван", "Иванов")
author_3 = Author("Джо", "Малкия")
print(author_3.first_name)

book_1 = Books("Стив Джобс", author_1, 35)             # инстанция на класа
book_1.notes.append(["note 1", "note 2"])
book_2 = Books("Егото", author_2, 18.50, "e-book")     # инстанция на класа
book_5 = Books("Notebook", None, 2)
print(book_5.price)


"РАБОТА С ИНСТАНС АТРИБУТИ"
# print(book_1.title)
# print(book_1.change_price(20))

# print(book_1.__str__())
# print(book_2)

# print(author_1.args)
# print(book_1.price + book_2.price)

# print(book_2.type)


"РАБОТА С КЛАС АТРИБУТИ"
# print(book_1.market)
# print(book_2.market)
# print()
# book_1.market = "Helikon"
# print(book_1.market)
# print(book_2.market)
# print()
# Books.market = "Ciela"
# print(book_1.market)
# print(book_2.market)


"CLASS METHOD"
# book_3 = Books.promotion('"Class method book 3"', "az", 50)
# print(book_3.title)
# print(book_3.price)
# book_4 = Books.all_from_pratchett("Mort", "...")
# print(book_4.author)


"STATIC METHOD"
# print(Books.clean())


"@...SETTER"                    # служи за валидация и „ограничаване“ на достъпа
# author_1.first_name = "Уолт"    # вместо „author_1.set_age(25)“  става на  „object_1.age = 25“


"@PROPERTY"                     # (getter) пропърти декоратор, може да се извика кто атрибута
# print(author_1.first_name)      # или прави проверка, която не се дефинира в init-a
                                # вместо „author_1.get_age()“   става на


"НАСЛЕДЯВАНЕ"
"SINGLE"    # един клас наследен от един наследник
            # наследява super().__init__(...)
"MULTIPLE"      # наследява повече от един родителлски клас
                # ако в наследените класове има два еднакви метода, взема този от първия
# class Daughter(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
"MULTILEVEL"    # наследникът ства бащин клас за друг клас
"HIERARCHICAL"  # няколко различни класа наследяват един родителски клас
"HIBRID INHERITANCE"
"MIXIN, interface"  # мъничък клас само от методи, които могат да се наследят
# наследяват се ор различни класове, които трябва да имат тази обща функционалност
# mixin-ите се записват най-накрая



"ENCAPSULATION"     # за атрибути и методи
# __name            private - видимо само в класа       self.__pin = pin
# _name             protected - видимо в класа и неговите наследници
# name              public - видими за всички
# mangling          правим ги недостъпни (private, protected) погрозняване





"ДЕКОРАТОРИ GETTER & SETTER"
# съкращава синтаксиса и намалява грешките
# за да не изпадне в рекурсия пропъртитата се погрозняват
# тук се правят валидациите на данните, които подават
# когато е в кода програмата минава първо през setter-a




"DUNDER / MAGIC МЕТОДИ НА КЛАСА"

"__class__"
# print(book_1.__class__.__name__)        # достъпваме името на класа


"__dict__"
# print(book_2.__dict__)
# "{'tittle': 'Егото', 'author': <__main__.Author object at 0x00EAFE50>, " \
# "'price': 18.5, 'type': 'e-book', 'notes': []}"


"__repr__"      # да се ползва от програмисти и технически хора
                # добре е да връща стринг, който ако подадем на eval да върне обект

"__str__"      # за ползвателя
# print(str(book_1))        # печати обекта или предварително подготвеният му стринг
# print(book_1)


"__doc__"   # връща коментацията
# print(Books.__doc__)
# print(Author.__doc__)



"BUILD-IN FUNCTIONS FOR ACCESSING ATTRIBUTES"

"getattr()"
# print(getattr(book_1, "title"))         # ще гръмне ако го няма този атрибут
# print(getattr(book_1, "tit", None))     # безопасен метод

"hasattr()"
# print(hasattr(book_1, "pages"))

"setattr()"         # не е добра практика да се ползва
# print(setattr(book_1, "num_pages", "524"))

"изтриване на атрибут на инстанцията"
# delattr(book_1, 'price')
# print(book_1)


