"""" Write a function that receives a string and a counter n.
The function should return a new string – the result of repeating
the old string n times. Print the result of the function.
Try using lambda.

abc 3 -> abcabcabc
String 2 -> StringString
"""


def repeat_string(text, number):
    return text * number


income_text = input()
number_of_repetition = int(input())
print(repeat_string(income_text, number_of_repetition))
