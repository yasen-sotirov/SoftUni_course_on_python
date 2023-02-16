from collections import deque

players_turn = deque(input().split(', '))

maze = []
size = 6
resting_players = []

for row in range(size):
    maze.append(input().split())

while True:
    current_player = players_turn[0]
    row, col = [int(ch) for ch in input() if ch.isdigit()]
    position = maze[row][col]
    if current_player not in resting_players:
        if position == "E":
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif position == "T":
            print(f"{current_player} is out of the game! The winner is {players_turn[1]}.")
        elif position == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            resting_players.append(current_player)
            players_turn.rotate(1)
        else:
            players_turn.rotate(1)
    else:
        players_turn.rotate(1)
        resting_players.remove(resting_players[0])


