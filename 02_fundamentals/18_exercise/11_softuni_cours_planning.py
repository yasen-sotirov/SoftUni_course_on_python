def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:
                list_of_lessons.pop(title_index + 1)
    return list_of_lessons


def swap_lessons(list_of_lessons, title):
    return list_of_lessons


def exercise(list_of_lessons, title):
    return list_of_lessons


lessons = input().split(", ")
command = input().split(':')

while len(command) > 1:  # while command[0] != 'course start'
    action = command[0]
    lesson_title = command[1]
    if len(lessons) > 2:
        lesson_title_or_index = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)

    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, lesson_title_or_index)

    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)

    elif action == "Swap":
        lessons = swap_lessons(lessons, lesson_title, lesson_title_or_index)

    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input().split(':')
