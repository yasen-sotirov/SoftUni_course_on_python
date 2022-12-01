""" You will receive a single line containing some food (keys) and quantities (values).
They will be separated by a single space (the first element is the key, the second –
the value, and so on).
Create a dictionary with all the keys and values and print it on the console."""

data = input().split()
products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

print(products)

