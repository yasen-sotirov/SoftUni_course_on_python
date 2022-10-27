"""" You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.
"""


to_do_list = [0] * 10
command = input()

while not command == 'End':
    importance, note = command.split('-')
    current_index = int(importance) - 1
    to_do_list[current_index] = note
    command = input()

print([element for element in to_do_list if not element == 0])
