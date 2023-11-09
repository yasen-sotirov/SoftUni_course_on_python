from math import floor


def check_index(index):
    if index >= size:
        index = 0
    elif index < 0:
        index = size - 1
    return index


size = int(input())
player_position = ()
matrix = []
movement = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
coins = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    if "P" in data:
        player_position = (row, data.index("P"))
        matrix[row][player_position[1]] = 0

path_tracker = [player_position]
while True:
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    directions = input()
    if directions not in movement:
        continue

    row_index = player_position[0] + movement[directions][0]
    next_row = check_index(row_index)
    col_index = player_position[1] + movement[directions][1]
    next_col = check_index(col_index)

    path_tracker.append((next_row, next_col))
    player_position = (next_row, next_col)
    position = matrix[next_row][next_col]

    if position == "X":
        print(f"Game over! You've collected {floor(coins / 2)} coins.")
        break

    else:
        coins += int(position)
        matrix[next_row][next_col] = 0

print("Your path: ")
for el in path_tracker:
    print(f"[{el[0]}, {el[1]}]")


