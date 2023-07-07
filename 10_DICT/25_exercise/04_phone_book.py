"""" Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-".
If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N.
Your program should be able to perform a search of contact by name and print its details in the format:
"{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."
"""


phonebook = {}
command = input()

while not command.isnumeric():
    name, number = command.split("-")
    if name not in phonebook.keys():
        phonebook[name] = number
    phonebook[name] = number

    command = input()

for contact in range(int(command)):
    current_name = input()
    if current_name in phonebook.keys():
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
