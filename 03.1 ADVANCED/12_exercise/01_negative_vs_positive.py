""" 1.	Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space.
Separate the negative numbers from the positive.
Find the total sum of the negatives and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
    o	If the absolute negative number is larger than the positive number:
	    "The negatives are stronger than the positives"
    o	If the positive number is larger than the absolute negative number:
	    "The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

Example

Input
1 2 -3 -4 65 -98 12 57 -84

Output
-189
137
The negatives are stronger than the positives

"""


number_sequence = [int(el) for el in input().split()]

negative_number = sum(x for x in number_sequence if x < 0)
positive_number = sum(x for x in number_sequence if x > 0)

print(negative_number)
print(positive_number)

if abs(negative_number) > positive_number:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

