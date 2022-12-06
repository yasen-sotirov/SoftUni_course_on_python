number_of_heroes = int(input())
dict_of_heroes = {}

for current_hero in range(number_of_heroes):
    data = input().split()
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])
    dict_of_heroes[hero_name] = {}
    dict_of_heroes[hero_name]["hit_points"] = hit_points
    dict_of_heroes[hero_name]["mana_points"] = mana_points

while True:
    command = input().split(" - ")
    if "End" in command:
        break

    elif "CastSpell" in command:
        hero_name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        if dict_of_heroes[hero_name]["mana_points"] >= mana_needed:
            dict_of_heroes[hero_name]["mana_points"] -= mana_needed
            mana_left = dict_of_heroes[hero_name]["mana_points"]
            print(f"{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in command:
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        dict_of_heroes[hero_name]["hit_points"] -= damage
        if dict_of_heroes[hero_name]["hit_points"] > 0:
            current_hit_points = dict_of_heroes[hero_name]["hit_points"]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hit_points} HP left!")
        else:
            del dict_of_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif "Recharge" in command:
        hero_name = command[1]
        amount = int(command[2])
        if dict_of_heroes[hero_name]:
            pass

    elif "Heal" in command:
        pass

print(dict_of_heroes)
