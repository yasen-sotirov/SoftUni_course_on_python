number_of_iterations = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, number_of_iterations + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print("Yes")
    print(f'Sum = {even_sum}')
else:
    different = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {different}')
