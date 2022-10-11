"""" Write a function that calculates the total price of an order
and returns it. The function should receive one of the following products:
"coffee", "coke", "water", or "snacks", and a quantity of the product.
The prices for a single piece of each product are:
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00
Print the result formatted to the second decimal place.
"""


def calculate(product, quality):
    result = None
    if product == 'coffee':
        result = quality * 1.50
    elif product == 'water':
        result = quality * 1
    elif product == 'coke':
        result = quality * 1.4
    elif product == 'snack':
        result = quality * 2
    return f'{result:.2f}'


type_product = input()
amount = int(input())
print(calculate(type_product, amount))
