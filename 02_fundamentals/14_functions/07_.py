def rounding(num):
    return round(num)


line_of_numbers = input().split()
number_list = []

for current_num in line_of_numbers:
    current_digit = float(current_num)
    rounded_num = round(current_digit)
    rounded_num.append(number_list)
