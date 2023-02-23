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


class Book:
    def __init__(self, title, author, publisher, image_url, price, short_desc): # конструктор на класа
        self.tittle = str(title)         # характеристики property на класа
        self.author = author
        self.publisher = publisher
        self.iage_url = image_url,
        self.price = float(price)
        self.short_desc = short_desc
        self.type = "paper book"

    def open_the_book(self):         # чрез self достъпваме proprety-та на класа  # метод на класа, поведение на обекта
        return f"Opening the book '{self.tittle}' with author {self.author.first_name}"


class Author:
    def __init__(self, first_name, last_name, age=30, *args):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.args = args



author_book_1 = Author("Уолтър", "Айзъксън", 50, 'заглавие 1', 'заглавие 2', 'заглавие 3')
author_book_2 = Author("Иван", "Иванов")

book_1 = Book("Стив Джобс", author_book_1, "СофтПрес", "aaa.png", 35, "Биографията на...")  # инстанция на класа
book_2 = Book("Егото", author_book_2, "Изток-Запад", "bbb.png", 18.50, "Психология на ...") # инстанция на класа
basket = []

basket.append(book_1)
basket.append(book_2)
total_price = 0

# for book in basket:
#     total_price += book.price
# print(total_price)



"ДОСТЪПВАНЕ ДО PROPERTY-то"
# print(book_1.tittle)
# print(book_2.author.first_name)
# print(book_1.open_the_book())
# print(author_book_1.args)
# print(book_1.price + book_2.price)
print(book_1.type)