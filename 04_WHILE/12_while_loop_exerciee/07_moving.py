length = int(input())
width = int(input())
height = int(input())
space_is_full = False
total_space = length * width * height
command = input()

while command != "Done":
    number_of_boxes = int(command)
    total_space -= number_of_boxes
    if total_space < 0:
        space_is_full = True
        break
    command = input()

if space_is_full:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
else:
    print(f"{total_space} Cubic meters left.")
