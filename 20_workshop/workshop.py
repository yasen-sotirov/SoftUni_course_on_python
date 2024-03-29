# TODO define winning conditions


class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(ma):
    # print matrix
    for el in ma:
        print(el)


def validate_colum_choice(selected_column_num, max_column_index):
    # verify player choice of number - if not ask again
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_column_index, player_num):
    # place player marker ot the spot.
    # check if the column is full if so - trow error.
    rows_count = len(ma)
    for row_index in range(rows_count - 1, - 1, - 1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = player_num
            return row_index, selected_column_index
    raise FullColumnError


def is_player_num(ma, row, col, player_num):  # if is out of range
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, player_num, slots_count):
    """
    We check in both sides, because we can have input like this:
    1
    1
    2
    2
    4
    4
    3
    Also we have to check this condition:
    1
    1
    2
    2
    5
    5
    6
    6
    7
    7
    3
    [T, T, T, F, T, T, T] - this in not a winner
    """
    right = []
    for index in range(slots_count):
        if is_player_num(ma, row, col+index, player_num):
            right.append(True)
        else:
            break

    left = []
    for index in range(slots_count):
        if is_player_num(ma, row, col-index, player_num):
            left.append(True)
        else:
            break

    # count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    # count_left = [is_player_num(ma, row, col - index, player_num) for index in range(slots_count)].count(True)
    # TODO handle exception case
    # It should be strict ">" because we are counting the current element sa well
    return (len(right) + len(left)) > slots_count


def is_right_diagonal(ma, row, col, player_num, slots_count):
    """
    We check for both (up right, left down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    right_up_count = [is_player_num(ma, row-index, col+index, player_num) for index in range(slots_count)].count(True)
    left_down_count = [is_player_num(ma, row+index, col-index, player_num) for index in range(slots_count)].count(True)
    return (right_up_count + left_down_count) > slots_count


def is_left_diagonal(ma, row, col, player_num, slots_count):
    """
    We check for both (up left, right down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    left_up_count = [is_player_num(ma, row-index, col-index, player_num) for index in range(slots_count)].count(True)
    right_down_count = [is_player_num(ma, row+index, col+index, player_num) for index in range(slots_count)].count(True)
    return (left_up_count + right_down_count) > slots_count


def is_winner(ma, row, col, player_num, slots_count=4):
    """
    We check for horizontal (both sides)
    Only down (because we fill the matrix from bottom to top)
    Check for right and left diagonal
    """
    is_down = all([is_player_num(ma, row + index, col, player_num) for index in range(slots_count)])
    if any(
            [
                is_horizontal(ma, row, col, player_num, slots_count),
                is_down,
                is_left_diagonal(ma, row, col, player_num, slots_count),
                is_right_diagonal(ma, row, col, player_num, slots_count),
            ]
    ):
        return True
    return False


rows_count = 6
cols_count = 7

# create matrix
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]

# print initial board
print_matrix(matrix)

player_num = 1
while True:
    # decide correct player num (only 1 and 2 is possible - 2 players)
    player_num = 2 if player_num % 2 == 0 else 1  # parity

    # read column choice from input
    try:
        colum_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_colum_choice(colum_num, cols_count - 1)
        row, col = place_player_choice(matrix, colum_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}!")
            break

        print_matrix(matrix)
        print()

    except InvalidColumnError:
        # not in range of game 1 - 7
        print(f"This column is not valid. Please select a "
              f"number between {1} and {cols_count}.")
        continue

    except ValueError:
        # not a valid number
        print(f"Please select a valid digit")
        continue  # връща ни в начало на while

    except FullColumnError:
        # this is full column
        print(f"This column is already full! "
              f"Please select another column number!")
        continue

    # only if the turn was successful, we go to the next player
    player_num += 1
