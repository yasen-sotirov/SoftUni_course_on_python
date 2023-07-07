class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]    # the topmost element

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "["+', '.join(reversed(self.data))+"]"


current_stack = Stack()
current_stack.push("A")
current_stack.push("B")
current_stack.push("C")
print(current_stack.is_empty())
print(current_stack.top())
print(current_stack)
print(current_stack.pop())
