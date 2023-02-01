""" 11.	*Math Operations
Write a function named math_operations that receives a different number of floats as arguments and 4 keyword arguments. The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
You need to take each float argument from the sequence and do mathematical operations as follows:
•	The first element should be added to the value of the key "a"
•	The second element should be subtracted from the value of the key "s"
•	The third element should be divisor to the value of the key "d"
•	The fourth element should be multiplied by the value of the key "m"
•	Each result should replace the value of the corresponding key
•	You must repeat the same steps consecutively until you run out of numbers
Beware: You cannot divide by 0. If the operation could throw an error, you should skip the operation and continue to the next one.
After you finish calculating all numbers, sort the four elements by their values in descending order. If two or more values are equal, sort them by their keys in ascending order (alphabetically).
In the end, return each key-value pair in the format "{key}: {value}" on separate lines. Each value should be formatted to the first decimal point.
For more clarifications, see the examples below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
•	All of the given numbers will be valid integers in the range [-100, 100]
Output
•	The function should return the final dictionary

Examples


    Test Code
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

    Output
d: 33.0
s: 15.1
a: 9.1
m: -58.5

"""

from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)

    while nums:
        kwargs["a"] += nums.popleft()
        if nums == 0:
            break

        kwargs["s"] -= nums.popleft()
        if nums == 0:
            break

        divider = nums.popleft()
        if divider != 0:
            kwargs["d"] /= divider
        else:
            continue

        kwargs["m"] *= nums.popleft()
        if nums == 0:
            break
    return nums


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
