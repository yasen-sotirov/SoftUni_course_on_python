from datetime import datetime, date, timedelta
import calendar

expected_day = input().split()
expected_day_as_list = [int(x) if x.isdigit() else x for x in expected_day]

month = list(calendar.month_name).index(expected_day_as_list[1])
edited_date = f'{expected_day_as_list[0]}-{month}-{expected_day_as_list[2]}'

expected_temperature = int(input())
rain = int(input())
winter_length = int(input())

optimal_temperature = 20
optimal_rain = 30


additional_days = 0

if calendar.isleap(expected_day_as_list[2]):
    expected_temperature += 5

additional_days += winter_length // 7
additional_days += optimal_temperature - expected_temperature
additional_days += abs(optimal_rain - rain) // 3

date_1 = datetime.strptime(edited_date, '%d-%m-%Y')
result = str(date_1 + timedelta(days=additional_days))
res = result.split()
res_1 = res[0].split('-')

month_as_num = int(res_1[1])
month_as_name = calendar.month_name[month_as_num]

res_2 = f'{res_1[2]} {month_as_name} {res_1[0]}'

print(res_2)

