import re

pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
