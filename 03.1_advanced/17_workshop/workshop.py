# place player marker ot the spot - check if the column is full
# TODO define winning conditions


class InvalidColumnError(Exception):
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
    # TODO
    rows_count = len(ma)
    for row_index in range(rows_count - 1, - 1, - 1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = player_num
            return


rows_count = 6
cols_count = 7


# create matrix
matrix = [[0 for _ in range(cols_count)]for row_num in range(rows_count)]
print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1    # parity

    # read column choice from input
    try:
        colum_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_colum_choice(colum_num, cols_count - 1)
        place_player_choice(matrix, colum_num, player_num)
        print_matrix(matrix)
        print()

    except InvalidColumnError:
        print(f"This column is not valid. Please select a number between {1} and {cols_count}.")
        continue

    except ValueError:
        print(f"Please select a valid digit")
        continue        # връща ни в начало на while

    player_num += 1



