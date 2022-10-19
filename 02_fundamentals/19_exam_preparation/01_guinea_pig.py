# https://pastebin.com/x4rX7btp

food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

enough_supply = True

for day in range(1, 31):
    if not enough_supply:
        print("Merry must go to the pet store!")
        break
    else:
        food -= 0.3
        if not food > 0:
            enough_supply = False

        if day % 2 == 0:
            hay -= food * 0.05
            if not hay > 0:
                enough_supply = False

        if day % 3 == 0:
            cover -= weight / 3
            if not cover > 0:
                enough_supply = False

if enough_supply:
    print(f"Everything is fine! Puppy is happy! Food: {food:.02f}, Hay: {hay:.02f}, Cover: {cover:.02f}.")
