""" On the first line, you will receive a single number n.
On the following n lines, you will receive integers.
After that, you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive and even).
Finally, print the result. """


number_of_lines = int(input())
numbers_list = []
filtered_num = []

for i in range(number_of_lines):
    numbers = int(input())
    numbers_list.append(numbers)

command = input()

for current_num in numbers_list:
    if command == 'even':
        if current_num % 2 == 0:
            filtered_num.append(current_num)

    elif command == 'odd':
        if not current_num % 2 == 0:
            filtered_num.append(current_num)

    elif command == 'negative':
        if current_num < 0:
            filtered_num.append(current_num)

    elif command == 'positive':
        if current_num >= 0:
            filtered_num.append(current_num)

print(filtered_num)
