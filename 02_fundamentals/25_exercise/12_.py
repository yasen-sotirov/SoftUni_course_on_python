student_dictionary = {}
banned_students = []
language_dict = {}

while True:
    command = input()
    if "exam finished" in command:
        break

    elif "banned" in command:
        username = command.split("-")
        banned_students.append(username[0])
        break

    username, language, points = command.split("-")
    if username not in student_dictionary:
        student_dictionary[username] = 0
    if student_dictionary[username] < int(points):
        student_dictionary[username] = int(points)
    if language not in language_dict:
        language_dict[language] = 0
    language_dict[language] += 1

print("Results:")
for student, grade in student_dictionary.items():
    if student not in banned_students:
        print(f"{student} | {grade}")

print("Submissions:")
for language, number_of_students in language_dict.items():
    print(f"{language} - {number_of_students}")
