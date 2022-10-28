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
