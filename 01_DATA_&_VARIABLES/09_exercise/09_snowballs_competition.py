number_of_balls = int(input())
best_ball_weight = 0
best_ball_time = 0
best_ball_value = 0
best_ball_quality = 0

for current_ball in range(number_of_balls):
    current_ball_weight = int(input())
    current_ball_time = int(input())
    current_ball_quality = int(input())

    current_ball_value = (current_ball_weight / current_ball_time) ** current_ball_quality
    if current_ball_value > best_ball_value:

        best_ball_weight = current_ball_weight
        best_ball_time = current_ball_time
        best_ball_value = current_ball_value
        best_ball_quality = current_ball_quality

print(f"{best_ball_weight} : {best_ball_time} = {int(best_ball_value)} ({best_ball_quality})")
