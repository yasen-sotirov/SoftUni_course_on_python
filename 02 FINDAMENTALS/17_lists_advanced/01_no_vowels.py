text = input()
vowels = ["a", 'o', 'u', 'e', 'i']
print(''.join([element for element in text if element.lower() not in vowels]))

# ИЛИ

result = []
for element in text:
    if element.lower() not in vowels:
        result.append(element)

print(''.join(result))