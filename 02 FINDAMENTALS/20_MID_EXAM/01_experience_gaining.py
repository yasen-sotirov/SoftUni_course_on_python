needed_experience = float(input())
count_of_battles = int(input())
collected_exp = 0
battle_counter = 0
gain_experience = False

for current_battle in range(1, count_of_battles + 1):
    battle_exp = float(input())
    collected_exp += battle_exp
    battle_counter += 1
    if current_battle % 3 == 0:
        collected_exp += battle_exp * 0.15
    if current_battle % 5 == 0:
        collected_exp -= battle_exp * 0.1
    if current_battle % 15 == 0:
        collected_exp += battle_exp * 0.05
    if collected_exp >= needed_experience:
        gain_experience = True
        break

difference = needed_experience - collected_exp
if gain_experience:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
