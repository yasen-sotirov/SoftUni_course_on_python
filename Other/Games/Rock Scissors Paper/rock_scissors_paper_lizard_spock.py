import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
lizard = 'Lizard'
spock = 'Spock'

player_move = input("Choose [r]ock, [s]cissors, [p]aper, [l]izard or [sp]ock: ")
if player_move == 'r':
    player_move = rock
elif player_move == 's':
    player_move = scissors
elif player_move == "p":
    player_move = paper
elif player_move == "l":
    player_move = lizard
elif player_move == "sp":
    player_move = spock
else:
    raise SystemExit('Invalid Input. Tray again...')

computer_random_number = random.randint(1, 5)
computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = scissors
elif computer_random_number == 3:
    computer_move = paper
elif computer_random_number == 4:
    computer_move = lizard
else:
    computer_move = spock

print(f"The computer chose {computer_move}.")

if (player_move == rock and (computer_move == scissors or computer_move == lizard)) or \
        (player_move == paper and (computer_move == rock or computer_move == spock)) or \
        (player_move == scissors and (computer_move == paper or computer_move == lizard)) or \
        (player_move == lizard and (computer_move == paper or computer_move == spock)) or \
        (player_move == spock and (computer_move == scissors or computer_move == rock)):

    print('You win!')
elif player_move == computer_move:
    print('Draw!')
else:
    print('You lose!')
