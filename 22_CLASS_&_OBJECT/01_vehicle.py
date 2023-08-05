class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


my_first_car = Vehicle(20)
print(my_first_car.max_speed)
print(my_first_car.mileage)
print(my_first_car.gadgets)
my_first_car.gadgets.append('Hudly Wireless')
print(my_first_car.gadgets)
