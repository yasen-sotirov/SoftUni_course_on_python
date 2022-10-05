command = input()
max_goals = 0
best_player = 0
player_hat_trick = ''
counter_hat_trick = 0
counter_goals_10 = 0

while command != "END":
    name_of_player = command
    number_of_goals = int(input())
    if number_of_goals >= 10:
        best_player = name_of_player
        max_goals = number_of_goals
        break
    elif number_of_goals > max_goals:
        max_goals = number_of_goals
        best_player = name_of_player
        if number_of_goals > 3:
            player_hat_trick = name_of_player
    command = input()

print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
