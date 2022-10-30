"""" Create a class Storage. The __init__ method should accept one parameter -
the capacity of the storage. The Storage class should also have an attribute called storage -
empty list, where all the items will be stored.
The class should have two additional methods:
•	add_product(product: str) - adds the product in the storage if there is enough space for it
•	get_products() - returns the storage list
"""


class Warehouse:
    storage_list = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Warehouse.storage_list.append(product)
            self.capacity -= 1

    def show_products_in_storage_list(self):
        return Warehouse.storage_list


food_storage = Warehouse(4)
food_storage.add_product("apple")
food_storage.add_product("banana")
food_storage.add_product("potato")
food_storage.add_product("tomato")
food_storage.add_product("bread")
print(food_storage.show_products_in_storage_list())

car_storage = Warehouse(3)
car_storage.add_product("bmw")
car_storage.add_product("opel")
car_storage.add_product("audi")
print(car_storage.show_products_in_storage_list())
