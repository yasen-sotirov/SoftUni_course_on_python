import sys

count_of_numbers = int(input())
sum_of_all_elements = 0
max_element = - sys.maxsize

for number in range(count_of_numbers):
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_element:
        max_element = current_number

if max_element == sum_of_all_elements - max_element:
    print('Yes')
    print(f'Sum = {max_element}')

else:
    difference = abs(max_element - (sum_of_all_elements - max_element))
    print('No')
    print(f'Diff = {difference}')
