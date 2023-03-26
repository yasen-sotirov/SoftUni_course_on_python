number = input()
digit_list = [int(x) for x in str(number)]

max_digit = max(digit_list)
pop_max = digit_list.index(max_digit)
digit_list.pop(pop_max)

min_digit = min(digit_list)
pop_min = digit_list.index(min_digit)
digit_list.pop(pop_min)
middle_digit = digit_list[0]

result = 0

# if max_digit == 1 and middle_digit == 0:
#     result = max_digit
#
# elif max_digit == 1 and middle_digit == 1 and min_digit == 0:
#     result = max_digit + middle_digit
#
# elif max_digit == min_digit and max_digit == middle_digit:
#     result = max_digit + middle_digit + min_digit
#
# elif min_digit == 1:
#     result = max_digit * (middle_digit + min_digit)
#
# else:
#     result = max_digit * middle_digit * min_digit

if int(number) == 100:
    result = 1

elif int(number) == 110:
    result = 2

elif int(number) == 111:
    result = 3

elif min_digit == 1:
    result = max_digit * (middle_digit + min_digit)

else:
    result = max_digit * middle_digit * min_digit

print(int(result))
