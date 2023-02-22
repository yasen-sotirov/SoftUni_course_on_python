"CLASS and OBJECTS"     # Класът вдига инстанции на обект („инстанция“ поредна степен в йерархията на органи)
                        # „Class“ - шаблона, който определя общите характеристики на обекта
                        # като „типов етаж“ на сграда
                        # По-сложен тип данни съдържащ характеристики, които ние задаваме
                        # build-in класовете са с мали букви list(), set(), dict()
                        # „self“ - грубо казано, поема стойноста на променливата („book_1“, „book_2“)
                        # различните „self. ...“ се казват property
class Book:
    def __init__(self, title, author, publisher, image_url, price, short_desc):
        self.tittle = title
        self.author = author
        self.publisher = publisher
        self.iage_url = image_url,
        self.price = price
        self.short_desc = short_desc


book_1 = Book("Стив Джобс", "У.Айзъксън", "СофтПрес", "aaa.png", 35, "Биографията на...")
book_2 = Book("Егото", "П.И", "Изток-Запад", "bbb.png", 18.50, "Психология на ...")


"ДОСТЪПВАНЕ ДО PROPERTY-то"
print(book_1.tittle)
print(book_2.author)