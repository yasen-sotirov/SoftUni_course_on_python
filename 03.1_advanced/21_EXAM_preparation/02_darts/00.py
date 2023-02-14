from collections import deque

matrix_size = 7
players = deque(input().split(", "))
# contains player, start points, and hits counter
player_dict = {}
# filling the dictionary
for player in players:
    player_dict[player] = [501, 0]

matrix = []
# filling the matrix
for row in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)


def is_valid(index):
    if 0 <= index < matrix_size:
        return True


def sum_corners(row_index, col_index):
    # we are getting the four ends of a cross like figure:
    left = matrix[row_index][0]
    right = matrix[row_index][matrix_size - 1]
    up = matrix[0][col_index]
    down = matrix[matrix_size - 1][col_index]
    # sum the four values, but before that convert them into integers
    result = sum([int(x) for x in (left, right, up, down)])
    return result


while True:
    # getting the current player from the queue
    current_player = players[0]
    # getting the current coordinates from string(input)
    row, col = (int(x) for x in input()[1:-1].split(", "))
    # increasing the current player tries by one
    player_dict[current_player][1] += 1
    # testing if the coordinates are inside the matrix
    if is_valid(row) and is_valid(col):
        # getting the value of the current coordinates
        current_hit = matrix[row][col]
        if current_hit == "D":  # D for double
            player_dict[current_player][0] -= sum_corners(row, col) * 2
        elif current_hit == "T":  # T for triple
            player_dict[current_player][0] -= sum_corners(row, col) * 3
        elif current_hit == "B":  # B for bullseye
            print(f"{current_player} won the game with {player_dict[current_player][1]} throws!")
            break
        else:
            # decrease the points of the current player from 501 to 0 or below
            player_dict[current_player][0] -= int(current_hit)
    if player_dict[current_player][0] <= 0:
        print(f"{current_player} won the game with {player_dict[current_player][1]} throws!")
        break
    # rotate the queue
    players.rotate()


