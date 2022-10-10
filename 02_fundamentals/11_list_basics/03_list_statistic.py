""" On the first line, you will receive a number n.
On the following n lines, you will receive integers.
You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message:
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"
"""


number_of_lines = int(input())
positive_number = []
negative_number = []

for _ in range(number_of_lines):
    current_number = int(input())

    if current_number >= 0:
        positive_number.append(current_number)
    else:
        negative_number.append(current_number)

print(positive_number)
print(negative_number)

print(f"Count of positives: {len(positive_number)}")
print(f"Sum of negatives: {sum(negative_number)}")
 