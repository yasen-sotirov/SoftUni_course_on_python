t_shirt_price = float(input())
sum_for_bonus = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (t_shirt_price + shorts_price) * 2

total_price = (t_shirt_price + shorts_price + socks_price + shoes_price) * 0.85
difference = abs(total_price - sum_for_bonus)

if total_price >= sum_for_bonus:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
