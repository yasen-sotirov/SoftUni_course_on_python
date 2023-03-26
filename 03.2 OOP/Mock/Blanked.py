""" Balanced Numbers

A balanced number is a 3-digit number whose second digit is equal to the sum of the first and last digit.

Write a program which reads and sums balanced numbers. You should stop when an unbalanced number is given.
Input

Input data is read from the standard input

    Numbers will be given
        Each one will be on a separate line

Output

Print to the standard output
Constraints

    No more than 1000 numbers will be given

Sample tests
Input

132

123

Output

 132

Input

275

693

110

742

Output

1078
"""


data = int(input())
result = 0
for num in range(data):
    current_nums = [int(x) for x in str(data)]
    digit_1 = current_nums[0]
    digit_2 = current_nums[1]
    digit_3 = current_nums[2]
    if digit_1 + digit_3 == digit_2:
        result += num
    else:
        break
print(result)
