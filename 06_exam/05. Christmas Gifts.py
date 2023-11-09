command = input()
adults_counter = 0
kids_counter = 0
sum_toys = 0
sum_sweaters = 0

while command != "Christmas":
    years = int(command)
    if years <= 16:
        sum_toys += 5
        kids_counter += 1
    else:
        sum_sweaters += 15
        adults_counter += 1
    command = input()

print(f"Number of adults: {adults_counter}")
print(f"Number of kids: {kids_counter}")
print(f"Money for toys: {sum_toys:.0f}")
print(f"Money for sweaters: {sum_sweaters:.0f}")
