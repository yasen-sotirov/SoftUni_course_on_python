number = float(input())

while 1 > number and 100 > number:
    number = float(input())
else:
    print(f"The number {number} is between 1 and 100")
