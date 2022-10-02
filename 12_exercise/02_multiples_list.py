factor = int(input())
count = int(input())
list_of_multiples = []

for element in range(1, count + 1):
    list_of_multiples.append(factor * element)
print(list_of_multiples)
