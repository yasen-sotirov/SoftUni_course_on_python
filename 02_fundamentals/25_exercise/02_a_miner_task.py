"""" You will be given a sequence of strings, each on a new line until you receive the "stop"
command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on)
 and every even - quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
The quantities will be in the range [1 … 2 000 000 000].
"""

resource_list = {}
command = input()

while not command == "stop":
    resource = command
    if resource not in resource_list:
        resource_list[resource] = 0

    quantity = int(input())
    resource_list[resource] += quantity
    command = input()

for resource, quantity in resource_list.items():
    print(f"{resource} -> {quantity}")
