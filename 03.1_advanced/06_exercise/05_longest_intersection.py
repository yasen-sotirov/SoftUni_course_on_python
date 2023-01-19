""" 5.	Longest Intersection
Write a program that finds the longest intersection. You will be given a number N.
On each of the next N lines you will be given two ranges in the format:
"{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these
two ranges. The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections,
print the numbers that are included and its length in the format:
"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection.
If there are two equal intersections, print the first one.

    Examples
    Input
3
0,3-1,2
2,10-3,5
6,15-3,10

    Output
Longest intersection is [6, 7, 8, 9, 10] with length 5

    Comment
The intersection of [0-3] and [1-2] is [1-2] (length 2)
The intersection of [2-10] and [3-5] is [3-5] (length 3)
The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest
"""


def gen_of_sequence(range_info):
    start, end = [int(el) for el in range_info.split(",")]
    return set(range(start, end + 1))


number_of_lines = int(input())
all_intersections = {}
best_intersection = set()

for _ in range(number_of_lines):
    line_parts = input().split('-')
    first_set = gen_of_sequence(line_parts[0])
    second_set = gen_of_sequence(line_parts[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(el) for el in best_intersection])}] with length {len(best_intersection)}")
