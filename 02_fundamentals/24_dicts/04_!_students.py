"""" You will be receiving names of students, their ID, and a course of programming they
have taken in the format "{name}:{ID}:{course}". On the last line, you will receive
a name of a course in snake case lowercase letters. You should print only the information
of the students who have taken the corresponding course in the format: "{name} - {ID}"
on separate lines. """


command = input()
courses_list = {}

while ":" in command:
    student_name, student_id, course_name = command.split(":")
    if course_name not in courses_list:
        courses_list[course_name] = {}
    courses_list[course_name][student_id] = student_name

    command = input()

searched_course = command
searched_course_name_as_list = searched_course.split("_")
searched_course = ' '.join(searched_course_name_as_list)

for course_name in courses_list:
    if course_name == searched_course:
        for student_id, name in courses_list[course_name].items():
            print(f"{name} - {student_id}")
