"""" Write a program that receives a sequence of numbers,
separated by a single space,  and prints their absolute value as a list.
Use abs()."""


number = input().split()
abs_number = []

for digit in number:
    abs_number.append(abs(float(digit)))

print(abs_number)
