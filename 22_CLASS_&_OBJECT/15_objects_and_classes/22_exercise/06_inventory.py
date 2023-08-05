"""" Create a class Inventory. The __init__ method should accept only the __capacity:
int (private attribute) of the inventory. You can read more about private attributes here.
Each inventory should also have an attribute called items - empty list, where all the items will be stored.
The class should also have 3 methods:"""


class Inventory:
    __capacity = 0
    items = []

    def __init__(self, capacity: int):
        Inventory.__capacity = capacity

    def add_item(self, item: str):
        if len(Inventory.items) < Inventory.__capacity:
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {Inventory.__capacity - len(Inventory.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")

print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
