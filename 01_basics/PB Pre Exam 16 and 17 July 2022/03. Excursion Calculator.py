number_of_people = int(input())
season = input()
price_per_person = 0

if season == 'spring':
    if number_of_people <= 5:
        price_per_person = 50
    else:
        price_per_person = 48
elif season == 'summer':
    if number_of_people <= 5:
        price_per_person = 48.50 * 0.85
    else:
        price_per_person = 45 * 0.85
elif season == 'autumn':
    if number_of_people <= 5:
        price_per_person = 60
    else:
        price_per_person = 49.50
elif season == 'winter':
    if number_of_people <= 5:
        price_per_person = 86 * 1.08
    else:
        price_per_person = 85 * 1.08

total_price = number_of_people * price_per_person
print(f"{total_price:.2f} leva.")
