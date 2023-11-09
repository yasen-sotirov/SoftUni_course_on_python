def is_inside(rows, cols, matrix_size):
    return 0 <= rows < matrix_size and 0 <= cols < matrix_size  # Връща True ако отговаря на условието


def is_knight(row, col, matrix):
    return matrix[row][col] == "K"


def get_attack_counter(row, col, matrix):
    result = 0
        # row - 2, col - 1
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    # row - 2, col + 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    # row - 1, col - 2
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    # row - 1, col + 2
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    # row + 2, col - 1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    # row + 2, col + 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    # row + 1, col - 2
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    # row + 1, col + 2
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1

    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = get_attack_counter(row, col, matrix)
            table[row][col] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coards, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coards[0]
            knight_col = coards[1]
    print()
    matrix[knight_row][knight_col] = '0'

print(table)