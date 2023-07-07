from collections import deque

vowels = deque(el for el in input().split())
consonants = [el for el in input().split()]

flowers_list = {
    "rose": [el for el in 'rose'],
    "tulip": [el for el in 'tulip'],
    "lotus": [el for el in 'lotus'],
    "daffodil": [el for el in 'daffodil']
}

founded_flower = None

while vowels and consonants and not founded_flower:
    current_vowels = vowels.popleft()
    current_consonants = consonants.pop()

    for current_letter in (current_vowels, current_consonants):
        for key_flower_name, value_flower_letters in flowers_list.items():
            while value_flower_letters.count(current_letter):
                value_flower_letters.remove(current_letter)
                if not value_flower_letters:      # if there are no more letters in the value
                    founded_flower = key_flower_name

if founded_flower:
    print(f"Word found: {founded_flower}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
