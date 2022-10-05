number_of_days = int(input())
first_day_km = int(input())
new_km = 0
total_added_km = 0
last_day_km = 0
counter_km = 0
target = 1000

for i in range(number_of_days):
    if i == 0:
        counter_km += first_day_km
        last_day_km += first_day_km
    else:
        percentage_increasing = int(input()) / 100
        new_km = last_day_km * percentage_increasing
        total_added_km += new_km
        last_day_km = total_added_km + first_day_km
        counter_km += last_day_km

if counter_km >= target:
    print(f"You've done a great job running {counter_km - target:.2f} more   kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {target - counter_km:.2f} more kilometers")
