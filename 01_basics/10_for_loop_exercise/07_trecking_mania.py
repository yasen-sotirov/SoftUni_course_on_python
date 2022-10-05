numbers_of_groups = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for num in range(1, numbers_of_groups + 1):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group > 40:
        everest += people_in_group

total_sum = musala + monblan + kilimanjaro + k2 + everest

percentage_of_climbing_musala = musala / total_sum * 100
percentage_of_climbing_monblan = monblan / total_sum * 100
percentage_of_climbing_kilimanjaro = kilimanjaro / total_sum * 100
percentage_of_climbing_k2 = k2 / total_sum * 100
percentage_of_climbing_everest = everest / total_sum * 100

print(f'{percentage_of_climbing_musala:.2f}%')
print(f'{percentage_of_climbing_monblan:.2f}%')
print(f'{percentage_of_climbing_kilimanjaro:.2f}%')
print(f'{percentage_of_climbing_k2:.2f}%')
print(f'{percentage_of_climbing_everest:.2f}%')
