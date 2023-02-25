import re

spell = input()
while True:
    command = input().split()
    if "Abracadabra" in command:
        break

    elif "Abjuration" in command:
        spell = spell.upper()
        print(spell)

    elif "Necromancy" in command:
        spell = spell.lower()
        print(spell)

    elif "Illusion" in command:
        index = int(command[1])
        letter = command[2]
        if index > len(spell) - 1:
            print(f"The spell was too weak.")
        else:
            temp = list(spell)
            temp[index] = letter
            spell = ''.join(temp)
            print("Done!")

    elif "Divination" in command:
        first_substring = command[1]
        second_substring = command[2]
        result = re.search(first_substring, spell)
        if result:
            result = result.group()
            spell = spell.replace(first_substring, second_substring)
            print(spell)
        else:
            continue

    elif "Alteration" in command:
        pattern = fr'{command[1]}'
        search = re.search(pattern, spell)
        if search:
            search = search.group()
            spell = re.sub(pattern, "", spell)
            print(spell)
        else:
            continue
    else:
        print(f"The spell did not work!")
