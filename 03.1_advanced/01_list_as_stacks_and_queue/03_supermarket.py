""" 3.	Supermarket
Tom is working at the supermarket, and he needs your help to keep track of his clients.
Write a program that reads lines of input consisting of a customer's name and adds it to the end
of a queue until "End" is received. If, in the meantime, you receive the command "Paid",
you should print each customer in the order they are served (from the first to the last one)
and empty the queue.
When you receive "End", you should print the count of the remaining people in the queue in the format:
"{count} people remaining.".

Examples
Input
George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End

Output
George
Peter
William
4 people remaining.
"""

from collections import deque

names = input()
line = deque()

while not names == 'End':
    if names == 'Paid':
        while line:
            print(line.popleft())
    else:
        line.append(names)
    names = input()

print(f'{len(line)} people remaining.')
