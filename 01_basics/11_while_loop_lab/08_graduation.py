name = input()
year_counter = 0
low_grade = 0
grade_counter = 0
average_grade = 0

while True:
    annual_grade = float(input())
    year_counter += 1

    if annual_grade < 4:
        low_grade += 1
        if low_grade == 2:
            print(f"{name} has been excluded at {year_counter} grade")
            break
        year_counter -= 1

    else:
        grade_counter += annual_grade

    if year_counter == 12:
        average_grade = grade_counter / year_counter
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
