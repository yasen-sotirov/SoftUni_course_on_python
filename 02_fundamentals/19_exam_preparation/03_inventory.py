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
