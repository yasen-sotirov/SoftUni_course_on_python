month = input()
number_of_nights = int(input())

price_per_night = 0
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < number_of_nights < 14:
        studio *= 0.95
    elif 14 < number_of_nights:
        studio *= 0.7
        apartment *= 0.9

elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if 14 < number_of_nights:
        studio *= 0.8
        apartment *= 0.9

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if 14 < number_of_nights:
        apartment *= 0.9

total_price_for_apartment = number_of_nights * apartment
total_price_for_studio = number_of_nights * studio

print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")
