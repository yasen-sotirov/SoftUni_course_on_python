needed_money = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
total_sum = puzzle * 2.60 + \
            dolls * 3 + \
            bears * 4.10 + \
            minions * 8.20 + \
            trucks * 2.0
total_toys = puzzle + dolls + bears + minions + trucks
if total_toys >= 50:
    total_sum *= 0.75
total_sum *= 0.90
difference = abs(needed_money - total_sum)
if total_sum >= needed_money:
    print(f'Yes! {difference:.2F} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')