number_of_lines = int(input())
tank_capacity = 255
water_counter = 0

for current_lines in range(number_of_lines):
    added_liters = int(input())
    if added_liters > tank_capacity:
        print("Insufficient capacity!")
        continue
    tank_capacity -= added_liters
    water_counter += added_liters
print(water_counter)


