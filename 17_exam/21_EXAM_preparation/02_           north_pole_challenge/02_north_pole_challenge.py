# read, print matrix
# locate start coordinates
# count all items in the field
# track collected items
# define movements
# mark used parth
# print result


rows, cols = [int(x) for x in input().split(', ')]
matrix = []
row_position = 0
col_position = 0
all_items = 0

items_list = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}
movement = {
    "up": lambda x, y: ((x-1), y),
    "down": lambda x, y: ((x+1), y),
    "left": lambda x, y: (x, (y-1)),
    "right": lambda x, y: (x, (y+1))
}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        position_in_matrix = matrix[row][col]
        if position_in_matrix == "Y":
            row_position = row
            col_position = col
        elif position_in_matrix == "D":
            all_items += 1
        elif position_in_matrix == "G":
            all_items += 1
        elif position_in_matrix == "C":
            all_items += 1

while True:
    command = input()
    if command == "End" or all_items == 0:
        break

    direction, steps = command.split("-")
    for current_move in range(int(steps)):
        matrix[row_position][col_position] = "x"
        new_position = movement[direction](row_position, col_position)
        row_position = new_position[0]
        col_position = new_position[1]

        if matrix[row_position][col_position] == "D":
            items_list["Christmas decorations"] += 1
            all_items -= 1
        elif matrix[row_position][col_position] == "G":
            items_list["Gifts"] += 1
            all_items -= 1
        elif matrix[row_position][col_position] == "C":
            items_list["Cookies"] += 1
            all_items -= 1
        matrix[row_position][col_position] = "Y"

if all_items == 0:
    print("Merry Christmas!")

for item, number in items_list.items():
    print(f"- {number} {item}")

for row in matrix:
    print(' '.join(row))
