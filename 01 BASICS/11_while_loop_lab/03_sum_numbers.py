constant_number = int(input())
current_sum = 0

while True:
    number = int(input())
    current_sum += number

    if current_sum >= constant_number:
        print(current_sum)
        break
