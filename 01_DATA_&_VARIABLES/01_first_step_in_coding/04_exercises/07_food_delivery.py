chicken_meal = int(input()) * 10.35
fish_meal = int(input()) * 12.40
vegan_meal = int(input()) * 8.15
desert = (chicken_meal + fish_meal + vegan_meal) * 0.2
delivery_coast = 2.50
print(chicken_meal + fish_meal + vegan_meal + desert + delivery_coast)