length = float(input())
height = float(input())

length_in_cm = length * 100
height_in_cm = height * 100 - 100

number_of_columns = length_in_cm // 120
desks_per_column = height_in_cm // 70

total_desks = number_of_columns * desks_per_column - 3

print(int(total_desks))