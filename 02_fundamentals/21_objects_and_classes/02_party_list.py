"""" Create a class Party that only has an attribute people – empty list.
The __init__ method should not accept any parameters.
You will be given names of people (on separate lines) until
you receive the command "End". Use the created class to solve this problem.
After you receive the "End" command, print 2 lines:
•	"Going: {people}" - the people should be separated by comma
and space ", ".
•	"Total: {total_people_going}"
"""


class Party:
    def __init__(self):
        self.people = []


my_party = Party()

gest_name = input()

while not gest_name == "End":
    my_party.people.append(gest_name)
    gest_name = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
