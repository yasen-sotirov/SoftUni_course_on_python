number_of_rows = int(input())

for current_number in range(1, number_of_rows + 1):
    for num in range(current_number):
        print(current_number, end=' ')
    print()
