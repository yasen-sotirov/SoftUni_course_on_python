import pyfiglet
# read players signs
# print instruction board
# check order of players
# place players choice - validate if is correct
# check if is winner
# print art of winner's name


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_player_name():
    # read players names
    first_player_name = input(f"Player one name: ")
    second_player_name = input(f"Player two name: ")

    while True:
        first_player_sign = input(f'{first_player_name} wold you like to play with "X" ot "O"? ').upper()
        if first_player_sign == "X" or first_player_sign == "O":
            break

    second_player_sign = "O" if first_player_sign == "X" else "X"
    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def init_board():
    size = 3
    result = []
    for _ in range(size):
        result.append([None] * size)
    return result


def is_valid_position(board, board_mapper, position):
    if position < 1 or position > 9:
        return False
    row, col = board_mapper[position]
    return board[row][col] is None


def print_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join([x if x is not None else ' ' for x in row]), end='')
        print(' |')


def has_won(board, sign):
    # rows
    for row in board:
        if all([el == sign for el in row]):
            return True

    # cols
    for col in range(len(board)):
        col_won = True
        for row in range(len(board)):
            if board[row][col] != sign:
                col_won = False
                break
        if col_won:
            return True

    # diagonals
    left_diagonal = True
    right_diagonal = True
    for index in range(len(board)):
        if board[index][index] != sign:
            left_diagonal = False
        if board[index][len(board) - 1 -index] != sign:
            right_diagonal = False
    return left_diagonal or right_diagonal


def instruction_board():
    print("\n"
          "This is numeration of the board: ")
    print("| 7 | 8 | 9 |\n"
          "| 4 | 5 | 6 |\n"
          "| 1 | 2 | 3 |\n")

first_player, second_player = read_player_name()
print(instruction_board())
print(f'{first_player.name} starts first!')

board = init_board()
board_mapper = {
    7: [0, 0],
    8: [0, 1],
    9: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    1: [2, 0],
    2: [2, 1],
    3: [2, 2]
}
turn = 1

while True:
    current_player = first_player if turn % 2 != 0 else second_player
    print()
    position = int(input(f"{current_player.name} choose a free position [1-9]: "))

    if not is_valid_position(board, board_mapper, position):
        continue

    row, col = board_mapper[position]
    board[row][col] = current_player.sign

    print_board(board)

    if has_won(board, current_player.sign):
        print()
        result = pyfiglet.figlet_format(f"{current_player.name} WIN!")
        print(result)
        break

    turn += 1

















