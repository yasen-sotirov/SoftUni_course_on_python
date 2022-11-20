"""You receive a string consisting of a number between two letters. For the given string,
you should perform different mathematical operations to achieve a result:
•	First, if the letter in front of the number is:
o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
•	Next, if the letter after the number is:
o	Uppercase: subtract its position from the resulting number (starting from 1)
o	Lowercase: add its position to the resulting number (starting from 1)
The game was too easy for John. He decided to complicate it by doing the same calculations to
multiple strings keeping track of only the total sum of all results.
Once he started to solve this with more strings and bigger numbers,
it became quite hard to do it only in his mind.
He kindly asks you to write a program that performs the operations described above and sums the
 final results of each string.
Input
•	The input comes from the console as a single line, holding a sequence of strings
•	Strings are separated by one or more white spaces
•	The input data will always be valid. There is no need to check it explicitly
Output
•	Print at the console a single number:
o	The total sum of all processed numbers, formatted to the second decimal separator"""


data = input().split()
sum_list = []


for sequence in data:
    number = int(sequence[1:-1])
    result_1 = 0
    result_2 = 0

    if sequence[0].isupper():
        first_letter_position = int(ord(sequence[0])) - 64
        result_1 += (number / first_letter_position)
    else:
        first_letter_position = int(ord(sequence[0])) - 96
        result_1 += (number * first_letter_position)

    if sequence[-1].isupper():
        last_letter_position = int(ord(sequence[-1])) - 64
        result_2 = last_letter_position
        total_sum = result_1 - result_2
    else:
        last_letter_position = int(ord(sequence[- 1])) - 96
        result_2 = last_letter_position
        total_sum = result_1 + result_2
    sum_list.append(total_sum)

final_sum = sum(sum_list)
print(f"{final_sum:.2f}")
