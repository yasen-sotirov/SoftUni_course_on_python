
num_rows, num_cols = [int(x) for x in input().split()]
playground = []
row_old = 0
col_old = 0
touched_players = 0
moves_counter = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


for row in range(num_rows):
    current_row = input().split()
    playground.append(current_row)
    if "B" in current_row:
        row_old = row
        col_old = current_row.index("B")


while touched_players != 3:
    command = input()
    if command == "Finish":
        break

    row, col = directions[command]
    next_row = row_old + row
    if next_row < 0:
        next_row = 0
    elif next_row == num_rows:
        next_row = num_rows - 1

    next_col = col_old + col
    if next_col < 0:
        next_col = 0
    elif next_col == num_cols:
        next_col = num_cols - 1

    if playground[next_row][next_col] == "O":
        continue

    if playground[next_row][next_col] == "P":
        touched_players += 1
        moves_counter += 1
    elif playground[next_row][next_col] == "-":
        if not row_old == next_row and not col_old == next_col:
            moves_counter += 1

    playground[next_row][next_col] = "B"
    playground[row_old][col_old] = "-"

    row_old = next_row
    col_old = next_col

    # print()
    # for row in playground:
    #     print(' '.join([str(x) for x in row]))

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_counter}")

