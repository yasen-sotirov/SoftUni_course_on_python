"""" Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-".
If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N.
Your program should be able to perform a search of contact by name and print its details in the format:
"{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."
"""


phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = input().split("-")
    phonebook[name] = phone

for search in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
