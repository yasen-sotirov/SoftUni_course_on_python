"""" On the first line, you will receive words separated by a single space.
On the second line, you will receive a palindrome.
First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format:
"Found palindrome {number} times"."""


word_list = input().split()
searched_word = input()
palindrom_list = []

for word in word_list:
    if word == word[::-1]:
        palindrom_list.append(word)

counter = palindrom_list.count(searched_word)

print(palindrom_list)
print(f"Found palindrome {counter} times")
