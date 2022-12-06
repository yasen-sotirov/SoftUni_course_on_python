""" 03. The Pianist
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2525#2.

Create a program to help you organize it and add, change, remove pieces from it!
On the first line of the standard input, you will receive an integer n – the number of pieces
you will initially have. On the next n lines, the pieces themselves will follow with their composer
and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
Then, you will be receiving different commands, each on a new line, separated by "|",
until the "Stop" command is given:

•	"Add|{piece}|{composer}|{key}":
    - You need to add the given piece with the information about it to the other pieces and print:
      "{piece} by {composer} in {key} added to the collection!"
    -  If the piece is already in the collection, print:
      "{piece} is already in the collection!"

•	"Remove|{piece}":
    - If the piece is in the collection, remove it and print:  "Successfully removed {piece}!"
    - Otherwise, print:   "Invalid operation! {piece} does not exist in the collection."

•	"ChangeKey|{piece}|{new key}":
    - If the piece is in the collection, change its key with the given one and print:
      "Changed the key of {piece} to {new key}!"
    - Otherwise, print:  "Invalid operation! {piece} does not exist in the collection."

Upon receiving the "Stop" command, you need to print all pieces in your collection,
sorted by their name and by the name of their composer in alphabetical order, in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"

Input/Constraints
•	You will receive a single integer at first – the initial number of pieces in the collection
•	For each piece, you will receive a single line of text with information about it.
•	Then you will receive multiple commands in the way described above until the command "Stop".

Output
•	All the output messages with the appropriate formats are described in the problem description.

Examples:

    Input
3
Fur Elise|Beethoven|A Minor
Moonlight Sonata|Beethoven|C# Minor
Clair de Lune|Debussy|C# Minor
Add|Sonata No.2|Chopin|B Minor
Add|Hungarian Rhapsody No.2|Liszt|C# Minor
Add|Fur Elise|Beethoven|C# Minor
Remove|Clair de Lune
ChangeKey|Moonlight Sonata|C# Major
Stop

    Output
Sonata No.2 by Chopin in B Minor added to the collection!
Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
Fur Elise is already in the collection!
Successfully removed Clair de Lune!
Changed the key of Moonlight Sonata to C# Major!
Fur Elise -> Composer: Beethoven, Key: A Minor
Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor
Moonlight Sonata -> Composer: Beethoven, Key: C# Major
Sonata No.2 -> Composer: Chopin, Key: B Minor
"""


def store_data_func(number):
    data = {}
    for _ in range(number):
        current_data = input().split("|")
        piece = current_data[0]
        composer = current_data[1]
        key = current_data[2]
        data[piece] = [composer, key]
    return data


def add_command_function(piece, composer, key, data):
    if piece not in data:
        data[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_function(piece, data):
    if piece in data:
        print(f"Successfully removed {piece}!")
        del data[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_function(piece, new_key, data):
    if piece in data:
        data[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_function(data):
    result = ''
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"
    return result


def the_pianist_func(number):
    data = store_data_func(number)
    while True:
        command = input().split("|")

        if command[0] == "Stop":
            print(print_function(data))
            break

        current_command = command[0]
        piece = command[1]

        if current_command == "Add":
            composer = command[2]
            key = command[3]
            add_command_function(piece, composer, key, data)
        elif current_command == "Remove":
            remove_function(piece, data)
        elif current_command == "ChangeKey":
            new_key = command[2]
            change_key_function(piece, new_key, data)


number_of_pieces = int(input())
the_pianist_func(number_of_pieces)
