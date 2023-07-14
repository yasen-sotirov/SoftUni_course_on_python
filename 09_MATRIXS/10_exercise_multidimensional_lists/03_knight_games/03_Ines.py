n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))


def is_valid_boundary(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, 1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if is_valid_boundary(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == "K":
                kills += 1
    return kills


for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == "K":
            kills = calculate_kills(matrix, row_index, col_index)

