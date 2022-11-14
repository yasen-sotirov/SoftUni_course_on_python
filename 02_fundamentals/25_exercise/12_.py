"""" You will be receiving lines in the following format:
"{username}-{language}-{points}" until you receive "exam finished".
You should store each username and their submissions and points.
If a student has two or more submissions for the same language,
save only his maximum points.
You can receive a command to ban a user for cheating in the following format:
"{username}-banned". In that case, you should remove the user from the contest
but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions
in the following format: "{username}-{language}-{points}"
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant
•	After that, print each language in the format shown above
•	Allowed working time / memory: 100ms / 16MB
"""


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
