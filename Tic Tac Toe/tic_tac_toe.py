def tic_tac_toe():
    field = list(input('Enter cells: '))
    print_field(field)
    game_state(field)


# prints the field from the given input
def print_field(field):
    print('---------')
    for i in range(0, len(field), 3):
        print('|', field[i], field[i + 1], field[i + 2], '|')
    print('---------')


# prints the current state of the game
def game_state(field):
    if impossible(field):
        print('Impossible')
    elif x_wins(field):
        print('X wins')
    elif o_wins(field):
        print('O wins')
    elif unfinished(field):
        print('Game not finished')
    else:
        print('Draw')


# returns True if the game state is impossible
def impossible(field):
    # the field has a lot more X's than O's or vice versa
    if abs(field.count('X') - field.count('O')) > 1:
        return True
    # the field has three X in a row as well as three O in a row
    elif x_wins(field) and o_wins(field):
        return True
    return False


# returns True if the field has three X in a row
def x_wins(field):
    return wins(field, 'X')


# returns True if the field has three O in a row
def o_wins(field):
    return wins(field, 'O')


# returns True if the given player wins
def wins(field, char):
    if horizontal_win(field, char) or vertical_win(field, char)\
            or diagonal_win(field, char):
        return True
    return False


# returns True if the given player wins horizontally
def horizontal_win(field, char):
    # checks all three rows
    for i in range(0, len(field), 3):
        if field[i] == char and field[i + 1] == char and field[i + 2] == char:
            return True
    return False


# returns True if the given player wins vertically
def vertical_win(field, char):
    # checks all three columns
    for i in range(len(field) // 3):
        if field[i] == char and field[i + 3] == char and field[i + 6] == char:
            return True
    return False


# returns True if the given player win diagonally
def diagonal_win(field, char):
    # checks both diagonals
    if field[4] == char:
        if field[0] == char and field[8] == char:
            return True
        elif field[2] == char and field[6] == char:
            return True
    return False


# returns True if the game state is unfinished
def unfinished(field):
    # checks whether no one has won, and whether the field has empty cells
    if not x_wins(field) and not o_wins(field) and field.count('_') > 0:
        return True
    return False


tic_tac_toe()
