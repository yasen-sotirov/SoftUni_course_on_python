""" 2. Expression Evaluator
Write a program that evaluates a string expression.
You will be given that string expression on the first line in the form of numbers and operators separated
with a single space from each other. Your job is to take that string expression and calculate the result
after evaluating it.

To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -",
the first time we meet an operator (*), we should take all the numbers we have so far (2, 4),
apply that operation to them, and save the result (8). The next time we meet an operator (-),
we again take all the numbers we have (8, 1, 3) and apply the operator to them in that order
(8 - 1 - 3 = 4). In the end, we print the result.

All the numbers will always be integers, and the possible operators are "*", "+", "-", "/".
It is important to keep the order of the numbers (especially for "/" and "-" because the order matters). When having a division, you should round the result to the lower integer.

Input
    •Single line: a string containing integers and operators

Output
    •Single number: the result after the evaluation

Constrains
    •When reaching an operator, it is sure that you will have a minimum of one number to evaluate
    •The string will always end with an operator, so you get one number as a result
    •Operators and numbers will always be valid
    •There will be no case of division by zero
    •There might be negative numbers in the string

Examples
    Input
6 3 - 2 1 * 5 /
    Output
1
    Comment
6 - 3 = 3
3 * 2 * 1 = 6
6 / 5 = 1
"""

from collections import deque

string_expression_data = input().split()
numbers = deque()
operators = {
    "+": (lambda first_num, second_num: first_num + second_num),
    "-": (lambda f, s: f - s),
    "*": (lambda f, s: f * s),
    "/": (lambda f, s: f // s)
}

for el in string_expression_data:
    if el not in "+-*/":
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            numbers.appendleft(operators[el](numbers.popleft(), numbers.popleft()))

print(numbers.pop())




#
# from collections import deque
#
# string_expression = input().split()
#
# numbers = deque()
#
# for element in string_expression:
#     if element in "+-*/":
#         while len(numbers) > 1:
#             num_one = numbers.popleft()
#             num_two = numbers.popleft()
#
#             result = 0
#
#             if element == "+":
#                 result = num_one + num_two
#             elif element == "-":
#                 result = num_one - num_two
#             elif element == "*":
#                 result = num_one * num_two
#             else:
#                 result = num_one // num_two
#
#             numbers.appendleft(result)
#
#     else:
#         numbers.append(int(element))
#
# print(numbers.popleft())
