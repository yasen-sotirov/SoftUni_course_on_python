import re

line = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
found_names = re.findall(pattern, line)
print(','.join(found_names))



