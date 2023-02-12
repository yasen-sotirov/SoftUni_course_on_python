""" 5. Truck Tour
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive).
For each petrol pump, you will receive two pieces of information (separated by a single space):
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle.
You know that the truck consumes 1 liter of petrol per 1 kilometer,
and its tank has infinite petrol capacity.

In the beginning, the tank is empty, but you start your journey at a petrol pump
so you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle.
You never miss filling its tank at a petrol pump.

Input
•	On the first line, you will receive the number of petrol pumps - N
•	On the next N lines, you will receive the amount of petrol that each petrol pump will give
    and the distance between that petrol pump and the next petrol pump, separated by a single space

Output
•	An integer which will be the smallest index of a petrol pump from which you can start the tour

Constraints
•	1 ≤ N ≤ 1000001
•	1 ≤ amount of petrol, distance ≤ 1000000000
•	You will always have at least one point from where the truck will be able to complete the circle

Examples
Input
3
1 5
10 3
3 4

Output
1

 """
from collections import deque

# pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
#
# pumps_data_copy = pumps_data.copy()
# index = 0
# gas_in_tank = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#
#     gas_in_tank += petrol
#
#     if gas_in_tank - distance < 0:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         index += 1
#         gas_in_tank = 0
#     else:
#         gas_in_tank -= distance
#
# print(index)


stations = int(input())
pumps_data = deque()
counter = 0

for _ in range(stations):
    data = [int(el) for el in input().split()]
    pumps_data.append(data)

race_failed = False
tank = 0

for start_index in range(stations):
    for current_station in pumps_data:
        petrol, distance = current_station
        tank += petrol
        if tank < distance:
            race_failed = True
            pumps_data.rotate(-1)
            break

if race_failed:
    pumps_data.rotate(-1)
    counter += 1

print(counter)

