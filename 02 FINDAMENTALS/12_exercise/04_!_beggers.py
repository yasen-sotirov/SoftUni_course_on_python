"""" You will receive 2 lines of input. On the first line,
you will receive a single string of integers, separated by a comma
and a space ", ". On the second line, you will receive a count
of beggars. Your job is to print a list with the sum of what each
beggar brings home, assuming they all take regular turns,
from the first to the last number in the list.
For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9
and 6, as the first one takes [1, 3, 5],
the second one collects [2, 4]. The same list with 3 beggars
would produce a better outcome for the second beggar: 5, 7 and 3,
as they will respectively take [1, 4], [2, 5], and [3].
Also, note that not all beggars have to take the same amount of
"offers", meaning that the length of the list is not necessarily a multiple of n.
The list length could be even shorter - i.e.,
the last beggars will take nothing (0).
"""


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
