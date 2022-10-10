""" On the first line, you will receive a number n.
On the second line, you will receive a word.
On the following n lines, you will be given some strings.
You should add them to a list and print them.
After that, you should filter out only the strings
 that include the given word and print that list too."""


number_of_lines = int(input())
searched_word = input()
list_for_all_str = []
list_with_searched_word = []

for current_line in range(number_of_lines):
    current_string = input()
    list_for_all_str.append(current_string)

    if searched_word in current_string:
        list_with_searched_word.append(current_string)

print(list_for_all_str)
print(list_with_searched_word)
 