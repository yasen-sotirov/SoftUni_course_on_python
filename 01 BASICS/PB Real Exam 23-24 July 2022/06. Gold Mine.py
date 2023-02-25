number_of_locations = int(input())

for location in range(number_of_locations):
    expected_average_profit = float(input())
    days_for_digging = int(input())
    gold_counter = 0

    for days in range(days_for_digging):
        collected_gold_per_day = float(input())
        gold_counter += collected_gold_per_day
        average_collected_gold_per_day = gold_counter / days_for_digging
        difference = abs(expected_average_profit - average_collected_gold_per_day)

    if average_collected_gold_per_day >= expected_average_profit:
        print(f"Good job! Average gold per day: {average_collected_gold_per_day:.02f}.")
    else:
        print(f"You need {difference:.02f} gold.")
