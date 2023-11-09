from math import floor

line_1_x1 = float(input())
line_1_y1 = float(input())
line_1_x2 = float(input())
line_1_y2 = float(input())

line_2_x1 = float(input())
line_2_y1 = float(input())
line_2_x2 = float(input())
line_2_y2 = float(input())

first_line_p1 = abs(line_1_x1) + abs(line_1_y1)
first_line_p2 = abs(line_1_x2) + abs(line_1_y2)

second_line_p1 = abs(line_2_x1) + abs(line_2_y1)
second_line_p2 = abs(line_2_x2) + abs(line_2_y2)

if first_line_p1 > first_line_p2:
    first_line_length = first_line_p1 - first_line_p2
else:
    first_line_length = first_line_p2 - first_line_p1

if second_line_p2 > second_line_p2:
    second_line_length = second_line_p1 - second_line_p2
else:
    second_line_length = second_line_p2 - second_line_p1

if first_line_length <= second_line_length:
    print(f"({floor(line_1_x2)}, {floor(line_1_y2)})({floor(line_1_x1)}, {floor(line_1_y1)})")
else:
    print(f"({floor(line_2_x2)}, {floor(line_2_y2)})({floor(line_2_x1)}, {floor(line_2_y1)})")
