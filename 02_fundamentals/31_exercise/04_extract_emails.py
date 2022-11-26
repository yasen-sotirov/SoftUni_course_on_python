import re

sentence = input()
pattern = r"\b([a-z\.\-\_]+@[a-z\.]+)\b"
found_emails = re.findall(pattern, sentence)
print('\n'.join(found_emails))
