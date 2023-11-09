""" You will receive a single number.
You should write a function that returns the sum of all even and all odd digits in a given number.
The result should be returned as a single string in the format:
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
"""


def odd_and_even_sum(number):
    sum_odd_nums = 0
    sum_even_nums = 0

    for digit in str(number):
        current_num = int(digit)
        if int(current_num) % 2 == 0:
            sum_even_nums += current_num
        else:
            sum_odd_nums += current_num
    return sum_odd_nums, sum_even_nums


number_as_string = input()
odd_nums_sum, even_nums_sum = odd_and_even_sum(number_as_string)

print(f"Odd sum = {odd_nums_sum}, Even sum = {even_nums_sum}")

