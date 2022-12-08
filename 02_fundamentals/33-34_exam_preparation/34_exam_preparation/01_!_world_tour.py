""" 01. World Tour
    SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
    On the first line, you will be given a string containing all of your stops.
Until you receive the command "Travel", you will be given some commands to manipulate
that initial string. The commands can be:

•	"Add Stop:{index}:{string}":
    o	Insert the given string at that index only if the index is valid

•	"Remove Stop:{start_index}:{end_index}":
    o	Remove the elements of the string from the starting index to the end
    index (inclusive) if both indices are valid

•	"Switch:{old_string}:{new_string}":
    o	If the old string is in the initial string,
        replace it with the new one (all occurrences)

Note: After each command, print the current state of the string
After the "Travel" command, print the following: "Ready for world tour!
Planned stops: {string}"

Input / Constraints
•	JavaScript: you will receive a list of strings
•	An index is valid if it is between the first and the last element index
    (inclusive) in the sequence.

Output
•	Print the proper output messages in the proper cases as described in
    the problem description

Examples

Input
Hawai::Cyprys-Greece
Add Stop:7:Rome
Remove Stop:11:16
Switch:Hawai:Bulgaria
Travel

Output
Hawai::RomeCyprys-Greece
Hawai::Rome-Greece
Bulgaria::Rome-Greece
Ready for world tour! Planned stops: Bulgaria::Rome-Greece
"""


# def add_stop(data, stops):
#     index, string = [int(x) if x.isdigit() else x for x in data]
#     if 0 <= index < len(stops):
#         stops = stops[:index] + string + stops[index:]
#     return stops
#
#
# def remove_stop(data, stops):
#     start_index, end_index = [int(x) for x in data]
#     if 0 <= start_index <= end_index < len(stops):
#         stops = stops[:start_index] + stops[end_index + 1:]
#     return stops
#
#
# def switch(data, stops):
#     old_string, new_string = [x for x in data]
#     if old_string in stops:
#         stops = stops.replace(old_string, new_string)
#     return stops
#
#
# def main():
#     stops = input()
#     while True:
#         commands = input()
#         if "Travel" in commands:
#             break
#         commands, *data = commands.split(":")
#         if "Add Stop" in commands:
#             stops = add_stop(data, stops)
#         elif "Remove Stop" in commands:
#             stops = remove_stop(data, stops)
#         elif "Switch" in commands:
#             stops = switch(data, stops)
#         print(stops)
#     print(f"Ready for world tour! Planned stops: {stops}")
#
#
# if __name__ == "__main__":
#     main()


list_of_stops = input()

while True:
    command = input().split(":")
    if "Travel" in command:
        print(f"Ready for world tour! Planned stops: {list_of_stops}")
        break

    elif "Add Stop" in command:
        index, string = int(command[1]), command[2]
        if 0 <= index < len(list_of_stops):
            list_of_stops = list_of_stops[:index] + string + list_of_stops[index:]
            print(list_of_stops)

    elif "Remove Stop" in command:
        start_index, end_index = [int(x) for x in command if x.isdigit()]
        if 0 <= start_index <= end_index < len(list_of_stops):
            list_of_stops = list_of_stops[:start_index] + list_of_stops[end_index + 1:]
            print(list_of_stops)

    elif "Switch" in command:
        old_string, new_string = command[1], command[2]
        if old_string in list_of_stops:
            list_of_stops = list_of_stops.replace(old_string, new_string)
            print(list_of_stops)
