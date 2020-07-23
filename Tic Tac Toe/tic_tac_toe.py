def tic_tac_toe():
    field = [' '] * 9
    print_field(field)

    current_player = 'X'
    while not game_over(field):
        player_move(field, current_player)
        print_field(field)
        current_player = next_player(current_player)

    game_state(field)


# prints the current game field
def print_field(field):
    print('-' * 9)
    for i in range(0, len(field), 3):
        print('|', field[i], field[i + 1], field[i + 2], '|')
    print('-' * 9)


# returns the player which has to make a move next
def next_player(current_player):
    return 'X' if current_player == 'O' else 'O'


# returns True if the game is finished
def game_over(field):
    if wins(field, 'X'):
        return True
    elif wins(field, 'O'):
        return True
    elif draw(field):
        return True
    return False


# prints the current state of the game
def game_state(field):
    if wins(field, 'X'):
        print('X wins')
    elif wins(field, 'O'):
        print('O wins')
    else:
        print('Draw')


# allows the current player to make a move
def player_move(field, player):
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
                field[index] = player
                break


# returns True if the given player wins
def wins(field, player):
    if horizontal_win(field, player) or vertical_win(field, player)\
            or diagonal_win(field, player):
        return True
    return False


# returns True if the given player wins horizontally
def horizontal_win(field, player):
    # checks all three rows
    for i in range(0, len(field), 3):
        if field[i] == player and field[i + 1] == player \
                and field[i + 2] == player:
            return True
    return False


# returns True if the given player wins vertically
def vertical_win(field, player):
    # checks all three columns
    for i in range(len(field) // 3):
        if field[i] == player and field[i + 3] == player \
                and field[i + 6] == player:
            return True
    return False


# returns True if the given player win diagonally
def diagonal_win(field, player):
    # checks both diagonals
    if field[4] == player:
        if field[0] == player and field[8] == player:
            return True
        elif field[2] == player and field[6] == player:
            return True
    return False


# returns True if the game is finished and no one has won
def draw(field):
    # checks whether no one has won,
    # and whether the field does not have empty cells
    if not wins(field, 'X') and not wins(field, 'O') \
            and field.count(' ') == 0:
        return True
    return False


tic_tac_toe()
