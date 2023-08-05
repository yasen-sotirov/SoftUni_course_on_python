from collections import deque

# check players turn
# check is valid hit
# read points on border
# check multiplication of score

# read input data
players_data = input()       # read players


players_points = {}
for player in players_data.split(", "):
    players_points[player] = [501, 0]

size_matrix = 7         # create matrix
dartboard = []
for row in range(size_matrix):
    current_row = input().split()
    dartboard.append([int(x) if x.isdigit() else x for x in current_row])  # read dartboard


def is_valid(board_row, board_col):
    if board_row < 0 or board_row >= size_matrix or board_col < 0 or board_col >= size_matrix:
        return False
    return True


def sum_points(board_row, board_col):
    left = int(dartboard[board_row][0])
    right = int(dartboard[board_row][size_matrix-1])
    up = int(dartboard[0][board_col])
    down = int(dartboard[size_matrix-1][board_col])
    return left + right + up + down


while True:
    turn = deque(players_data.split(', '))
    current_player = turn.popleft()
    coordinates = input().strip("()")
    row, col = [int(x) for x in coordinates.split(", ")]

    if is_valid(row, col):
        hit = dartboard[row][col]
        players_points[current_player][1] += 1
        current_points = sum_points(row, col)

        if hit == "D":
            players_points[current_player][0] -= current_points * 2
        elif hit == "T":
            players_points[current_player][0] -= current_points * 3
        elif hit == "B":
            print(f"{current_player} won the game with {players_points[current_player][1]} throws!")
            break
        else:
            players_points[current_player][0] -= hit
    else:
        continue

    if players_points[current_player][0] <= 0:
        print(f"{current_player} won the game with {players_points[current_player][1]} throws!")
        break
    else:
        turn.append(current_player)

