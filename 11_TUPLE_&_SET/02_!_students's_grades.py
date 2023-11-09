
n = int(input())
grades_dict = {}

for _ in range(n):
    name, grade_as_string = input().split()
    current_grade = float(grade_as_string)
    if name not in grades_dict:
        grades_dict[name] = []
    grades_dict[name].append(current_grade)

for tuple in grades_dict.items():
    print(f"{tuple[0]} -> {' '.join([f'{el:.2f}' for el in tuple[1]])} "
          f"(avg: {(sum(tuple[1])/len(tuple[1])):.2f})")
