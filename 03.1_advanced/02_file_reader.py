""" 2.	File Reader
You are given a file called numbers.txt with the following content:

Create a program that reads the numbers from the file.
Print on the console the sum of those numbers.
"""


try:
    with open("numbers.txt") as file:
        result = 0
        for line in file.readlines():     # readlines() може да се изпусне
            current_num = int(line)
            result += current_num
        print(result)

        # print(sum([int(line_nums) for line_nums in file.readline().split()]))   # ако е на един ред
except FileNotFoundError:
    print("File was not found")

