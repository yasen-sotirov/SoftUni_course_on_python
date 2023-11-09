from collections import deque


def check_gifts_table(score):
    for key in gift_list:
        if gift_list[key](score) is not None:
            if key not in crafted_gifts:
                crafted_gifts[key] = 0
            crafted_gifts[key] += 1
            return True
    else:
        return False


materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gift_list = {
    "Gemstone": lambda x: x if 100 <= x <= 199 else None,
    "Porcelain Sculpture": lambda x: x if 200 <= x <= 299 else None,
    "Gold": lambda x: x if 300 <= x <= 399 else None,
    "Diamond Jewellery": lambda x: x if 400 <= x <= 499 else None
}
crafted_gifts = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    current_score = current_material + current_magic

    if 100 <= current_score <= 499:
        check_gifts_table(current_score)
        continue

    else:
        if current_score < 100:
            if current_score % 2 == 0:
                current_score = current_material * 2 + current_magic * 3
            else:
                current_score *= 2
        elif current_score > 499:
            current_score //= 2

        check_gifts_table(current_score)

if {"Gemstone", "Porcelain Sculpture"}.issubset(set(crafted_gifts.keys())) or \
        {"Gold", "Diamond Jewellery"}.issubset(set(crafted_gifts.keys())):
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key in sorted(crafted_gifts):
    print(f"{key}: {crafted_gifts[key]}")


