""" 5.	Primary Diagonal
Write a program that finds the sum of all numbers in a matrix's primary diagonal
(runs from top left to bottom right). On the first line,
you will receive an integer N – the size of a square matrix.
The next N lines holds the values for each column - N numbers,
separated by a single space.
"""

n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split()])

result = 0

for row in range(n):
    for col in range(n):
        if row == col:
            result += matrix[row][col]

print(result)
