"ПЪЛНЕНЕ НА GIT CONTRIBUTION CHART" #
# терминала:
# [main = +2 ~0 -0 !]> python app.py

import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2022, 10, 24)
end_date = datetime(2022, 12, 2)

current_date = start_date

while current_date <= end_date:
    # Проверете дали текущият ден не е събота или неделя (0 и 6 са съответно неделя и събота в Python).
    if current_date.weekday() not in [5, 6]:
        num_commits = randint(1, 3)
        for _ in range(num_commits):
            # Създайте и запишете комит.
            commit_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
            with open('file.txt', 'a') as file:
                file.write(commit_date)
            os.system('git add .')
            os.system('git commit --date="' + commit_date + '" -m "commit"')
    # Преминете към следващия ден.
    current_date += timedelta(days=1)

os.system('git push -u origin main')