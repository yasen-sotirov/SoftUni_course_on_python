""" 4.	Count Symbols
Write a program that reads a text from the console and counts the occurrences
of each character in it. Print the results in alphabetical (lexicographical) order.
"""

line = input()
counter = {}

for ch in line:
    if ch in counter:
        counter[ch] += 1
    else:
        counter[ch] = 1

for ch, times in sorted(counter.items()):
    print(f"{ch}: {times} time/s")

