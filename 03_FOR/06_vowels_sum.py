# text[i] - взема буквата с №i от думата, а „i“ се променя
# word = "Hello, World!"
# print(word[5])

text = input()
sum_of_letters = 0

for letter in range(0, len(text)):
    if text[letter] == 'a':
        sum_of_letters += 1
    if text[letter] == 'e':
        sum_of_letters += 2
    if text[letter] == 'i':
        sum_of_letters += 3
    if text[letter] == 'o':
        sum_of_letters += 4
    if text[letter] == 'u':
        sum_of_letters += 5

print(sum_of_letters)
 