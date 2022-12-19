""" Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2474#0.

Every day, thousands of students pass by the reception at SoftUni with different questions to ask.
The employees have to help everyone by providing all the information and answering all of the questions.
Three employees are working on the reception all day. Each of them can handle a different number of
students per hour. Your task is to calculate how much time it will take to answer all the questions
of a given number of students.

First, you will receive 3 lines with integers, representing the number of students that each employee
can help per hour. On the following line, you will receive students count as a single integer.
Every fourth hour, all employees have a break, so they don't work for an hour.
It is the only break for the employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."

Input / Constraints
•	On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
•	On the fourth line - students count – integer in the range [0 – 10000]
•	Input will always be valid and in the range specified

Output
•	Print a single line: "Time needed: {time}h."
•	Allowed working time / memory: 100ms / 16MB

    Examples
    Input
5
6
4
20

    Output
    Time needed: 2h.

    Comment
All employees can answer 15 students per hour. After the first hour, there are 5 students left to be answered.
All students will be answered in the second hour.

Input
1
2
3
45

Output
Time needed: 10h.

Comment
All employees can answer 6 students per hour. In the first 3 hours, they have answered 6 * 3 = 18 students. Then they have a break for an hour.
After the next 3 hours, there are
18 + 6 * 3 = 36 answered students.
After the break for an hour, there are only 9 students to answer.
So in the 10th hour, all of the student's questions would be answered.

 """

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
number_of_students = int(input())

hours_counter = 0
rests = 0
efficiency = employee_1 + employee_2 + employee_3

while number_of_students > 0:
    number_of_students -= efficiency
    hours_counter += 1
    if number_of_students > 0:
        if hours_counter % 3 == 0:
            rests += 1
print(f"Time needed: {hours_counter + rests}h.")
