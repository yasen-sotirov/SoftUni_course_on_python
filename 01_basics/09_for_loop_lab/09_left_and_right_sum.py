numbers_of_iterations = int(input())
left_sum = 0
right_sun = 0

for i in range(numbers_of_iterations * 2):
    current_number = int(input())

    if i < numbers_of_iterations:
        left_sum += current_number
    else:
        right_sun += current_number

difference = abs(left_sum - right_sun)

if left_sum == right_sun:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {difference}')
