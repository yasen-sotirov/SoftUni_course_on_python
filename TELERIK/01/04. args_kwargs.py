# variable length args
# it's usually named *args, but the name does not matter, only the asterisk symbol
def print_standings(*standings):
    position = 1
    for name in standings:
        print(f'{position}. {name}')
        position += 1


# pass as many as you need
print_standings('Jill', 'Alice', 'Bob', 'Steven')


# the usual name for Variable-Length keyword args is **kwargs, but the name can be any
# only the double asterisk ** is important
def print_standing_with_score(**standings):
    position = 1
    for name, score in standings.items():
        print(f'{position}. {name.capitalize()} ({score} pts)')
        position += 1

# the "key" is typed without quotes (e.g. jill not 'jill')
print_standing_with_score(jill=350, alice=220, bob=180, steven=180)
