beginning_num = int(input())
ending_num = int(input())

for digit_1 in range(beginning_num, ending_num + 1):
    for digit_2 in range(beginning_num, ending_num + 1):
        for digit_3 in range(beginning_num, ending_num + 1):
            for digit_4 in range(beginning_num, ending_num + 1):
                if digit_1 > digit_4:
                    if (digit_2 + digit_3) % 2 == 0:
                        if (digit_1 % 2 == 0 and digit_4 % 2 != 0) or (digit_1 % 2 != 0 and digit_4 % 2 == 0):
                            print(f'{digit_1}{digit_2}{digit_3}{digit_4}', end=" ")
