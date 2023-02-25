""" Create a program that receives two strings on a single line separated by a single space.
Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0]
and add the result to the total sum, then continue with the next two characters.
If one of the strings is longer than the other, add the remaining character codes
to the total sum without multiplication."""


str_1, str_2 = input().split()
total_sum = 0

if len(str_1) > len(str_2):
    for index in range(len(str_2)):
        total_sum += ord(str_1[index]) * ord(str_2[index])
    for index in range(len(str_2), len(str_1)):
        total_sum += ord(str_1[index])

elif len(str_2) > len(str_1):
    for index in range(len(str_1)):
        total_sum += ord(str_1[index]) * ord(str_2[index])
    for index in range(len(str_1), len(str_2)):
        total_sum += ord(str_2[index])

else:
    for index in range(len(str_1)):
        total_sum += ord(str_1[index]) * ord(str_2[index])

print(total_sum)
