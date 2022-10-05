from math import ceil, floor

number_of_days = int(input())
kg_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

total_needed_food = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * number_of_days
difference = abs(kg_food - total_needed_food)

if total_needed_food <= kg_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f'{ceil(difference)} more kilos of food are needed.')
