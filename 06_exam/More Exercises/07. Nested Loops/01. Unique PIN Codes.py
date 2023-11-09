upper_number_1 = int(input())
upper_number_2 = int(input())
upper_number_3 = int(input())

for num_1 in range(1, upper_number_1 + 1):
    for num_2 in range(2, upper_number_2 + 1):
        for num_3 in range(1, upper_number_3 + 1):
            if num_1 % 2 == 0:
                if num_2 == 2 or num_2 == 3 or num_2 == 5 or num_2 == 7:
                    if num_3 % 2 == 0:
                        print(f'{num_1} {num_2} {num_3}')
