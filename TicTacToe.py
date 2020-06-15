#--------Global variables---------

#Stores the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#Variable to hold the winner
winner = None

#Determines if the game is still going or finished
game_still_going = True

#Holds the current player either X or O
current_player = "X"

#Displays the board on screen
def display_board():
    print("{0[0]} | {0[1]} | {0[2]}         | 1 | 2 | 3 |".format(board))
    print("{0[3]} | {0[4]} | {0[5]}         | 4 | 5 | 6 |".format(board))
    print("{0[6]} | {0[7]} | {0[8]}         | 7 | 8 | 9 |".format(board))
    print("\n")

#Executes the game of Tic Tac Toe
def play_game():
    display_board()
    while game_still_going:
        handle_turns(current_player)
        check_if_game_over()
        flip_player(current_player)
    if winner == "X" or winner=="O":
        print("{0} won".format(winner))
    else:
        print("Tie")


#Stores players' moves
def handle_turns(player):
    print("{0}'s turn".format(player))
    position = input("Choose a position from 1-9: ")
    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:
        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: " )
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("The slot is already filled")
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner
    row_winner = row_check()
    column_winner = column_check()
    diagonal_winner  = diagonal_check()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        return None


def row_check():
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
        # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def column_check():
    global  game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def diagonal_check():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    else:
        return None


# Flip the current player from X to O, or O to X
def flip_player(player):
    global current_player
    if player == "X":
        current_player = "O"
    else:
        current_player = "X"


#Start the game
play_game()