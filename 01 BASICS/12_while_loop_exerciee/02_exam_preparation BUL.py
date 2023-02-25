max_bad_grade = int(input())
average_grade = 0
total_problems = 0
last_problem_name = ''
bad_grade_counter = 0
is_expelled = False

current_problem = input()

while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == max_bad_grade:
            is_expelled = True
            break
    average_grade += current_grade
    total_problems += 1
    last_problem_name = current_problem
    current_problem = input()

if is_expelled: #if is_expelled == True  или  if bad_grade_counter == max_bad_grade
    print(f'You need a break, {max_bad_grade} poor grades.')
else:
    average_grade /= total_problems
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {total_problems}')
    print(f'Last problem: {last_problem_name}')
