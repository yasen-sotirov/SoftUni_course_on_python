"""" Create a function that calculates and returns the area
of a rectangle by given width and height.
Print the result on the console."""


def area(w, h):
    return w * h


width = int(input())
heigth = int(input())
print(area(width, heigth))

print(area(6, 8))
print(area(7, 8))
