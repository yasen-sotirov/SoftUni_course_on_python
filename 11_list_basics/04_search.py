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
 