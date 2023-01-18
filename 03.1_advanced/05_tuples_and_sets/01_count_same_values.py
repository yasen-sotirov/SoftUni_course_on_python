""" 1.	Count Same Values
You will be given numbers separated by a space.
Write a program that prints the number of occurrences of each number in the format
"{number} - {count} times". The number must be formatted to the first decimal point.
"""


data = (float(el) for el in input().split())
counter_dict = {}

for num in data:
    if num not in counter_dict:
        counter_dict[num] = 0
    counter_dict[num] += 1

# for key, value in counter_dict.items():
#     print(f"{key} - {value} times")

for data in counter_dict.items():
    print(f"{data[0]} - {data[1]} times")
    # print(type(data))