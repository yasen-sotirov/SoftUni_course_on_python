holidays = int(input())
tom_capacity_time = 30000
game_time_on_working_days = 63
game_time_on_holidays = 127

total_game_time_on_working_days = (365 - holidays) * game_time_on_working_days
total_game_time_on_holidays = holidays * game_time_on_holidays

total_game_time = total_game_time_on_working_days + total_game_time_on_holidays
difference = abs(tom_capacity_time - total_game_time)

hours = difference // 60
minutes = difference % 60

if total_game_time > tom_capacity_time:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
