divisor = int(input())
boundary = int(input())

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        break
print(current_number)
