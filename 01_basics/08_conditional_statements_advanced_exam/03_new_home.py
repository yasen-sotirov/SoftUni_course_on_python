type_of_flower = input()
number_of_flower = int(input())
budget = int(input())
price_per_flower = 0

if type_of_flower == 'Roses':
    price_per_flower = 5
    if number_of_flower > 80:
        price_per_flower *= 0.9

elif type_of_flower == 'Dahlias':
    price_per_flower = 3.80
    if number_of_flower > 90:
        price_per_flower *= 0.85

elif type_of_flower == 'Tulips':
    price_per_flower = 2.80
    if number_of_flower > 80:
        price_per_flower *= 0.85

elif type_of_flower == 'Narcissus':
    price_per_flower = 3.00
    if number_of_flower < 120:
        price_per_flower *= 1.15

elif type_of_flower == 'Gladiolus':
    price_per_flower = 2.50
    if number_of_flower < 80:
        price_per_flower *= 1.20

total_sum = number_of_flower * price_per_flower
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flower} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
