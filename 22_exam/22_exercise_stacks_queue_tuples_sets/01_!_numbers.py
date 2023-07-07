"""
1.	Numbers
First, you will be given two sequences of integers values on different lines. The values of the sequences
are separated by a single space between them.
Keep in mind that each sequence should contain only unique values.

Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
•	"Add First {numbers, separated by a space}" -
    add the given numbers at the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" -
    add the given numbers at the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" -
    remove only the numbers contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" -
    remove only the numbers contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other.
    If it is, print "True". Otherwise, print "False".

In the end, print the final sequences, separated by a comma and a space ", ".
The values in each sequence should be sorted in ascending order.

Examples
Input
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset

Output
True
1, 2, 3, 4, 5, 6
1, 2, 3

"""


first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command_line = input().split()
    command = command_line[0]
    argument = command_line[1]

    if command == "Add":
        if argument == "First":
            [first.add(int(x)) for x in command_line[2:]]
        else:
            [second.add(int(x)) for x in command_line[2:]]

    elif command == "Remove":
        if argument == "First":
            first = first.difference([int(x) for x in command_line[2:]])
        else:
            second = second.difference([int(x) for x in command_line[2:]])

    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
