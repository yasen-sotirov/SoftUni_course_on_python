""" 2.	Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals
(absolute value).
 On the first line, you will receive an integer N - the size of a square matrix.
The following N lines hold the values for each column - N numbers separated by a single space.
Print the absolute difference between the primary and the secondary diagonal sums.

    Examples
    Input
3
11 2 4
4 5 6
10 8 -12

    Output
15
"""


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
