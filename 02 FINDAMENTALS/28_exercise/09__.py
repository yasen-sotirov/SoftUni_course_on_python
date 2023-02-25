data = input()

letter = ""
number = ""
last_char_is_letter = True
final_text = ""


for current_char in data:
    if not last_char_is_letter and current_char.isdigit():
        number += current_char

    elif current_char.isalpha() and not last_char_is_letter:
        final_text += letter * int(number)
        letter = ""
        number = ""
        last_char_is_letter = True
        letter = current_char

    elif not current_char.isdigit():
        letter += current_char
    else:
        number += current_char
        last_char_is_letter = False

final_text += letter * int(number)
print(final_text.upper())

