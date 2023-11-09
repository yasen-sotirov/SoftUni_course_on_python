from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents_list = {
    "Doll": [0, 150],
    "Wooden train": [0, 250],
    "Teddy bear": [0, 300],
    "Bicycle": [0, 400]
}


while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    product = current_material * current_magic

    if materials == 0 and magic == 0:
        continue

    if product < 0:
        sum_values = current_material + current_magic
        materials.append(sum_values)

    else:
        present_is_found = False
        for gift, data in presents_list.items():
            magic_price = data[1]
            if magic_price == product:
                presents_list[gift][0] += 1
                present_is_found = True
                break

        if not present_is_found:
            materials.append(current_material + 15)

if (presents_list["Doll"][0] > 0 and presents_list["Wooden train"][0] > 0) or \
        (presents_list["Teddy bear"][0] > 0 and presents_list["Bicycle"][0] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join(str(el) for el in materials)}')
if magic:
    print(f"Magic left: {', '.join(str(el) for el in magic)}")

for toy, value in sorted(presents_list.items()):
    if value[0] > 0:
        print(f"{toy}: {value[0]}")
