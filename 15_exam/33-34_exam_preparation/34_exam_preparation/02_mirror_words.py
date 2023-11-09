""" On the first line of the input, you will be given a text string.
To win the competition, you have to find all hidden word pairs, read them,
and mark the ones that are mirror images of each other.
First of all, you have to extract the hidden word pairs. Hidden word pairs are:
•	Surrounded by "@" or "#" (only one of the two) in the following pattern
    #wordOne##wordTwo# or @wordOne@@wordTwo@
•	At least 3 characters long each (without the surrounding symbols)
•	Made up of letters only

If the second word, spelled backward, is the same as the first word and vice versa (casing matters!),
they are a match, and you have to store them somewhere. Examples of mirror words:
    #Part##traP# @leveL@@Level@ #sAw##wAs#
•	If you don`t find any valid pairs, print: "No word pairs found!"
•	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
•	If there are no mirror words, print: "No mirror words!"
•	If there are mirror words print:

    "The mirror words are:
    {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"

    Input / Constraints
•	You will recive a string.

    Output
•	Print the proper output messages in the proper cases as described in the problem description.
•	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
•	Each pair of mirror word must be printed with " <=> " between the words.

    Examples
    Input
@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r

    Output
5 word pairs found!
The mirror words are:
Part <=> traP, leveL <=> Level, sAw <=> wAs

    Input
    #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@

    Output
2 word pairs found!
No mirror words!

 """

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


    # NOT FINISHED