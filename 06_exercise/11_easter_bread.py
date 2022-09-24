budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
bread_price = flour_price + eggs_price + milk_price

bread_counter = 0
colored_eggs_counter = 0

while budget >= bread_price:
    budget -= bread_price
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! "
      f"Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
