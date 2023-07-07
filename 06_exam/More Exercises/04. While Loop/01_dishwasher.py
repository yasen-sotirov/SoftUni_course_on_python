number_bottles = int(input())
command = input()
detergent_amount = number_bottles * 750
number_of_loading = 0
counter_plates = 0
counter_pots = 0
detergent_finished = False

while command != 'End':
    number_of_loading += 1
    number_of_dishes = int(command)
    if number_of_loading % 3 == 0:
        detergent_amount -= number_of_dishes * 15
        counter_pots += number_of_dishes
    else:
        detergent_amount -= number_of_dishes * 5
        counter_plates += number_of_dishes

    if detergent_amount < 0:
        detergent_finished = True
        break
    command = input()

if detergent_amount >= 0:
    print(f'Detergent was enough!')
    print(f"{counter_plates} dishes and {counter_pots} pots were washed.")
    print(f"Leftover detergent {abs(detergent_amount)} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_amount)} ml. more necessary!")

