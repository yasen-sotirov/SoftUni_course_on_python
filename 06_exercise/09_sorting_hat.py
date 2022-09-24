command = input()
name = ""

while command != "Welcome!":
    name = command
    if name != "Voldemort":
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")
        command = input()
    else:
        print("You must not speak of that name!")
        break
if name != "Voldemort":
    print("Welcome to Hogwarts.")
