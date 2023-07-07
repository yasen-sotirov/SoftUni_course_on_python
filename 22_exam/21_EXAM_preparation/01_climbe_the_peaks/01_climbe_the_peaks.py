from collections import deque

food_portions = [int(el) for el in input().split(', ')]
stamina = deque(int(el) for el in input().split(', '))
days = 7

peaks_list = deque(
    [('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70)]
)

climbed_peaks = []

for _ in range(days):
    if not peaks_list:
        break
    current_portion = food_portions.pop()
    current_stamina = stamina.popleft()
    current_peak = peaks_list.popleft()
    current_capacity = current_portion + current_stamina

    if current_capacity >= current_peak[1]:
        climbed_peaks.append(current_peak[0])
    else:
        peaks_list.appendleft(current_peak)


if not peaks_list:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    for peak in climbed_peaks:
        print(peak)