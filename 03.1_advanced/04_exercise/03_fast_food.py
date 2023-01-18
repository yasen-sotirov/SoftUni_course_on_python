""" 3. Fast Food
You have a fast-food restaurant, and the food you are offering is previously prepared.
Write a program that checks if you have enough food to serve lunch to all your customers.
You also want to know who the client with the biggest order for that day is.
First, you will be given the quantity of the food you have for the day (an integer number).
 Next, you will be given a sequence of integers (separated by a single space),
 each representing the quantity of food in each order. Keep the orders in a queue.

Find the biggest order and print it. Next, you will begin servicing your clients from the first one
that came. Before each order, check if you have enough food left to complete it:
•	If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
•	Otherwise, stop serving.

Input
•	On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
•	On the second line, you will receive a sequence of integers, representing each order,
separated by a single space

Output
•	On the first line, print the quantity of the biggest order
•	On the second line:
    o	If you succeeded in servicing all your clients, print: "Orders complete".
    o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".

Constraints
•	The input will always be valid

Examples
Input
348
20 54 30 16 7 9

Output
54
Orders complete
"""

from collections import deque

total_food = int(input())
orders = deque([int(el) for el in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]
    if total_food >= current_order:
        total_food -= current_order
        orders.popleft()
    else:
        break

if not orders:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")