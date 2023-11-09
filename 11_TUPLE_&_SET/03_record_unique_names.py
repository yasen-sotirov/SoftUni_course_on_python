""" 3.	Record Unique Names
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
Examples
    Input
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey

    Output
Alan
Joey
Lee
Joe
Peter
"""


number = int(input())
names = set()

for _ in range(number):
    names.add(input())

print("\n".join(names))