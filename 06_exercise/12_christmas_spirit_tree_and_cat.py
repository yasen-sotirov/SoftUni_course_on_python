quantity = int(input())
days_left = int(input())
budget = 0
spirit = 0

ornament_set_price = 2
ornament_set_spirit = 5

skirt_price = 5
skirt_spirit = 3

garland_price = 3
garland_spirit = 10

lights_price = 15
lights_spirit = 17

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        budget += ornament_set_price * quantity
        spirit += ornament_set_spirit
    if current_day % 3 == 0:
        budget += (skirt_price + garland_price) * quantity
        spirit += skirt_spirit + garland_spirit
    if current_day % 5 == 0:
        budget += lights_price * quantity
        spirit += lights_spirit
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        budget += skirt_price + garland_price + lights_price
if days_left % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
