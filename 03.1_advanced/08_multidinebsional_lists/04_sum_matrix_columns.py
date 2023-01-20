""" 4.	Sum Matrix Columns
Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows,
you will get elements for each column separated with a single space.

    Examples
    Input
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

    Output
12
10
19
20
8
7
"""

n_rows, n_cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(n_rows):
    matrix.append([int(el) for el in input().split()])

for col in range(n_cols):
    current_sum = 0
    for row in range(n_rows):
        current_sum += matrix[row][col]

    print(current_sum)
