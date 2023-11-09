from math import floor

planed_number_processors = int(input())
number_employees = int(input())
working_days = int(input())

total_working_hours = number_employees * working_days * 8
total_produced_processors = floor(total_working_hours / 3)

difference = abs(total_produced_processors - planed_number_processors)
profit_in_bgn = difference * 110.10

if total_produced_processors >= planed_number_processors:
    print(f"Profit: -> {profit_in_bgn:.2f} BGN")
else:
    print(f"Losses: -> {profit_in_bgn:.2f} BGN")
