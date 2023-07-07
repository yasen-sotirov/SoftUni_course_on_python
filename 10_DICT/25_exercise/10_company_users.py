"""" Write a program that keeps the information about companies and their employees.
You will be receiving company names and an employees' id until you receive the command "End" command.
Add each employee to the given company.
Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format:
"{company_name} -> {employee_id}".
•	The input always will be valid.
"""


dictionary = {}

while True:
    command = input()
    if "End" in command:
        break

    company_name, employees_id = command.split(" -> ")
    if company_name not in dictionary.keys():
        dictionary[company_name] = []
    if employees_id not in dictionary[company_name]:
        dictionary[company_name].append(employees_id)

for company_name, employees_id in dictionary.items():
    print(company_name)
    for employees_id in dictionary[company_name]:
        print(f"-- {employees_id}")
