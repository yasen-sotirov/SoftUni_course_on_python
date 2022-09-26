number_of_letters = int(input())

for first_char in range(number_of_letters):
    for second_char in range(number_of_letters):
        for third_char in range(number_of_letters):
            print(f"{chr(first_char + 97)}{chr(second_char + 97)}{chr(third_char + 97)}")
