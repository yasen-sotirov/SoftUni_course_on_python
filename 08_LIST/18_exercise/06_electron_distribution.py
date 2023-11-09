"""" You will receive a single integer - the number of electrons.
Your task is to fill shells until there are no more electrons left.
The rules for electron distribution are as follows:
•	The maximum number of electrons in a shell can be 2n2,
where n is the position of a shell (starting from 1).
For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
•	You should start filling the shells from the first one at the first position.
•	If the electrons are enough to fill the first shell,
the left unoccupied electrons should fill the following shell and so on.
In the end, print a list with the filled shells.
"""


number_of_electrons = int(input())
electrons_left = number_of_electrons
shell_number = 1
shell_list = []

while electrons_left > 0:
    needed_electrons_for_current_shell = 2 * shell_number ** 2
    if needed_electrons_for_current_shell > electrons_left:
        needed_electrons_for_current_shell = electrons_left

    shell_list.append(needed_electrons_for_current_shell)
    electrons_left -= needed_electrons_for_current_shell
    shell_number += 1

print(shell_list)
