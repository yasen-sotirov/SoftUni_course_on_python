from math import ceil

number_of_people = int(input())
entry_tax = float(input())
sunbed_tax = float(input())
umbrella_tax = float(input())

total_entry_tax = number_of_people * entry_tax
total_umbrella_tax = ceil(number_of_people / 2) * umbrella_tax
total_sunbed_tax = ceil(number_of_people * 0.75) * sunbed_tax

total_price = total_sunbed_tax + total_umbrella_tax + total_entry_tax

print(f'{total_price:.2f} lv.')
