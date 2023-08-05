""" 5.	Word Count
Write a program that reads a list of words from the file words.txt
and finds how many times each of the words is contained in
another file text.txt. Matching should be case-insensitive.
The results should be written to other text files.
Sort the words by frequency in descending order.
"""

import re


def read_searched_words(file_path):
    searched_word = []
    with open(file_path) as file:
        searched_word = file.read().split()
    return searched_word


def calculate_searched_words(searched_word, file_path):
    words_count = {}
    with open(file_path) as file:
        text = file.read()
        for word in searched_word:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count
    return words_count


def store_result(result, output_file_path):
    with open(output_file_path, "w") as file:
        # връща лист от тюпъли
        sorted_result = sorted(result.items(), key=lambda kvpt: -kvpt[1])

        # чете от листа
        for key, value in sorted_result:
            file.writelines(f"{key} - {value}\n")


words_for_search = read_searched_words("words.txt")
count_result = calculate_searched_words(words_for_search, "input.txt")
store_result(count_result, "output.txt")
