number_as_string = [int(x) for x in input()]
even_nums = 0
odd_nums = 0

for current_num in number_as_string:
    if current_num % 2 == 0:
        even_nums += current_num
    else:
        odd_nums += current_num

if even_nums > odd_nums:
    print(f'{even_nums} energy drinks')

elif odd_nums > even_nums:
    print(f'{odd_nums} cups of coffee')

else:
    print(f'{even_nums} of both')

