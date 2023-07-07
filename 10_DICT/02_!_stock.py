"""" You will be given key-value pairs of products and quantities
 (on a single line separated by space). On the following line,
 you will be given products to search for. Check for each product.
 You have 2 possibilities:
•	If you have the product, print "We have {quantity} of {product} left".
•	Otherwise, print "Sorry, we don't have {product}".
"""


data = input().split()
searched_products = input().split()
products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

for current_product in searched_products:
    if current_product in products:
        print(f"We have {products[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
