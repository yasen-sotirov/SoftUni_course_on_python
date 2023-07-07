def read_matrix(rows):
    matrix = []
    for row in range(rows):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


def get_submatrix_sum(sub_matrix):
    submatr_sum = 0
    for row in sub_matrix:
        submatr_sum += sum(row)
    return submatr_sum


def get_submatrix(matrix, submatrix_size, start_row_index, start_col_index):
    submatrix = []
    for row in range(start_row_index, start_row_index + submatrix_size):
        if row < len(matrix) and (start_col_index + submatrix_size) <= len(matrix[0]):
            submatrix.append(matrix[row][start_col_index:start_col_index + submatrix_size])
    # print(submatrix)
    return submatrix


def print_output(matrix, m_sum):
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    print(m_sum)


SUBMATRIX_SIZE = 2
rows, cols = map(int, input().split(', '))
matrix = read_matrix(rows)

max_sub_matrix = get_submatrix(matrix, SUBMATRIX_SIZE, 0, 0)
max_sum = get_submatrix_sum(max_sub_matrix)

for row in range(rows - SUBMATRIX_SIZE + 1):
    for col in range(cols - SUBMATRIX_SIZE + 1):
        submatrix = get_submatrix(matrix, SUBMATRIX_SIZE, row, col)
        current_sum = get_submatrix_sum(submatrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = submatrix

print_output(max_sub_matrix, max_sum)
