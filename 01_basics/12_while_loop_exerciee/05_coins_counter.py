change = float(input())
change = int(change * 100)
coin_counter = 0

coin_counter += change // 200
change %= 200
coin_counter += change // 100
change %= 100
coin_counter += change // 50
change %= 50
coin_counter += change // 20
change %= 20
coin_counter += change // 10
change %= 10
coin_counter += change // 5
change %= 5
coin_counter += change // 2
change %= 2
coin_counter += change // 1
change %= 1

print(coin_counter)