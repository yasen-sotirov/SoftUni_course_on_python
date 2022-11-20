"""" Write a program that returns an encrypted version of the same text.
Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII t.
 For example, A would be replaced with D, B would become E, and so on. Print the encrypted text."""


input_text = input()
for char in input_text:
    new_char = ord(char) + 3
    print(chr(new_char), end="")
