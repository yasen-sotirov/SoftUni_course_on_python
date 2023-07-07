""" 2. Stacked Queries
You have an empty stack. You will receive an integer – N.
On the next N lines, you will receive queries.
Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom
in the following format:
"{n}, {n1}, {n2}, ... {nn}"

Examples
Input
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

Output
26
20
91, 20, 26
"""


from collections import deque

numbers = deque()
map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers) if numbers else None),
    4: lambda x: print(min(numbers) if numbers else None),
}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)

numbers.reverse()
# print(numbers)
print(*numbers, sep=', ')
