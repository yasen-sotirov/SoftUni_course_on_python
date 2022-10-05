ages = float(input())
gender = input()

if gender == 'm':
    if ages >= 16:
        print('Mr.')
    else:
        print('Master')
if gender == 'f':
    if ages >= 16:
        print('Ms.')
    else:
        print('Miss')
