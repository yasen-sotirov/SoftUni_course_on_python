
data = input().split('#')
water_amount = int(input())
effort = 0
list_of_cells = []
total_fire = 0
ran_out_water = False

for current_cell in data:
    fire_level, cell_value = current_cell.split(' = ')
    cell_value = int(cell_value)
    if fire_level == 'High':
        if 81 <= cell_value <= 125:
            if water_amount >= cell_value:
                water_amount -= cell_value
                effort += int(cell_value) * 0.25
                list_of_cells.append(f'- {cell_value}')
                total_fire += cell_value
                if water_amount == 0:
                    ran_out_water = True
                    break
            else:
                continue

    elif fire_level == 'Medium':
        if 51 <= cell_value <= 80:
            if water_amount >= cell_value:
                water_amount -= cell_value
                effort += int(cell_value) * 0.25
                list_of_cells.append(f'- {cell_value}')
                total_fire += cell_value
                if water_amount == 0:
                    ran_out_water = True
                    break
            else:
                continue

    else:
        if 1 <= cell_value <= 50:
            if water_amount >= cell_value:
                water_amount -= cell_value
                effort += int(cell_value) * 0.25
                list_of_cells.append(f'- {cell_value}')
                total_fire += cell_value
                if water_amount == 0:
                    ran_out_water = True
                    break
            else:
                continue

print('Cells:')
print('\n'.join(list_of_cells))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
