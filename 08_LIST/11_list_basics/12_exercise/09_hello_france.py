"""" You want to go to France by train, and the train ticket costs exactly 150$.
You do not have enough money, so you decide to buy some items with your budget
and then sell them at a higher price – with a 40% markup.
You will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a specific price, which is given below:
Type	Maximum Price
Clothes	50.00
Shoes	35.00
Accessories	20.50
If a price for a particular item is higher than the maximum price, don't buy it.
Every time you buy an item, you have to reduce the budget with its price value.
If you don't have enough money for it, you can't buy it. Buy as many items as you can.
Next, you should increase the price of each item you have successfully bought by 40%
and then sell it. Calculate if the budget after selling all the items is enough for buying the ticket.
"""


items = input().split("|")
budget = float(input())
buy_list = []

for current_deal in items:
    current_item = current_deal.split("->")
    current_item_type = current_item[0]
    current_item_value = float(current_item[1])

    if current_item_type == 'Clothes' and current_item_value <= 50:
        if budget >= current_item_value:
            budget -= current_item_value
            buy_list.append(current_item_value)

    elif current_item_type == 'Shoes' and current_item_value <= 35:
        if budget >= current_item_value:
            budget -= current_item_value
            buy_list.append(current_item_value)

    elif current_item_type == 'Accessories' and current_item_value <= 20.50:
        if budget >= current_item_value:
            budget -= current_item_value
            buy_list.append(current_item_value)

sell_list = []
pure_profit = []

for current_selle in buy_list:
    current_selle_profit = current_selle * 1.4
    pure_profit.append(current_selle * 0.4)
    sell_list.append(current_selle_profit)

total_profit = sum(sell_list)
final_money = total_profit + budget

for price in sell_list:
    print(f"{price:.2f}", end=' ')
print()
print(f"Profit: {sum(pure_profit):.2f}")

if final_money >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")
