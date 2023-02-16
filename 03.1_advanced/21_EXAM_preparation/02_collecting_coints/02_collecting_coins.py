from math import floor


def check_index(index):
    if index >= size:
        index = 0
    elif index < 0:
        index = size - 1
    return index


size = int(input())
player_position = (0, 0)
matrix = []
movement = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
counter = 0
path_tracker = []

for row in range(size):
    data = input().split()
    matrix.append(data)
    if "P" in data:
        player_position = (row, data.index("P"))


while True:
    if counter >= 100:
        break

    directions = input()
    row_index = player_position[0] + movement[directions][0]
    next_row = check_index(row_index)
    col_index = player_position[1] + movement[directions][1]
    next_col = check_index(col_index)
    position = matrix[next_row][next_col]

    if position.isdigit():
        counter += int(position)
        matrix[next_row][next_col] = 0
    elif position == "X":
        print(f"Game over! You've collected {floor(counter/2)} coins.")


