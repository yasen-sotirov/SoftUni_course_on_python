""" 8.	*Bombs
You will be given a square matrix of integers, each integer separated by a single space,
and each row will be on a new line. On the last line of input, you will receive indexes -
coordinates of several cells separated by a single space, in the following format:
"{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given.
When a bomb explodes, it deals damage equal to its integer value to all the cells around it
(in every direction and in all diagonals). One bomb can't explode more than once,
and after it does, its value becomes 0. When a cell's value reaches 0 or below,
it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all
its cells (including the dead ones).

Input
•	On the first line, you are given the integer N - the size of the square matrix.
•	The following N lines hold each column's values - N numbers separated by a space.
•	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.

Output
•	On the first line, you need to print the count of all alive cells in the format:
    "Alive cells: {alive_cells}"
•	On the second line, you need to print the sum of all alive cells in the format:
    "Sum: {sum_of_cells}"
•	In the end, print the matrix. A space must separate the cells.

Constraints
•	The size of the matrix will be between [0…1000].
•	The bomb coordinates will always be in the matrix.
•	The bomb's values will always be greater than 0.
•	The integers of the matrix will be in the range [1…10000].

    Examples
    Input
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0

    Output
Alive cells: 3
Sum: 12
8 -4 -5 -2
-3 -3 0 2
0 0 -4 -1
-3 -1 -1 2

    Comments
1) The bomb with value 7 will explode and reduce the values of the cells around it.
2) The bomb with coordinates 2,1 and value 9 will explode and reduce its neighbor cells.
3) The bomb with coordinates 2,0 and value 9 will explode.
After that, you have to print the count of the alive cells - 3, and their sum - 12. Print the matrix after the explosions.

"""


def is_inside_matrix(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbors(row, col, matrix):
    size = len(matrix)
    neighbors = []

    if is_inside_matrix(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbors.append([row - 1, col])

    if is_inside_matrix(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbors.append([row + 1, col])

    if is_inside_matrix(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbors.append([row, col - 1])

    if is_inside_matrix(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbors.append([row, col + 1])

    if is_inside_matrix(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbors.append([row - 1, col - 1])

    if is_inside_matrix(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbors.append([row - 1, col + 1])

    if is_inside_matrix(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbors.append([row + 1, col - 1])
    # row + 1, col + 1
    if is_inside_matrix(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbors.append([row + 1, col + 1])
    return neighbors


size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(el) for el in input().split()])

bombs_coordinates = input().split()

for current_bomb in range(len(bombs_coordinates)):
    bomb_row, bomb_col = [int(el) for el in bombs_coordinates[current_bomb].split(',')]
    if matrix[bomb_row][bomb_col] <= 0:
        continue

    power_of_bomb = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

    for row, col in get_neighbors(bomb_row, bomb_col, matrix):
        matrix[row][col] -= power_of_bomb

alive_cells = 0
alive_cells_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el


print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")

for row in matrix:
    print(*row, sep=' ')
