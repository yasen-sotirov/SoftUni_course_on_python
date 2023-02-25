def shop_from_grocery_list(budget, grocery_list, *args):
    bought_items = []

    for el in args:
        product_name = el[0]
        product_price = el[1]

        for product in grocery_list:
            if product_name == product:
                if product_name not in bought_items:
                    product_price = float(product_price)
                    if budget >= product_price:
                        budget -= product_price
                        bought_items.append(product_name)
                        grocery_list.remove(product_name)
                    else:
                        break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.02f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
