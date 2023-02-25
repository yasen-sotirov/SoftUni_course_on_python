# Трябва да импортирам числото ПИ
from math import pi, floor

# Трябва да прочета входа за радиани - floating
radians = float(input())
# трябва да пресметна градусите
degree = radians * 180 / pi
# Трябва да отпечатам градусите
print(degree)
