from math import floor, ceil
flower_1 = int(input())
flower_2 = int(input())
flower_3 = int(input())
flower_4 = int(input())
gift_price = int(input())

income_flower_1 = flower_1 * 3.25
income_flower_2 = flower_2 * 4
income_flower_3 = flower_3 * 3.5
income_flower_4 = flower_4 * 8


total_income = (income_flower_1 + income_flower_2 + income_flower_3 + income_flower_4) * 0.95
difference = abs(gift_price - total_income)

if total_income >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
