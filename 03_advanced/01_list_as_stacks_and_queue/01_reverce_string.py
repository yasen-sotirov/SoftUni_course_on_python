""" 1.	Reverse Strings
Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console
Examples
Input
I Love Python
Output
nohtyP evoL I
 """


text = list(input())
stack = []

for element in range(len(text)):
    stack.append(text.pop())

print(''.join(stack))
