number_n = int(input())

odd_set = set()
even_set = set()
sum_odd = 0
sum_even = 0

for row in range(1, number_n + 1):
    name_sum = sum([ord(el) for el in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
        sum_even += name_sum
    else:
        odd_set.add(name_sum)
        sum_odd += name_sum


