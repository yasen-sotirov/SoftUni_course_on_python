import re

final_list = []
count_of_string = int(input())
pattern = r"![A-Z][a-z]{2,}!:\[[A-Za-z]{8,}\]"

for _ in range(count_of_string):
    line = input()
    match = re.search(pattern, line)
    if match:
        match = match.group()
        match = match.split(":")
        command = match[0]
        command = command[1:-1]
        text_to_translate = match[1]

        for element in text_to_translate:
            if element.isalpha():
                translated_element = str(ord(element))
                final_list.append(translated_element)
        list_for_print = " ".join(final_list)
        print(f"{command}: {list_for_print}")

    else:
        print(f"The message is invalid")
