number_of_floors = int(input())
flat_per_floor = int(input())

flat_number = 0
flat_name = ''

for floor in range(number_of_floors, 0, -1):
    for apartment in range(flat_per_floor):
        if floor == number_of_floors:
            flat_name = f'L{floor}{apartment}'
        elif floor % 2 != 0:
            flat_name = f'A{floor}{apartment}'
        elif floor % 2 == 0:
            flat_name = f'O{floor}{apartment}'

        print(flat_name, end=' ')
    print()
