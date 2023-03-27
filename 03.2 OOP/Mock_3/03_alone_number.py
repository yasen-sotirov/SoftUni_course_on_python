""" Alone Numbers
We will give you array and a target! You need to find all "alone" elements in the array that
match the given target. These elements are alone if they have values before and after them,
but those values are different from them.
Return new version of the given array where every element that matches
the target and is alone is replaced by whichever value to its left or right is larger.
Input

Read from the standard input:

    The first line is the array with coma separated integer values -> 1,2,3
    The second line is the target that you should check against -> 2

Output

Print to the standard output:

    One line of output - the changed array -> [1, 3, 3]
    please note that there is space after each coma.

Sample Tests
Input
1, 2, 3
2
Output
[1, 3, 3]

Input
1, 2, 3, 2, 5, 2
2

Output
[1, 3, 3, 5, 5, 2]
"""

changed_list = []
data_array = [int(x) for x in input().split(", ")]
target = int(input())

for index, num in enumerate(data_array):

    if num == target and \
            index != 0 and \
            index != len(data_array) - 1 and \
            num != data_array[index - 1] and \
            num != data_array[index + 1]:

        if index == 0 and data_array[index + 1] > target:
            changed_list.append(data_array[index + 1])

        elif index == len(data_array) - 1 and  data_array[index - 1] > target:
            changed_list.append(data_array[index - 1])

        else:
            if data_array[index - 1] > data_array[index + 1]:
                changed_list.append(data_array[index - 1])
            else:
                changed_list.append(data_array[index + 1])

    else:
        changed_list.append(num)

print(changed_list)
