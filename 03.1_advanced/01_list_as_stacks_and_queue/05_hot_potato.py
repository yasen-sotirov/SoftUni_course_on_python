from collections import deque

kids_queue = deque(input().split())
numer_of_rotation = int(input())

while len(kids_queue) > 1:
    kids_queue.rotate(-numer_of_rotation)
    print(f'Removed {kids_queue.pop()}')

print(f'Last is {kids_queue.pop()}')
