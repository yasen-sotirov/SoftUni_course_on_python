""" Problem 2. Mu Online
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2028#1.

You have initial health 100 and initial bitcoins 0.
You will be given a string representing the dungeon's rooms.
Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:

•	"potion"
    o	You are healed with the number in the second part. But your health cannot exceed your initial
        health (100).
    o	First print: "You healed for {amount} hp."
    o	After that, print your current health: "Current health: {health} hp."

•	"chest"
    o	You've found some bitcoins, the number in the second part.
    o	Print: "You found {amount} bitcoins."

•	In any other case, you are facing a monster, which you will fight.
The second part of the room contains the attack of the monster. You should remove the monster's
attack from your health.
    o	If you are not dead (health <= 0), you've slain the monster, and you should print:
        "You slayed {monster}."
    o	If you've died, print "You died! Killed by {monster}." and your quest is over.
        Print the best room you've manage to reach: "Best room: {room}"

    If you managed to go through all the rooms in the dungeon, print on the following three lines:
"You've made it!"
"Bitcoins: {bitcoins}"
"Health: {health}"

    Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".

    Output
Print the corresponding messages described above.

    Examples
    Input
rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000

    Output
You slayed rat.
You slayed bat.
You healed for 10 hp.
Current health: 80 hp.
You slayed rat.
You found 100 bitcoins.
You died! Killed by boss.
Best room: 6

    Input
cat 10|potion 30|orc 10|chest 10|snake 25|chest 110

    Output
You slayed cat.
You healed for 10 hp.
Current health: 100 hp.
You slayed orc.
You found 10 bitcoins.
You slayed snake.
You found 110 bitcoins.
You've made it!
Bitcoins: 120
Health: 65
"""


health = 100
bitcoins = 0
last_monster = ''
best_room = 0
is_alive = True

rooms = input().split('|')
for current_room in rooms:
    action, points = current_room.split()
    points = int(points)
    best_room += 1

    if action == "potion":
        if health + points < 100:
            health += points
            print(f"You healed for {points} hp.")
            print(f"Current health: {health} hp.")

        elif health + points >= 100:
            difference = 100 - health
            health = 100
            print(f"You healed for {difference} hp.")
            print(f"Current health: 100 hp.")

    elif action == "chest":
        bitcoins += points
        print(f'You found {points} bitcoins.')

    else:
        last_monster = action
        health -= points
        if health <= 0:
            print(f"You died! Killed by {last_monster}.")
            print(f"Best room: {best_room}")
            is_alive = False
            break
        else:
            print(f"You slayed {last_monster}.")

if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
