"""" You will be receiving key-value pairs on separate lines separated by ": "
until you receive the command "statistics". Sometimes you may receive a product
more than once. In that case, you have to add the new quantity to the existing one.
When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
- {productN}: {quantityN}
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
"""


data = input()
products_list = {}

while not data == "statistics":
    product_name, product_quantity = data.split(': ')
    if product_name not in products_list:
        products_list[product_name] = int(product_quantity)
    else:
        products_list[product_name] += int(product_quantity)

    data = input()

print("Products in stock:")
for key, value in products_list.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products_list)}")
print(f"Total Quantity: {sum(products_list.values())}")
