given_string = input()
current_letter_as_capital = ''
lst = []

for index, letter in enumerate(given_string):
    current_letter_as_capital = letter.isupper()
    if current_letter_as_capital:
        lst.append(index)

print(lst)
