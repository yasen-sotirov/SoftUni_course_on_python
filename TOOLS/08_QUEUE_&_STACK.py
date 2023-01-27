"QUEUES"        # опашки, линеина структура
                # може да се използва като стек, но с .pop(), ако искаме да го въртим
                # Doubly Linked List
                # push - append
                # pull - popleft
                # peek - deque[0]

from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
my_deque.append(3)
my_deque.append(4)

# parentheses = deque(input())
# print(parentheses)

"ПОКАЗВА ПРЕМАХНАТИЯ ЕЛЕМЕНТ"
# print(my_deque.popleft())
# print(my_deque.popleft())


"ДОБАВЯ В НАЧАЛОТО"
# print(my_deque)
# my_deque.appendleft(0)
# my_deque.appendleft(0)
# print(my_deque)


"ПРЕМАХВА ПЪРВИЯ ЕЛЕМЕНТ"
# print(my_deque)
# my_deque.popleft()
# my_deque.popleft()
# print(my_deque)


"ПРЕМАХВА ПОСЛЕДНИЯ ЕЛЕМЕНТ"
# print(my_deque)
# my_deque.pop()
# my_deque.pop()
# print(my_deque)


"ВЪРТИ ОПАШКАТА"        # последният минава най-отпред
# print(my_deque)
# my_deque.rotate()     # с 1 позиция
# print(my_deque)

# print(my_deque)         # с 2 позиции
# my_deque.rotate(2)
# print(my_deque)

# print(my_deque)         # в обратен ред
# my_deque.rotate(-1)
# print(my_deque)



"ОБРЪЩА ОПАШКАТА"
# print(my_deque)
# my_deque.reverse()
# print(my_deque)


"БРОЙ „Х“ ЕЛЕМЕНТИТЕ"
# print(my_deque)
# print(my_deque.count(3))


"ДОБАВЯ ЕЛЕМЕНТ В НАЧАЛОТО"
# print(my_deque)
# my_deque.appendleft(0)
# print(my_deque)





"STACKS"    # стек - за основа ползваме лист
            # LIFO
            # push - append
            # pull - pop
            # peek - stack[-1]

"PUSH = .append()"
"RETRIEVING = .pop()"

# stack = []
# print(stack)
# stack.append(5)
# stack.append(6)
# print(stack)
# stack.pop()
# print(stack)


