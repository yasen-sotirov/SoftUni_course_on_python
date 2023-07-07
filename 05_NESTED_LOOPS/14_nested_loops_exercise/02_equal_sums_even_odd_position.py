first_number = int(input())
second_number = int(input())

for current_num in range(first_number, second_number + 1):
    even_digit_sum = 0
    odd_digit_sum = 0
    current_num_as_string = str(current_num)
    for index, digit in enumerate(current_num_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if even_digit_sum == odd_digit_sum:
        print(current_num, end=' ')
         