decrypting_key = int(input())
number_of_lines = int(input())

for _ in range(number_of_lines):
    current_letter = input()
    letter_code = ord(current_letter)
    decrypted_letter = letter_code + decrypting_key
    print(chr(decrypted_letter), end='')
