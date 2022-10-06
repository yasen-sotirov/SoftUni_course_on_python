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
