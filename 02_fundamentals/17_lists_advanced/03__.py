"""" You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.
"""


notes = input()
to_do_list = []

while not notes == "End":
    to_do_list.append(notes)
    notes = input()

to_do_list.sort()
new_list = str("-".join(to_do_list))

to_do_list.split("-")


print(new_list)
