list_of_gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    command = command.split()
    if command[0] == "OutOfStock":
        name_of_gift = command[1]
        while name_of_gift in list_of_gifts:
            gift_index = list_of_gifts.index(name_of_gift)
            list_of_gifts[gift_index] = "None"

    elif command[0] == "Required":
        searched_index = int(command[2])
        new_gift = command[1]
        if len(list_of_gifts) >= searched_index:
            list_of_gifts[searched_index] = new_gift

    elif command[0] == "JustInCase":
        final_gift = command[1]
        list_of_gifts[-1] = final_gift

while "None" in list_of_gifts:
    list_of_gifts.remove("None")

print(*list_of_gifts)
