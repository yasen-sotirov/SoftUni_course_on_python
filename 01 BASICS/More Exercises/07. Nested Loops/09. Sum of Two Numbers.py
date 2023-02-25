start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
counter = 0
combination_is_found = False

for first_number in range(start_of_interval, end_of_interval + 1):
    for second_number in range(start_of_interval, end_of_interval + 1):
        counter += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            print(f'Combination N:{counter} ({first_number} + {second_number} = {magic_number})')
            break

if combination_is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
