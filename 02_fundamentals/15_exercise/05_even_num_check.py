def check_even(number):
    if number % 2 == 0:
        return True
    return False


number_line = input().split()
numbers = []

for current_digit in number_line:
    current_num = int(current_digit)
    numbers.append(current_num)

even_numbers_iterator = filter(check_even, numbers)
print(list(even_numbers_iterator))

