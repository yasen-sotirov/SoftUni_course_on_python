""" 4. Fashion Boutique
You own a fashion boutique and receive a delivery of a huge box of clothes,
represented as a sequence of integers. On the following line,
you will be given an integer representing the capacity for one rack in your store.
You must arrange the clothes in the store and use the racks to hang up every piece
of clothing. You start from the last piece of clothing on the top of the pile
to the first one at the bottom. Use a stack for this purpose.
Each piece of clothing has its value (an integer).
You must sum their values while you take them out of the box:
•	If the sum becomes equal to the capacity of the current rack,
    you must take a new one for the next clothes (if there are any left in the box).
•	If the sum becomes greater than the capacity, do not hang the piece of clothing
    on the current rack. Take a new rack and then hang it up.

In the end, print how many racks you have used to hang up the clothes.

Input
•	On the first line, you will be given a sequence of integers representing
    the clothes in the box, separated by a single space.
•	On the second line, you will be given an integer representing the capacity
    of a rack.

Output
•	Print the number of racks needed to hang up the clothes from the box.

Constraints
•	The values of the clothes will be integers in the range [0,20]
•	There will never be more than 50 clothes in a box
•	The capacity will be an integer in the range [0,20]
•	None of the integers from the box will be greater than the value of the capacity

Examples
Input
5 4 8 6 3 8 7 7 9
16

Output
5

 """


clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

current_rack = rack_capacity
counter = 1

while clothes:
    current_clothe = clothes[-1]
    if current_clothe <= current_rack:
        clothes.pop()
        current_rack -= current_clothe
    else:
        counter += 1
        clothes.pop()
        current_rack = rack_capacity - current_clothe

print(counter)
