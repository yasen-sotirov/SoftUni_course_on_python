kilometers = int(input())
time_of_the_day = input()
price = 0

if kilometers < 20:
    if time_of_the_day == 'day':
        price = 0.7 + kilometers * 0.79
    else:
        price = 0.7 + kilometers * 0.9
elif kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06

print(f'{price:.2f}')
