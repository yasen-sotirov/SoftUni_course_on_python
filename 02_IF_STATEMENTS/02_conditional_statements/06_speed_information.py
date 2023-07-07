info_of_speed = round(float(input()), 1)

if info_of_speed <= 10:
    print('slow')
elif 10 < info_of_speed <= 50:
    print('average')
elif 50 < info_of_speed <= 150:
    print('fast')
elif 150 < info_of_speed <= 1000:
    print('ultra fast')
elif info_of_speed > 1000:
    print('extremely fast')
