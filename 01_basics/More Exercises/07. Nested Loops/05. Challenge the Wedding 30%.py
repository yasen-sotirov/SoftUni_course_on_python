number_boys = int(input())
number_girls = int(input())
tables = int(input())
counter_dates = 0
total_number_of_dates = number_boys * number_girls

for men in range(1, number_boys + 1):
    for women in range(1, number_girls + 1):
        counter_dates += 1
        if counter_dates == tables + 1:
            break
        print(f'({men} <-> {women})', end=' ')
