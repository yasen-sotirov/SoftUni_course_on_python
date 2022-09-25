number = int(input())
for digit in range(1, number + 1):
    working_number = digit
    special_number = 0
    is_special = False
    while working_number > 0:
        special_number += working_number % 10
        working_number = working_number // 10
    if special_number == 5 or special_number == 7 or special_number == 11:
        is_special = True
    print(f"{digit} -> {is_special}")