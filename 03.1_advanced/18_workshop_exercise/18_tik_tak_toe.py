
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


def instruction_board():
    print("\n"
          "This is numeration of the board: ")
    print("| 1 | 2 | 3 |\n"
          "| 4 | 5 | 6 |\n"
          "| 7 | 8 | 9 |\n")


first_player, second_player = read_player_name()
print(instruction_board())
print(f'{first_player.name} starts first!')


















