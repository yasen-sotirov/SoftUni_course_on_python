"""" Write a program that keeps the information about students and their grades.
On the first line, you will receive an integer number representing the next pair of rows.
On the next lines, you will be receiving each student's name and their grade.
Keep track of all grades for each student and keep only the students with an average grade higher than
or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
"""


number_of_student = int(input())
students_dictionary = {}

for current_student in range(number_of_student):
    name = input()
    grade = float(input())
    if name not in students_dictionary:
        students_dictionary[name] = []
    students_dictionary[name].append(grade)

for name, grade in students_dictionary.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
