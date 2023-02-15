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
    if row < 0 or row > size_matrix or col < 0 or col > size_matrix:
        return False


def sum_borders(board_row, board_col):
    left = int(dartboard[board_row][0])
    right = int(dartboard[board_row][size_matrix-1])
    up = int(dartboard[0][board_col])
    down = int(dartboard[size_matrix-1][board_col])
    return sum(left, right, up, down)


while True:
    turn = deque(players_data.split(', '))
    current_player = turn.popleft()
    row, col = (int(x) for x in input()[1:-1].split(", "))

    if is_valid(row, col):
        if dartboard[row][col] == "D":
            pass
    else:
        continue

    if players_points[current_player][0] <= 0:
        break
    else:
        turn.append(current_player)

