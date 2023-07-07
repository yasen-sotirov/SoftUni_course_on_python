""" Password Reset
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2303#0.

Yet again, you have forgotten your password. Naturally, it's not the first time this has happened.
Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
Write a password reset program that performs a series of commands upon a predefined string.
First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
•	"TakeOdd"
    - Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
•	"Cut {index} {length}"
    - Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
    - The given index and the length will always be valid.
•	"Substitute {substring} {substitute}"
    - If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
    - If it doesn't, prints "Nothing to replace!".

Input
•	You will be receiving strings until the "Done" command is given.

Output
•	After the "Done" command is received, print:
    - "Your password is: {password}"

Constraints
•	The indexes from the "Cut {index} {length}" command will always be valid.
"""


password = input()

while True:
    command = input().split()
    action = command[0]
    if action == "Done":
        print(f"Your password is: {password}")
        break

    elif action == "TakeOdd":
        password = password[1::2]
        print(password)

    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)

    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
