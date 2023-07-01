actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

total_points = academy_points

for current_grade in range(number_of_jury):
    current_jury_name = input()
    current_jury_points = float(input())

    current_final_points = len(current_jury_name) * current_jury_points / 2
    total_points += current_final_points

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points}!')
else:
    difference = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')



# for hour in range(0, 24):
#     for minutes in range(0, 60):
#         for seconds in range(0, 60):
#             print( f'time is {hour:02d}:{minutes:02d}:{seconds:02d}')