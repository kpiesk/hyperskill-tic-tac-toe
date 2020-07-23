def tic_tac_toe():
    field = list(input('Enter cells: '))

    replace_empty(field)
    print_field(field)

    player_move(field)
    print_field(field)
    # game_state(field)


# prints the field from the given input
def print_field(field):
    print('-' * 9)
    for i in range(0, len(field), 3):
        print('|', field[i], field[i + 1], field[i + 2], '|')
    print('-' * 9)


# replaces underscores with spaces in empty cells
def replace_empty(field):
    for i in range(len(field)):
        if field[i] == '_':
            field[i] = ' '


def player_move(field):
    while True:
        try:
            x, y = input('Enter the coordinates: ').split()
            x = int(x)
            y = int(y)
        except ValueError:
            print('You should enter numbers!')
            continue

        if x < 1 or x > 3 or y < 1 or y > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            # converts coordinates to index in the field list
            index = (x - 1) + (9 - (3 * y))

            if field[index] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                field[index] = 'X'
                break


# prints the current state of the game
def game_state(field):
    if impossible(field):
        print('Impossible')
    elif wins(field, 'X'):
        print('X wins')
    elif wins(field, 'O'):
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
    elif wins(field, 'X') and wins(field, 'O'):
        return True
    return False


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
    if not wins(field, 'X') and not wins(field, 'O') and field.count('_') > 0:
        return True
    return False


tic_tac_toe()
