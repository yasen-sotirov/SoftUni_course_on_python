number = int(input())
parking = set()

for _ in range(number):
    action, car_number = input().split(", ")
    if action == "IN":
        parking.add(car_number)
    elif action == "OUT":
        parking.remove(car_number)

if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")

