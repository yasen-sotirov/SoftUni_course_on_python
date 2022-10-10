""" You will receive a single number.
You should write a function that returns the sum of all even and all odd digits in a given number.
The result should be returned as a single string in the format:
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
"""


def odd_and_even_sum(number):
    sum_of_odd_nums = 0
    sum_of_even_nums = 0

    for current_num in number:
        if int(current_num) % 2 == 0:
            sum_of_even_nums += int(current_num)
        else:
            sum_of_odd_nums += int(current_num)
    return sum_of_odd_nums, sum_of_even_nums


number_as_string = input()

sum_of_odd_nums, sum_of_even_nums = odd_and_even_sum(number_as_string)

print(f'"Odd sum = {sum_of_odd_nums}, Even sum = {sum_of_even_nums}"')
