""" It's the end of the week, and it is time for you to go shopping,
so you need to create a shopping list first.

Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
•	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
•	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
•	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
•	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.

Constraints
•	There won't be any duplicate items in the initial list

Output
•	Print the list with all the groceries, joined by ", ":
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"


Examples

Input
Tomatoes!Potatoes!Bread
Unnecessary Milk
Urgent Tomatoes
Go Shopping!

Output
Tomatoes, Potatoes, Bread
"""


shopping_list = input().split("!")
command = input().split()

while len(command) > 1:
    action = command[0]
    item = command[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif "Unnecessary" in action:
        if item in shopping_list:
            shopping_list.remove(item)
    elif "Correct" in action:
        new_item = command[2]
        if item in shopping_list:
            item_index = int(shopping_list.index(item))
            shopping_list.remove(item)
            shopping_list.insert(item_index, new_item)
    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input().split()

print(", ".join(shopping_list))
