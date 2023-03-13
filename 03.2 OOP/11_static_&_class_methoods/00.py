import math
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y) ** 2)

    @staticmethod
    def calc(point_1, point_2):
        return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y) ** 2)


p1 = Point(5, 6)
p2 = Point(3, 4)

p1.calculate_distance(p2)
Point.calc(p1, p2)
