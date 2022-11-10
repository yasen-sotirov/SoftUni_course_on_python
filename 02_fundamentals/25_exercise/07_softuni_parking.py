parking = {}
number_of_cars = int(input())

for car in range(number_of_cars):
    current_car = input().split()
    action = current_car[0]
    if action == "register":
        username = current_car[1]
        license_plate_number = current_car[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        username = current_car[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
