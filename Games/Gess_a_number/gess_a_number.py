import random
player_guesses_counter = 0
computer_number = random.randint(1, 100)

while True:
    player_input = input('Guess the number (1-100): ')
    if not player_input.isdigit():
        print('Invalid input. Try again...')
        continue
    player_number = int(player_input)
    player_guesses_counter += 1

    if player_number == computer_number:
        print('You guess it!')
        print(f'You guessed {player_guesses_counter} times')
        break
    elif player_number < computer_number:
        print('Too Low!')
        print(f'You guessed {player_guesses_counter} times')
        print()
    else:
        print('Too High!')
        print(f'You guessed {player_guesses_counter} times')
        print()
