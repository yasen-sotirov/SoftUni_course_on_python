"""" Write a program, which validates a parking place - users can register to enter the park
and unregister to leave.
The program receives 2 types of commands:
•	"register {username} {license_plate_number}":
o	The system only supports one car per user at the moment, so if a user tries to register another
license plate using the same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"
o	If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
•	"unregister {username}":
o	If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
o	If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license
plates in the format:
•	"{username} => {license_plate_number}"
Input
•	First line: n - number of commands - integer
•	Next n lines: commands in one of the two possible formats:
o	Register: "register {username} {license_plate_number}"
o	Unregister: "unregister {username}"
The input will always be valid, and you do not need to check it explicitly.
"""


parking_dictionary = {}
number_of_commands = int(input())

for current_car in range(number_of_commands):
    command = input().split(" ")
    if "register" in command:
        username = command[1]
        license_plate_number = command[2]
        if username in parking_dictionary.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            print(f"{username} registered {license_plate_number} successfully")
            parking_dictionary[username] = license_plate_number
    else:
        username = command[1]
        if username not in parking_dictionary.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_dictionary[username]

for username, license_plate_number in parking_dictionary.items():
    print(f"{username} => {license_plate_number}")
