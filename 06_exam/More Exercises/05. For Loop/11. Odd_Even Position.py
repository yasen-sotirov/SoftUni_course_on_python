from sys import maxsize

number_of_numbers = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = - maxsize
even_sum = 0
even_min = maxsize
even_max = - maxsize

for num in range(1, number_of_numbers + 1):
    current_num = float(input())

    if num % 2 == 0:
        even_sum += current_num
        if current_num > even_max:
            even_max = current_num
        if current_num < even_min:
            even_min = current_num

    else:
        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num
        if current_num < odd_min:
            odd_min = current_num

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min:.2f},')
print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min:.2f},')
print(f'EvenMax={even_max:.2f},')
