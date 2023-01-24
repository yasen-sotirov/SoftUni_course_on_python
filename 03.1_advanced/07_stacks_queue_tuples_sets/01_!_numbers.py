first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command_line = input().split()
    command = command_line[0]
    argument = command_line[1]

    if command == "Add":
        if argument == "First":
            [first.add(int(x)) for x in command_line[2:]]
        else:
            [second.add(int(x)) for x in command_line[2:]]

    elif command == "Remove":
        if argument == "First":
            first = first.difference([int(x) for x in command_line[2:]])
        else:
            second = second.difference([int(x) for x in command_line[2:]])

    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
