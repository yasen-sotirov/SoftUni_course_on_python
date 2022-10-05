type_of_movie = input()
rows = int(input())
columns = int(input())
income = 0

if type_of_movie == 'Premiere':
    income = rows * columns * 12
elif type_of_movie == 'Normal':
    income = rows * columns * 7.50
elif type_of_movie == 'Discount':
    income = rows * columns * 5

print(f'{income:.2f} leva')
