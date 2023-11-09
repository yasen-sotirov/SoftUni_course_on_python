"""
3.	Knight Game
Chess is the oldest game, but it is still popular these days.
It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated.
It can move to the nearest square but not on the same row, column,
or diagonal. (e.g., it can move two squares horizontally,
then one square vertically, or it can move one square horizontally
then two squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells.
Your task is to remove knights until no knights that can attack one
another with one move are left.
Always remove the knight who can attack the greatest number of knights.
If there are two or more knights with the same number of attacks,
remove the top-left one.

Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"

Output
•	Print a single integer with the number of knights that need to be removed.

Constraints
•	The size of the board will be 0 < N < 30
•	Time limit: 0.3 sec. Memory limit: 16 MB

Examples

Input
5
0K0K0
K000K
00K00
K000K
0K0K0

Output
1
===

Input
2
KK
KK

Output
0
===

Input
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK

Output
12
"""


rows = int(int(input()))
pos_knights = []
matrix = []
total_knights = [0]

for row in range(rows):
    matrix.append(list(input()))
    for col in range(len(matrix[0])):
        if matrix[row][col] == "K":
            pos_knights.append([row, col])

cols = len(matrix[0])


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


movement = {
    "up left": [-2, -1], "up right": [-2, 1],
    "down left": [2, -1], "down right": [2, 1],
    "left up": [-1, -2], "left down": [1, -2],
    "right up": [-1, 2], "right down": [1, 2],
}


def check_knights():
    result = {}
    for row, col in pos_knights:
        for m_row, m_col in movement.values():
            knight_row, knight_col = row + m_row, col + m_col
            if check_valid_index(knight_row, knight_col) and matrix[knight_row][knight_col] == "K":

                b = result.get(f"{row} {col}", 0) + 1
                result[f"{row} {col}"] = 1
    if not result:
        return
    total_knights[0] += 1
    row, col = [int(x) for x in max(result, key=result.get).split()]
    matrix[row][col] = "0"
    pos_knights.remove([row, col])
    check_knights()


check_knights()
print(total_knights[0])
