from math import sqrt


class Number:

    def __init__(self, number: int):
        self.number = number

    def increase_with_root(self):
        self.number += self.get_root(self.number)

    @staticmethod
    def get_root(number: int):
        return sqrt(number)

    @classmethod
    def from_float(cls, float_number: float):
        return cls(int(float_number))

    def __repr__(self):
        return f"{self.number}"


a = Number.from_float(121.5)
print(a)

print(a.get_root(49))

a.increase_with_root()
print(a)