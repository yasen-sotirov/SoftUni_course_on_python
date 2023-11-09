list_of_coffee = input().split(" ")
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split(" ")

    if "Include" in command:
        action = command[0]
        coffee_name = command[1]
        list_of_coffee.append(coffee_name)

    elif "Remove" in command:
        action = command[0]
        position_in_list = command[1]
        coffee_to_remove = command[2]
        if not len(list_of_coffee) < int(coffee_to_remove):
            if "first" in position_in_list:
                for _ in range(int(coffee_to_remove)):
                    list_of_coffee.pop(0)
            elif "last" in position_in_list:
                for _ in range(int(coffee_to_remove)):
                    list_of_coffee.pop(- 1)

    elif "Prefer" in command:
        action = command[0]
        index_1 = int(command[1])
        index_2 = int(command[2])
        if len(list_of_coffee) >= index_1 and len(list_of_coffee) >= index_2:
            list_of_coffee[index_1], list_of_coffee[index_2] = list_of_coffee[index_2], list_of_coffee[index_1]

    elif "Reverse" in command:
        list_of_coffee.reverse()

print('Coffees: ')
print(" ".join(list_of_coffee))
