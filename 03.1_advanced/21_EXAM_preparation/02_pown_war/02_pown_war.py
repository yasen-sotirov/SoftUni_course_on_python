



# check if pawn reach the end
# print the result

matrix = []
board_size = 8
w_row, w_col, b_row, b_col = 0, 0, 0, 0

# create board
for row in range(board_size):
    matrix.append(input().split())

    # locate pawns coordinates
    if "w" in matrix[row]:
        w_row, w_col = row, matrix[row].index("w")
    elif "b" in matrix[row]:
        b_row, b_col = row, matrix[row].index("b")


while True:
    # White
    # check if there is a collision
    if (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col):
        print(f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row - 8)}.")
        break
    else:
        w_row -= 1

    # define borders for the pawns
    if w_row == -1:
        print(f"Game over! White pawn is promoted to a queen at {chr(97+ w_col)}8.")
        break

    # Black
    # check if there is a collision
    if (b_row + 1, b_col - 1) == (w_row, w_col) and (b_row - 1, b_col + 1) == (w_row, w_col):
        print(f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row - 8)}.")
        break
    else:
        b_row += 1

    # define borders for the pawns
    if b_row == 8:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
        break









