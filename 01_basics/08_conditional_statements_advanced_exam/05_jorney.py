budget = float(input())
season = input()

location = ''
type_of_vacation = ''
percentage_of_budget = 0


if budget <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        type_of_vacation = 'Camp'
        budget *= 0.3
    elif season == 'winter':
        type_of_vacation = 'Hotel'
        budget *= 0.7


elif budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        type_of_vacation = 'Camp'
        budget *= 0.4
    elif season == 'winter':
        type_of_vacation = 'Hotel'
        budget *= 0.8

else:
    location = 'Europe'
    type_of_vacation = 'Hotel'
    budget *= 0.9

print(f"Somewhere in {location}")
print(f"{type_of_vacation} - {budget:.2f}")
