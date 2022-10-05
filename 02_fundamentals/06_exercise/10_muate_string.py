first_string = input()
second_string = input()
last_printed_string = first_string

for character_index in range(len(first_string)):
    left_path = second_string[:character_index + 1]
    right_path = first_string[character_index + 1:]
    current_string = left_path + right_path
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
