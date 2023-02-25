command = input()
stock_dict = {}

while not command == 'buy':
    name, price, quantity = command.split(" ")

    if name not in stock_dict.keys():
        stock_dict[name] = [0.00, 0]
    stock_dict[name][0] = float(price)
    stock_dict[name][1] += int(quantity)

    command = input()

for key, value in stock_dict.items():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")
