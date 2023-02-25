""" 6.	Symbol in Matrix
Write a program that reads a number - N, representing the rows and columns of a square matrix.
On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix
and print its position in the format: "({row}, {col})". You should start searching from the top left.
If there is no such symbol, print the message "{symbol} does not occur in the matrix".

    Examples
    Input
3
ABC
DEF
X!@
!

    Output
(2, 1)
"""


n = int(input())
matrix = []
position = None

for row in range(n):
    matrix.append(list(input()))

symbol = input()
symbol_is_found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")
