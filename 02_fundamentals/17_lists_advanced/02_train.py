number_of_wagon = int(input())
command = input()
train = [0] * number_of_wagon

while not command == "End":
    data = command.split()
    if data[0] == 'add':
        train[-1] += int(data[1])
    elif data[0] == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])

    command = input()