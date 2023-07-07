def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == "END":
        break

    command = line.split()

    if not command[0] == "swap" or not len(command) == 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_outside(row1, col1, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')
