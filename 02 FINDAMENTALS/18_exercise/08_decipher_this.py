"""" You are given a secret message you should decipher.
To do that, you need to know that in each word:
•	the second and the last letter are switched (e.g., Holle means Hello)
•	the first letter is replaced by its character code (e.g., 72 means H)
"""


cipher_list = input().split()
output_list = []

for word in cipher_list:
    letters = []
    nums = ""
    current_word = []
    for char in word:
        if char.isalpha():
            letters.append(char)
        else:
            nums += char

    first_parth = chr(int(nums))
    changing_letters = letters[0], letters[-1] = letters[-1], letters[0]
    second_part = "".join(letters)

    current_word.append(first_parth)
    current_word.append(second_part)
    print("".join(current_word), end=' ')
