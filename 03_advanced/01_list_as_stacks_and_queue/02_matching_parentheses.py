""" 2.	Matching Parentheses
You are given an algebraic expression with parentheses.
Scan through the string and extract each set of parentheses.
Print the result back on the console.
Examples
Input
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

Output
(2 + 3)
(3 + 1)
(2 - (2 + 3) * 4 / (3 + 1))
 """


expression = list(input())
per_stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        per_stack.append(index)

    elif expression[index] == ')':
        start_index = per_stack.pop()
        print(expression[start_index:index + 1])
