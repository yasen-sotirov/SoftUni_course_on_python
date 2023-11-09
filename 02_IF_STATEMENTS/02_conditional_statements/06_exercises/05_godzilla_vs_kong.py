budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())
all_dress_price = one_dress_price * number_of_statists

if number_of_statists > 150:
    all_dress_price *= 0.9

decor = budget * 0.1
needed_money = all_dress_price + decor
difference = abs(budget - needed_money)

if budget < needed_money:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")



