""" 4.	Maximal Sum
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square
with a maximum sum of its elements. There will be no case with two or more 3x3 squares
with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in the format
    "{rows} {columns}" – integers in the range [1, 20]
•	On the following lines, you will receive each row with its columns -
    integers, separated by a single space in the range [-20, 20]

Output
•	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
•	On the following 3 lines, print each element of the found submatrix, separated by a single space

    Examples
    Input
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4

    Output
Sum = 75
1 4 14
7 11 2
8 12 16
"""


rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = 0
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row, best_col = row, col

print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")
