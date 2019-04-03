import random

# create board


def display_board(board):
    print(" \n" * 100)

    print('  TIC TAC TOE  ')
    print('----------------')
    print('|7   |8   |9   |')
    print('|  ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9] + ' |')
    print('|    |    |    |')
    print('----------------')
    print('|4   |5   |6   |')
    print('|  ' + board[4] + ' |  ' + board[5] + ' |  ' + board[6] + ' |')
    print('|    |    |    |')
    print('----------------')
    print('|1   |2   |3   |')
    print('|  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3] + ' |')
    print('|    |    |    |')
    print('----------------')

# player 1 chooses Xs or Os


def player_input():
    marker = 'n'

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# place X or O based on user input


def place_marker(board, marker, position):
    board[position] = marker

# check for winner


def win_check(board, mark):

    return ((board[7] == board[8] == board[9] == mark) or  # across the top
            # across the middle
            (board[4] == board[5] == board[6] == mark) or
            # across the bottom
            (board[1] == board[2] == board[3] == mark) or
            # down the left side
            (board[7] == board[4] == board[1] == mark) or
            # down the middle
            (board[8] == board[5] == board[2] == mark) or
            # down the right side
            (board[9] == board[6] == board[3] == mark) or
            # diagonals
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

# coin flip to see who goes first


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# check if a space if available to play in


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# ask player for their next position choice


def player_choice(turn, board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input(f'{turn} choose your next position: (1-9) '))
        except:
            print("Not a valid position, choose a position (1-9)")
    return position

# ask if player wants to play again


def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# Run the Game!
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(turn, theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has won this game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(turn, theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won this game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
