""" Hot Potato is a game in which children form a circle and toss a hot potato.
The counting starts with the first kid. Every nth toss,
the child holding the potato leaves the game.
When a kid leaves the game, it passes the potato to the next kid.
It continues until there is only one kid left.
Create a program that simulates the game of Hot Potato.
On the first line, you will receive kids' names, separated by a single space.
On the second line, you will receive the nth toss (integer) in which a child leaves the game.
Print every kid who is removed from the circle in the format "Removed {kid}".
In the end, print the only kid left in the format "Last is {kid}".

    Examples
    Input
Tracy Emily Daniel
2

    Output
Removed Emily
Removed Tracy
Last is Daniel


    Input
George Peter Michael William Thomas
10

    Output
Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William

 """


from collections import deque

kids_queue = deque(input().split())
numer_of_rotation = int(input())

while len(kids_queue) > 1:
    kids_queue.rotate(-numer_of_rotation)
    print(f'Removed {kids_queue.pop()}')

print(f'Last is {kids_queue.pop()}')
