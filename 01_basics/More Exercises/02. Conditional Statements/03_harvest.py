from math import ceil, floor

vineyard = int(input())
grape_per_square_meter = float(input())
needed_liters_wine = int(input())
number_of_workers = int(input())

total_kg_grape = vineyard * grape_per_square_meter
total_wine = total_kg_grape * 0.4 / 2.5

difference = abs(needed_liters_wine - total_wine)
wine_per_worker = difference / number_of_workers

if needed_liters_wine <= total_wine:
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
