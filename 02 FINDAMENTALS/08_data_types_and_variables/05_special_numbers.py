start_number = int(input())

for digit in range(1, start_number + 1):
    if digit <= 10:
        if digit == 5 or digit == 7:
            print(f'{digit} -> True')
        else:
            print(f'{digit} -> False')

    elif digit > 10:
        first_digit = digit // 10
        second_digit = digit % 10
        if first_digit + second_digit == 5 \
                or first_digit + second_digit == 7 \
                or first_digit + second_digit == 11:
            print(f'{digit} -> True')
        else:
            print(f'{digit} -> False')
