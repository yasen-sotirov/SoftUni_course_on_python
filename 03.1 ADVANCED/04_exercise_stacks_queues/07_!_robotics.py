""" 7.	*Robotics
There is a robotics factory. The current 08_pokemon_battle is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product,
and processing start time.
Each robot processes a product coming from the assembly line.
A product is coming from the line each second (so the 1st product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it,
it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.

Input
•	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.

Output
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

Examples
    Input
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

    Output
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]

 """

from collections import deque


def convert_str_to_sec(str_time):
    hours, minutes, sec = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + sec


def convert_seconds_to_str_time(total_sec):
    total_sec %= 24 * 60 * 60
    hours = total_sec // (60 * 60)
    minutes = total_sec // 60
    seconds = total_sec % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robot_data = input().split(';')
process_time_per_robot = {}
busy_until_by_robot = {}
items = deque()

for robot in robot_data:
    name, process_time = robot.split("-")
    process_time_per_robot[name] = int(process_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_sec(input())

while True:
    products = input()
    if products == "End":
        break
    items.append(products)

while items:
    time += 1
    current_item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_per_robot[name]
            print(f'{name} - {current_item} [{convert_seconds_to_str_time(time)}]')
            break
    else:
        items.append(current_item)
