percentage_fats = int(input())
percentage_proteins = int(input())
percentage_carbs = int(input())
total_amount_calories = int(input())
percentage_water = int(input())

grams_from_fats = (total_amount_calories * percentage_fats / 100) / 9
grams_from_proteins = (total_amount_calories * percentage_proteins / 100) / 4
grams_from_carbs = (total_amount_calories * percentage_carbs / 100) / 4

total_food_weight = grams_from_fats + grams_from_proteins + grams_from_carbs
calories_per_gram_food = total_amount_calories / total_food_weight

i = (100 - percentage_water) / 100
real_calories = calories_per_gram_food * i

print(f'{real_calories:.4f}')
