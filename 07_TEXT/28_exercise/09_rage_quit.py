data = input()
repetition_symbols = ""
number_of_repetition = 0
final_text = ""
unique_symbols = []

for current_symbol in data:
    if current_symbol.isdigit():
        number_of_repetition += int(current_symbol)
    else:
        repetition_symbols += current_symbol
        current_symbol = current_symbol.upper()
        if current_symbol not in unique_symbols:
            unique_symbols.append(current_symbol)

    if number_of_repetition > 0:
        final_text += repetition_symbols.upper() * number_of_repetition
        number_of_repetition = 0
        repetition_symbols = ""

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_text)
