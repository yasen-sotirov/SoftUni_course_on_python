number_of_entry = int(input())
score = 0
invalid_counter = 0
counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 = 0
counter_40_50 = 0

for number in range(number_of_entry):
    new_number = int(input())
    if new_number < 0 or new_number > 50:
        score /= 2
        invalid_counter += 1
    elif 0 <= new_number <= 9:
        score += new_number * 0.1
        counter_0_9 += 1
    elif new_number <= 19:
        score += new_number * 0.3
        counter_10_19 += 1
    elif new_number <= 29:
        score += new_number * 0.4
        counter_20_29 += 1
    elif new_number <= 39:
        score += 50
        counter_30_39 += 1
    elif new_number <= 50:
        score += 100
        counter_40_50 += 1

percentage_invalid_numbers = invalid_counter / number_of_entry * 100
percentage_number_in_range_0_9 = counter_0_9 / number_of_entry * 100
percentage_number_in_range_10_19 = counter_10_19 / number_of_entry * 100
percentage_number_in_range_20_29 = counter_20_29 / number_of_entry * 100
percentage_number_in_range_30_49 = counter_30_39 / number_of_entry * 100
percentage_number_in_range_40_50 = counter_40_50 / number_of_entry * 100

print(f'{score:.2f}')
print(f"From 0 to 9: {percentage_number_in_range_0_9:.2f}%")
print(f"From 10 to 19: {percentage_number_in_range_10_19:.2f}%")
print(f"From 20 to 29: {percentage_number_in_range_20_29:.2f}%")
print(f"From 30 to 39: {percentage_number_in_range_30_49:.2f}%")
print(f"From 40 to 50: {percentage_number_in_range_40_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid_numbers:.2f}%")
