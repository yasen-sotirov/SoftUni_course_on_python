from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

items_dict = {"Patch": 30, "Bandage": 40, "MedKit": 100}
created_items = {}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    current_item = current_textile + current_medicament

    if current_item > 100:
        created_items["MedKit"] += 1
        rest = current_item - 100
        medicaments[-1] += rest

    elif current_item not in (30, 40, 100):
        current_medicament += 10
        medicaments.append(current_medicament)

    for key in items_dict:
        if current_item == items_dict[key]:
            if key not in created_items:
                created_items[key] = 0
            created_items[key] += 1

if not textiles and medicaments:
    print("Textiles are empty.")
if textiles and not medicaments:
    print("Medicaments are empty.")
if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

if created_items:
    for key, value in sorted(created_items.items(), key=lambda x: (- x[1], x[0])):
        print(f"{key} - {value}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
