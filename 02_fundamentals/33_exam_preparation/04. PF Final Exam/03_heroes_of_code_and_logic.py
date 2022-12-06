""" Problem 3 - Heroes of Code and Logic VII
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at
https://judge.softuni.org/Contests/Practice/Index/2303#0.

You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
You want to play it all day long! So cancel all other arrangements and create your party!

On the first line of the standard input, you will receive an integer n – the number of heroes
that you can choose for your party. On the next n lines, the heroes themselves will follow
with their hit points and mana points separated by a single space in the following format:
"{hero name} {HP} {MP}"
-	HP stands for hit points and MP for mana points
-	a hero can have a maximum of 100 HP and 200 MP

After you have successfully picked your heroes, you can start playing the game.
You will be receiving different commands, each on a new line, separated by " – ",
 until the "End" command is given.
There are several actions that the heroes can perform:

"CastSpell – {hero name} – {MP needed} – {spell name}"
•	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
    o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
•	If the hero is unable to cast the spell print:
    o	"{hero name} does not have enough MP to cast {spell name}!"

"TakeDamage – {hero name} – {damage} – {attacker}"
•	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0)
    print:
    o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
•	If the hero has died, remove him from your party and print:
    o	"{hero name} has been killed by {attacker}!"

"Recharge – {hero name} – {amount}"
•	The hero increases his MP. If it brings the MP of the hero above the maximum value (200),
    MP is increased to 200. (the MP can't go over the maximum value).
•	 Print the following message:
    o	"{hero name} recharged for {amount recovered} MP!"

"Heal – {hero name} – {amount}"
•	The hero increases his HP. If a command is given that would bring the HP of the hero above
    the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
•	 Print the following message:
    o	"{hero name} healed for {amount recovered} HP!"

Input
•	On the first line of the standard input, you will receive an integer n
•	On the following n lines, the heroes themselves will follow with their hit points and
    mana points separated by a space in the following format
•	You will be receiving different commands, each on a new line, separated by " – ",
    until the "End" command is given

Output
•	Print all members of your party who are still alive, in the following format
    (their HP/MP need to be indented 2 spaces):
    "{hero name}
  HP: {current HP}
  MP: {current MP}"

Constraints
•	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or
    exceed the respective limits.
•	The HP/MP amounts in the commands will never be negative.
•	The hero names in the commands will always be valid members of your party. No need to check
    that explicitly.

Examples

Input
2
Solmyr 85 120
Kyrre 99 50
Heal - Solmyr - 10
Recharge - Solmyr - 50
TakeDamage - Kyrre - 66 - Orc
CastSpell - Kyrre - 15 - ViewEarth
End

Output
Solmyr healed for 10 HP!
Solmyr recharged for 50 MP!
Kyrre was hit for 66 HP by Orc and now has 33 HP left!
Kyrre has successfully cast ViewEarth and now has 35 MP!
Solmyr
  HP: 95
  MP: 170
Kyrre
  HP: 33
  MP: 35

Input
4
Adela 90 150
SirMullich 70 40
Ivor 1 111
Tyris 94 61
Heal - SirMullich - 50
Recharge - Adela - 100
CastSpell - Tyris - 1000 - Fireball
TakeDamage - Tyris - 99 - Fireball
TakeDamage - Ivor - 3 - Mosquito
End

Output
SirMullich healed for 30 HP!
Adela recharged for 50 MP!
Tyris does not have enough MP to cast Fireball!
Tyris has been killed by Fireball!
Ivor has been killed by Mosquito!
Adela
  HP: 90
  MP: 200
SirMullich
  HP: 100
  MP: 40

"""

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
