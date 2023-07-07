""" On the first line, you will receive a single number n.
On the following n lines, you will receive names of courses.
You should create a list of courses and print it."""


number_of_lines = int(input())
course_list = []

for row in range(number_of_lines):
    current_name = input()
    course_list.append(current_name)

print(course_list)
 