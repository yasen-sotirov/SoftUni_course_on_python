from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."


current_sports_car = SportsCar()
print(current_sports_car.move())
print(current_sports_car.drive())
print(current_sports_car.race())

