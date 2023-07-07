def flights(*args):
    flight_list = {}
    from collections import deque
    all_flights = deque(args)
    while True:
        destination = all_flights.popleft()
        if destination == "Finish":
            break
        else:
            passengers = all_flights.popleft()
            if destination not in flight_list:
                flight_list[destination] = passengers
            else:
                flight_list[destination] += passengers

    return flight_list


# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
