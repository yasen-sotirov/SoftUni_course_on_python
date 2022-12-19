""" Problem 2 - Array Modifier
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2474#1.

You are given an array with integers.
Write a program to modify the elements after receiving the following commands:
•	"swap {index1} {index2}" takes two elements and swap their places.
•	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
•	"decrease" decreases all elements in the array with 1.

    Input
On the first input line, you will be given the initial array values separated by a single space.
On the next lines you will receive commands until you receive the command "end". The commands are as follow:
•	"swap {index1} {index2}"
•	"multiply {index1} {index2}"
•	"decrease"

    Output
The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".

    Constraints
•	Elements of the array will be integer numbers in the range [-231...231]
•	Count of the array elements will be in the range [2...100]
•	Indexes will be always in the range of the array

    Examples
    Input
23 -2 321 87 42 90 -123
swap 1 3
swap 3 6
swap 1 0
multiply 1 2
multiply 2 1
decrease
end

    Output
86, 7382, 2369942, -124, 41, 89, -3

    Comments
23 -2 321 87 42 90 -123 – initial values
swap 1(-2) and 3(87) ▼
23 87 321 -2 42 90 -123
swap 3(-2) and 6(-123) ▼
23 87 321 -123 42 90 -2
swap 1(87) and 0(23) ▼
87 23 321 -123 42 90 -2
multiply 1(23) 2(321) = 7383 ▼
87 7383 321 -123 42 290 -2
multiply 2(321) 1(7383) = 2369943 ▼
87 7383 2369943 -123 42 90 -2
decrease – all - 1 ▼
86 7383 2369942 -124 41 89 -3

 """

array = [int(el) for el in input().split()]
while True:
    command = input()
    if command == "end":
        break

    elif "swap" in command:
        command = command.split()
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]

    elif "multiply" in command:
        command = command.split()
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1] = array[index_1] * array[index_2]

    elif "decrease" in command:
        for index in range(len(array)):
            array[index] = array[index] - 1

array_as_str = [str(el) for el in array]
print(", ".join(array_as_str))
