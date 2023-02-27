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
    """ Примерен клас"""
    market = "Bookstore"      # атрибут на класа, глобален за целия клас. всички инстанции ще го ползват

    def __init__(self, title, author, price, type_book="paper book"):  # конструктор
        self.tittle = str(title)       # „атрибут/пропърти/variable“ - дефинира характеристиките на класа
        self.author = author           # атрибут на инстанцията, само тя си го ползва
        self.price = float(price)
        self.type = type_book          # default parameter
        self.notes = []

    def change_price(self, new_price):      # „метод“ дефинира действията на класа, променя атрибутите
        self.price = new_price              # чрез self достъпваме proprety-та на класа
                                            # метод на класа, поведение на обекта

    def __str__(self):                      # директно принтира обекта
        return f"заглавие: '{self.tittle}'\n" \
               f"автор: '{self.author.first_name}'\n" \
               f"цена: {self.price} лв\n" \
               f"магазин: {Books.market}"


class Author:
    """ примерен клас използван в основния клас"""
    def __init__(self, first_name, last_name, *args):
        self.first_name = first_name
        self.last_name = last_name
        self.args = args


author_book_1 = Author("Уолтър", "Айзъксън", 'заглавие 1', 'заглавие 2', 'заглавие 3')
author_book_2 = Author("Иван", "Иванов")

book_1 = Books("Стив Джобс", author_book_1, 35)             # инстанция на класа
book_1.notes.append(["note 1", "note 2"])
book_2 = Books("Егото", author_book_2, 18.50, "e-book")     # инстанция на класа


"РАБОТА С ИНСТАНС АТРИБУТИ"
# print(book_1.tittle)

# print(book_1.change_price(20))

# print(book_1.__str__())
# print(book_2)

# print(author_book_1.args)
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




"DUNDER / MAGIC МЕТОДИ НА КЛАСА"

"__dict__"
# print(book_2.__dict__)
# "{'tittle': 'Егото', 'author': <__main__.Author object at 0x00EAFE50>, " \
# "'price': 18.5, 'type': 'e-book', 'notes': []}"


"__str__"
# ако тръгнем да печатим обекта, връща предварително подготвен стринг с репрезентация на обекта


"__doc__"   # връща коментацията
# print(Books.__doc__)
# print(Author.__doc__)

