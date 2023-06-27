""" Socks Day Sale

Your friend owns a socks store, where he sells lots of fun and colorful socks. He is planning a huge sale for the National Socks Day(4th of December) and he has asked you to help him with the calculations of each order. The rules are simple - your friend wants to keep his standard price for a pair of socks but with each consecutive purchase a certain discount should be received. However, the price per pair should not go down below a certain amount. Essentially your friend wants for the customers to be able to input an amount they are willing to spend - then it is up to us to calculate the total pairs they will receive. What we will know is:

    Budget - how much does the client want to spend.
    Standard Price - the standard price of a pair of socks.
    Discount Per Purchase - the amount that accumulates with each consecutive purchase.
    Price Threshold - The lowest price per pair of socks your friend is willing to sell at.

Fortunately, your friend has prepared an example, so you have an easier time figuring it out:

    The standard price per pair is 100 units.
    The threshold is 40 units.
    The discount per purchase is 10 units.
    Finally, a client's budget is 550.

The client will be able to purchase a total of 8 pairs of socks for a total of 530 units and 20 units of change. The first pair will cost the full standard price - 100 units. The second one will cost the standard price minus the discount - 90 units. The third pair will cost 80 units due to the discount accumulating with every purchase. The final bill calculation will look like this: 100+90+80+70+60+50+40+40=530 units.

There is one more rule - each client that buys 10 or more pairs gets one extra pair.

Your task is to print how many pairs of socks a customer can buy as well as any change they get in return.
Input

Read from the standard input(the console). You will get 4 positive whole numbers on 4 separate lines:

    first line - The client's budget
    second line - the standard price of a pair
    third line - discount per purchase
    fourth line - price threshold

Output

Exactly one line:

    the amount of pairs the client will receive as well as their change, separated by a comma ','

Sample tests
Input

550

100

10

40


Output

8,20

Input

63

10

1

4

Output

11,2
"""
budget = int(input())
price = int(input())
discount_per_purchase = int(input())
threshold_price = int(input())
counter = 0


while True:
    current_discount = discount_per_purchase * counter
    current_price = price - current_discount

    if threshold_price >= current_price:
        current_price = threshold_price
    if budget <= current_price:
        break

    budget -= current_price
    counter += 1

print(f'{counter},{budget}')


