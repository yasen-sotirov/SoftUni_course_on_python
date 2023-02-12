""" 3.	2x2 Squares in Matrix
Find the number of all 2x2 squares containing identical chars in a matrix.
On the first line, you will receive the matrix's dimensions in the format
"{rows} {columns}". On the following rows, you will receive characters separated
by a single space. Print the number of all square matrices you have found.

    Examples
    Input
3 4
A B B D
E B B B
I J B B

    Output
2
"""


rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)
