from section import Section
from task import Task

first_task = Task("Make bed", "27/05/2020")
print(first_task.change_name("Go to University"))
print(first_task.change_due_date("28.05.2020"))
first_task.add_comment("Don't forget laptop")
print(first_task.edit_comment(0, "Don't forget laptop and notebook"))
print(first_task.details())
section = Section("Daily tasks")
print(section.add_task(first_task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())