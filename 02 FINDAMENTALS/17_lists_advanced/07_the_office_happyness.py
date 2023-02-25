"""" You will receive two lines of input:
•	a list of employees' happiness as a string of numbers separated by a single space
•	a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•	If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
"""


nums = [int(el) for el in input().split()]
factor = int(input())

happiness = [el*factor for el in nums]
average_happiness = sum(happiness) / len(nums)
half = len(nums)/ 2
total_happy = [el for el in happiness if el >= average_happiness]

if len(total_happy) < half:
    print(f"Score: {len(total_happy)}/{len(nums)}. Employees are not happy!")
else:
    print(f"Score: {len(total_happy)}/{len(nums)}. Employees are happy!")
