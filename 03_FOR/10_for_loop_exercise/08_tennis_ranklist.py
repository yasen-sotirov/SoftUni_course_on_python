number_of_games = int(input())
starting_points = int(input())

stage_w_points = 0
stage_f_points = 0
stage_sf_points = 0
number_of_win = 0
total_points = 0


for num in range(1, number_of_games + 1):
    stage_of_tournament = str(input())

    if stage_of_tournament == "W""":
        stage_w_points += 2000
        number_of_win += 1
    elif stage_of_tournament == "F":
        stage_f_points += 1200
    elif stage_of_tournament == "SF":
        stage_sf_points += 720

total_points = starting_points + stage_w_points + stage_f_points + stage_sf_points
average_points_per_tournament = (stage_w_points + stage_f_points + stage_sf_points) / number_of_games
percentage_of_win = number_of_win / number_of_games * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points_per_tournament:.0f}')
print(f'{percentage_of_win:.2f}%')
