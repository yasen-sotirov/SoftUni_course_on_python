number_of_strings = int(input())

for strings in range(number_of_strings):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")
