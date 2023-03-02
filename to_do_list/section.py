from to_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            found_task = next(filter(lambda t: t.name == task_name, self.tasks))

        except StopIteration:
            return f"Could not find task with the name {task_name}"

        found_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for current_task in filter(lambda t: t.completed, self.tasks):
            self.tasks.remove(current_task)
            cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        # output = [f'Section {self.name}:']
        # [output.append(t.details()) for t in self.tasks]
        # return '\n'.join(output)
        result = f'Section {self.name}:'
        for task in self.tasks:
            result += '\n' + task.details()
        return result



