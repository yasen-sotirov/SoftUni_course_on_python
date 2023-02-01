numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = input()
    if not number.isdigit():
        print(f"The variable number must be an integer")
    else:
        number = int(number)
        numbers_dictionary[number_as_string] = number
    line = input()

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])
    line = input()

line = input()

while line != "End":
    searched = line
    if searched in numbers_dictionary:
        del numbers_dictionary[searched]
    else:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
