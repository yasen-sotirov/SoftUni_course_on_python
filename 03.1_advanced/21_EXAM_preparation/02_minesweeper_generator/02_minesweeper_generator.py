def is_valid(index):
    if -1 < index < mine_field_size:
        return True


def check_directions(row_idx, col_idx):
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    counter = 0
    for direction in directions:
        next_row = row_idx + direction[0]
        next_col = col_idx + direction[1]
        if is_valid(next_row) and is_valid(next_col):
            if matrix[next_row][next_col] == "*":
                counter += 1
    return counter


mine_field_size = int(input())
number_of_bombs = int(input())

matrix = [[0] * mine_field_size for row in range(mine_field_size)]

for _ in range(number_of_bombs):
    line = input()[1:-1].split(', ')
    row, col = [int(x) for x in line]
    matrix[row][col] = "*"

for row in range(mine_field_size):
    for col in range(mine_field_size):
        current_position = matrix[row][col]
        if current_position != "*":
            matrix[row][col] = check_directions(row, col)

for row in matrix:
    print(' '.join([str(x) for x in row]))

