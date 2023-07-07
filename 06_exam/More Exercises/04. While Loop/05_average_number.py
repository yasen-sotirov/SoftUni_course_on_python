start_number = int(input())
sum_of_numbers = 0

for num in range(start_number):
    new_number = int(input())
    sum_of_numbers += new_number

print(f'{sum_of_numbers / start_number:.2f}')
