number_n = int(input())

odd_set = set()
even_set = set()
odd_sum = 0
even_sum = 0

for row in range(1, number_n + 1):
    name_sum = sum([ord(el) for el in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
        even_sum += name_sum
    else:
        odd_set.add(name_sum)
        odd_sum += name_sum

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(*result, sep=', ')
