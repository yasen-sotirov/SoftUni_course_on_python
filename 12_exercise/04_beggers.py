money_list_as_str = input().split(', ')
number_of_beggars = int(input())

money_list_as_digits = []
final_sum = []
starting_index = 0

for element in money_list_as_str:
    money_list_as_digits.append(int(element))

while starting_index < number_of_beggars:
    sum_of_current_beggar = 0

    for current_index in range(starting_index, len(money_list_as_digits), number_of_beggars):
        sum_of_current_beggar += money_list_as_digits[current_index]

    final_sum.append(sum_of_current_beggar)
    starting_index += 1

print(final_sum)
