number_of_days = int(input())
type_of_room = input()
rating = input()
price_for_room = 0
discount = 0

if type_of_room == 'room for one person':
    price_for_room = 18
    discount = 1

elif type_of_room == 'apartment':
    price_for_room = 25
    if number_of_days < 10:
        discount = 0.7
    elif 10 <= number_of_days <= 15:
        discount = 0.65
    elif 15 < number_of_days:
        discount = 0.5

elif type_of_room == 'president apartment':
    price_for_room = 35
    if number_of_days < 10:
        discount = 0.9
    elif 10 <= number_of_days <= 15:
        discount = 0.85
    elif 15 < number_of_days:
        discount = 0.8

if rating == 'positive':
    discount *= 1.25
else:
    discount *= 0.9

number_of_nights = number_of_days - 1

final_price = number_of_nights * price_for_room * discount

print(f'{final_price:.2f}')
