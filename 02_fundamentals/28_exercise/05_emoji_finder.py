"""" Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.
"""


single_string = input()

for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f":{single_string[index + 1]}")
