total_sum = 0

while True:
    command = input()

    if command == 'NoMoreMoney':
        break

    added_sum = float(command)

    if added_sum >= 0:
        total_sum += added_sum
        print(f'Increase: {added_sum:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {total_sum:.2f}')
