number = input().split()
abs_number = []

for digit in number:
    abs_number.append(abs(float(digit)))

print(abs_number)