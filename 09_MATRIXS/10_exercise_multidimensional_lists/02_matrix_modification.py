size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    action = command[0]
    row, col, value = [int(el) for el in command[1:]]

    if 0 > row or row >= size or 0 > col or col >= size:
        print("Invalid coordinates")
        continue        # ПРОПУСКА НЕВАЛИДНАТА КОМАНДА

    if action == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for el in matrix:
    print(*el, sep=" ")
