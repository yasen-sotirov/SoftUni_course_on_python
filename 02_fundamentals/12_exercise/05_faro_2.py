start_deck = input().split()
number_of_shuffle = int(input())

for shuffles in range(number_of_shuffle):
    first_half = []
    second_half = []
    char_counter = 0

    for current_char in start_deck:
        if char_counter < len(start_deck) / 2:
            first_half.append(current_char)
            char_counter += 1
        else:
            second_half.append(current_char)

    new_deck = []
    index_counter = 0

    for current_shuffle in range(len(start_deck)):
        new_deck.append(first_half[index_counter])
        new_deck.append(second_half[index_counter])
        index_counter += 1

    start_deck = new_deck

