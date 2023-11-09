upper_number_hundreds = int(input())
upper_number_dozens = int(input())
upper_number_units = int(input())

for digit_1 in range(1, upper_number_hundreds + 1):
    for digit_2 in range(1, upper_number_dozens + 1):
        for digit_3 in range(1, upper_number_units + 1):
            if digit_1 % 2 == 0 and digit_3 % 2 == 0:
                if digit_2 == 0:     # kak да проверя дали е просто число??
                    print(f'{digit_1} {digit_2} {digit_3}')
