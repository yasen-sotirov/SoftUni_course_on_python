from math import ceil
name = str(input())
duration_movie = int(input())
duration_break = int(input())

lunch = duration_break * 0.125
rest = duration_break * 0.25

needed_time_for_all_things = duration_movie + lunch + rest

difference = abs(needed_time_for_all_things - duration_break)

if duration_break >= needed_time_for_all_things:
    print(f"You have enough time to watch {name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(difference)} more minutes.")
