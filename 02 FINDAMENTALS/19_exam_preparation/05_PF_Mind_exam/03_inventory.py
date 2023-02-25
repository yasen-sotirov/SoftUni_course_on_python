""" Problem 3. Inventory
judge system at https://judge.softuni.org/Contests/Practice/Index/2028#2.

As a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", ").
After that, until receiving "Craft!" you will be receiving different commands split by " - ":
•	"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
•	"Drop - {item}" - you should remove the item from your inventory if it exists.
•	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
•	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.

Output
After receiving "Craft!" print the items in your inventory, separated by ", ".

    Examples
    Input
Iron, Wood, Sword
Collect - Gold
Drop - Wood
Craft!

    Output
Iron, Sword, Gold

    Input
Iron, Sword
Drop - Bronze
Combine Items - Sword:Bow
Renew - Iron
Craft!

    Output
Sword, Bow, Iron
 """


collecting_items = input().split(", ")
command = input().split(' - ')
inventory = collecting_items

while "Craft!" not in command:
    if command[0] == 'Collect':
        if not command[1] in inventory:
            inventory.append(command[1])
    elif command[0] == 'Drop':
        if command[1] in inventory:
            inventory.remove(command[1])
    elif command[0] == "Combine Items":
        new_command = ':'.join(command)
        command = new_command.split(':')
        if command[1] in inventory:
            old_item_index = inventory.index(command[1])
            inventory.insert(old_item_index + 1, command[2])
    elif command[0] == "Renew":
        if command[1] in inventory:
            inventory.remove(command[1])
            inventory.append(command[1])
    command = input().split(' - ')

print(", ".join(inventory))
