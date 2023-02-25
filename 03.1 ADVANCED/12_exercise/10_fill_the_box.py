""" 10.	*Fill the Box
Write a function called fill_the_box that receives a different number of arguments representing:
•	the height of a box
•	the length of a box
•	the width of a box
•	n-times a different number of cubes with exact size 1 x 1 x 1
•	a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.

    Output
    The function should return a string in the following format:
•	If, at the end, there is free space left in the box, print:
    o	"There is free space in the box. You could put {free space in cubes} more cubes."
•	If there is no free space in the box, print:
    o	"No more free space! You have {cubes left} more cubes."

    Examples
    Test Code
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

    Output
There is free space in the box. You could put 13 more cubes.

    Comment
The size of the box: 2 * 8 * 2 = 32
We put the cubes consistently. At the end there is more free space left.

"""


def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes_left = 0

    for element in args:
        if element == "Finish":
            break

        if element > volume:
            element -= volume
            cubes_left += element
            volume = 0
        else:
            volume -= element

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))