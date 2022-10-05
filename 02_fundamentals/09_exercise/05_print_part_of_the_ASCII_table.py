start_char_number = int(input())
final_char_number = int(input())

for character in range(start_char_number, final_char_number + 1):
    print(chr(character), end=' ')
