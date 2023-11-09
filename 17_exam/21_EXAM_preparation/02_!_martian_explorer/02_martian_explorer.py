from collections import deque


def is_outside(index, border):
    if index < 0:
        index = border - 1
    elif index == border:
        index = 0
    return index

size = 6
field = []
position = [0, 0]
deposits_found = set()
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
deposit = {"W": "Water", "M": "Metal", "C": "Concrete"}

for row in range(size):
    current_row = input().split()
    field.append(current_row)
    if "E" in current_row:
        position = [row, current_row.index("E")]

commands = deque(input().split(", "))

while commands:
    row, col = directions[commands.popleft()]
    next_row = position[0] + row
    next_row = is_outside(next_row, size)
    next_col = position[1] + col
    next_col = is_outside(next_col, size)

    current_position = field[next_row][next_col]
    if current_position == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    if current_position in deposit:
        print(f"{deposit[current_position]} deposit found at ({next_row}, {next_col})")
        deposits_found.add(deposit[current_position])
    position = [next_row, next_col]

if len(deposits_found) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")






