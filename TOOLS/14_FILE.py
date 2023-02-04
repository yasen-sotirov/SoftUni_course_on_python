"FILE HENDLING"  #

file_1 = open("example.txt")
file_2 = open("../../python_course_softuni/03.1_advanced/15_file_handling/text.txt") # релативен път



"ЧЕТЕНЕ НА ФАИЛ"                # в горната директория - релативен път
# print(file_1.readline())        # връща само първи ред
# print(file_2.readlines())     # връща list като всеки ред е отделен лист

# print(file_2.read())    # връща string

# print(file_2.read(10))  # връща string с първите „n“ bytes
# print(file_2.read(10))  # връща следващите „n“ bytes
# print(file_2.read())    # връща „n“ bytes до края на текста


"ЗАТВАРЯНЕ НА ФАЙЛ"
# with open("text.txt") as file_2:        # затваря файла след края на код-блока
#     print(file_2.read())

# file_1.close()      # слага се в края на код блока


"АБСОЛЮТЕН ПЪТ"
# import os       #
