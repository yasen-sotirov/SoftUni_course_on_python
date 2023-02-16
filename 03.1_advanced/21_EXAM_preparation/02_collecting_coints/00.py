matrix_size = int(input())
field = []
player_position = ()
for row in range(matrix_size):
    current_row = input().split()
    field.append(current_row)
    if "P" in current_row:
        player_position = (row, current_row.index("P"))
        field[row][player_position[1]] = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
collected_coins = 0


def check_index(index):
    if index >= matrix_size:
        index = 0
    elif index < 0:
        index = matrix_size - 1
    return index


path = [player_position]
wall_hit = False
win = False
while True:

    direction = input()
    if direction not in directions:
        continue

    next_row = player_position[0] + directions[direction][0]
    next_row = check_index(next_row)
    next_col = player_position[1] + directions[direction][1]
    next_col = check_index(next_col)
    next_position = field[next_row][next_col]
    path.append((next_row, next_col))
    player_position = (next_row, next_col)
    if next_position == "X":
        collected_coins //= 2
        break
    else:
        collected_coins += int(next_position)
        field[next_row][next_col] = 0
        if collected_coins >= 100:
            win = True
            break

if win:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")
print("Your path:")
for element in path:
    print(f"[{element[0]}, {element[1]}]")