from collections import deque

liters = int(input())
line = deque()
name = input()

while not name == 'Start':
    line.append(name)
    name = input()

command = input()

while not command == 'End':
    if command.isdigit():
        require_liters = int(command)
        name = line.popleft()
        if liters >= require_liters:
            liters -= require_liters
            print(f'{name} got water')
        else:
            print(f'{name} must wait')

    else:
        _, liters_to_fill = command.split()
        liters_to_fill = int(liters_to_fill)
        liters += liters_to_fill

    command = input()
print(f'{liters} liters left')
