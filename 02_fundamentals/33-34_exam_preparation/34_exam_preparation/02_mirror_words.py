import re
text = input()
list_of_couples = []
mirror_words = 0

pattern = r"(@|#)[A-Za-z]{3,}(\1{2,})[A-Za-z]{3,}(\1)"
couples = re.finditer(pattern, text)
for word_couple in couples:
    pear = word_couple.group()
    list_of_couples.append(pear)

if not list_of_couples:
    print("No word pairs found!")
else:
    print(f"{len(list_of_couples)} word pairs found!")

for couples in list_of_couples:
    first_word = couples[:(len(couples) // 2)]
    second_word = couples[(len(couples) // 2):]
    reversed_second_word = second_word[::-1]

    first_word = first_word.strip("@#")
    reversed_second_word = reversed_second_word.strip("@#")
    second_word = second_word.strip("@#")

    if first_word == reversed_second_word:
        print(f"{first_word} <=> {second_word}")




