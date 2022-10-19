"""" Write a program that receives a sequence of numbers (a string containing
integers separated by ", ") and prints the numbers sorted into lists of 10's
in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.
"""


number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")
