# https://pastebin.com/bbDQCr6G

starting_deck = input().split()
number_of_shuffle = int(input())

middle_of_deck = len(starting_deck) / 2

for _ in range(number_of_shuffle):
    new_deck = []
    for current_card in starting_deck:
        new_deck.append(current_card)
        new_deck.append(current_card * middle_of_deck)
