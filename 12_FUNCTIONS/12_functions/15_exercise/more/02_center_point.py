from math import floor


def nearest_point(x_1, y_1, x_2, y_2):
    point_1 = abs(x_1) + abs(y_1)
    point_2 = abs(x_2) + abs(y_2)
    if point_1 < point_2:
        return f"({floor(x_1)}, {floor(y_1)})"
    return f"({floor(x_2)}, {floor(y_2)})"


num_x_1 = float(input())
num_y_1 = float(input())
num_x_2 = float(input())
num_y_2 = float(input())

print(nearest_point(num_x_1, num_y_1, num_x_2, num_y_2))
