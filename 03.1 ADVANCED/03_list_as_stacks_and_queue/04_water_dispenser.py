""" 4.	Water Dispenser
Write a program that keeps track of people getting water from a dispenser and
the amount of water left at the end.
On the first line, you will receive the starting quantity of water (integer) in a dispenser.
Then, on the following lines, you will be given the names of some people who want to get
water (each on a separate line) until you receive the command "Start". A
dd those people in a queue.
Finally, you will receive some commands until the command "End":

-	"{liters}" - litters (integer) that the current person in the queue wants to get.
Check if there is enough water in the dispenser for that person.
o	If there is enough water, print "{person_name} got water" and remove him/her
    from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person from the queue
    without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.

In the end, print how many liters of water have left in the format:
"{left_liters} liters left".

    Examples
    Input
10
Peter
George
Amy
Alice
Start
2
3
3
3
End

    Output
Peter got water
George got water
Amy got water
Alice must wait
2 liters left
"""


from collections import deque

quantity_of_water = int(input())
name = input()
line = deque()

while not name == "Start":
    line.append(name)
    name = input()

command = input()

while not command == "End":
    if command.isdigit():
        needed_water = int(command)
        if needed_water > quantity_of_water:
            print(f"{line.popleft()} must wait")
        else:
            print(f"{line.popleft()} got water")
            quantity_of_water -= needed_water
    else:
        _, new_water = command.split()
        quantity_of_water += int(new_water)

    command = input()

print(f"{quantity_of_water} liters left")