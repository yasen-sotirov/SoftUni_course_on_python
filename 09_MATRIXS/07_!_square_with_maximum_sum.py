""" 7.	Square with Maximum Sum
Write a program that reads a matrix from the console and finds the 2x2 top-left
submatrix with biggest sum of its values.
On first line you will get matrix sizes in format "{rows}, {columns}".
On the next rows, you will get elements for each column,
separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements,
as shown in the examples.

    Examples
    Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0

    Output
9 8
7 9
33
"""


rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = 0
position = None

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col - 1] \
                      + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if current_sum >= max_sum:      # >= за да хване top left при [0, 0, 0],[0, 1, 0], [0, 0, 0]
            max_sum = current_sum
            position = (row, col)

row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(max_sum)
