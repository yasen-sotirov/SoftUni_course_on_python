number_of_students = int(input())
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
sum_grade = 0

for i in range(number_of_students):
    exam_grade = float(input())
    sum_grade += exam_grade
    if exam_grade < 3:
        counter_2 += 1
    elif exam_grade < 4:
        counter_3 += 1
    elif exam_grade < 5:
        counter_4 += 1
    else:
        counter_5 += 1

percentage_2 = counter_2 / number_of_students * 100
percentage_3 = counter_3 / number_of_students * 100
percentage_4 = counter_4 / number_of_students * 100
percentage_5 = counter_5 / number_of_students * 100
average_score = sum_grade / number_of_students

print(f"Top students: {percentage_5:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3:.2f}%")
print(f"Fail: {percentage_2:.2f}%")
print(f"Average: {average_score:.2f}")
