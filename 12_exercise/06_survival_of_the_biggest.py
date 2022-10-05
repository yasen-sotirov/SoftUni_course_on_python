list_of_numbers = input().split()
numbers_for_remove = int(input())

list_as_int = [int(x) for x in list_of_numbers]

for x in range(numbers_for_remove):
    list_as_int.pop(min(list_as_int))

print(list_as_int)
