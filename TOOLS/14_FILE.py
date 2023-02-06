"FILE HENDLING"  #

file_1 = open("example.txt")
file_2 = open("../../python_course_softuni/03.1_advanced/15_file_handling/text.txt") # релативен път



"ЧЕТЕНЕ НА ФАИЛ"                # в горната директория - релативен път
# print(file_1.readline())      # връща само първи ред
# print(file_2.readlines())     # връща list като всеки ред е отделен лист

# print(file_2.read())    # връща string на целия текст от файла

# print(file_2.read(10))  # връща string с първите „n“ bytes
# print(file_2.read(10))  # връща следващите „n“ bytes
# print(file_2.read())    # връща „n“ bytes до края на текста


# with open("my_first_file.txt", "a") as file:
#     file.writelines('I just created my first file!\n')


"ДОПИСВА КЪМ ФАЙЛ"
# with open("my_first_file.txt", "a") as file:
#     file.writelines('I just append to my first file!\n')


"ПРЕНАПИСВАНЕ НА ФАЙЛ"
# with open("my_first_file.txt", "w") as file:
#     file.writelines('I just REWRITE my first file!\n')



"ЗАТВАРЯНЕ НА ФАЙЛ"
# with open("text.txt") as file_2:        # затваря файла след края на код-блока
#     print(file_2.read())

# file_1.close()      # слага се в края на код блока



"ТРИЕ ФАЙЛ"
# import os
# if os.path.exists("my_first_file.txt"):
#     os.remove("my_first_file.txt")
# else:
#     print('File already deleted!')



"АБСОЛЮТЕН ПЪТ"
# import os       #


"ДАЛИ ФАЙЛА СЪЩЕСТВУВА"
# from os import path
# if not path.exists("file.txt"):
#     print("An error occurred")


"МЕСТИ КУРСОРА ВЪВ .txt ФАЙЛА"
# file.seek(2)

"ТРИЕ СЛЕД КУРСОРА ВЪВ .txt ФАЙЛА"
# file.truncate(15)


"ПОКАЗВА ВСИЧКИ ЕЛЕМЕНТИ В ТЕКУЩАТА ПАПКА"
# from os import listdir
# print(listdir("."))


"ПРОВЕРЯВА ФАЛИ ЕЛЕМЕНТА Е ДИРЕКТОРИЯ"
from os import path
print(path.isdir(file_1))