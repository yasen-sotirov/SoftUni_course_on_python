class Party:
    def __init__(self):
        self.people = []


my_party = Party()

gest_name = input()

while not gest_name == "End":
    my_party.people.append(gest_name)
    gest_name = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
