#Welcome to my Tic-Tac-Toe game. It isn't pretty but so far I think it's working.
import os
import time
####################################################################################
#building the board
def display_board(game_board):

    print(f' {game_board[6]} | {game_board[7]} | {game_board[8]} ')
    print('--- --- --- ')
    print(f' {game_board[3]} | {game_board[4]} | {game_board[5]} ')
    print('--- --- --- ')
    print(f' {game_board[0]} | {game_board[1]} | {game_board[2]} ')

####################################################################################
#The start of the game
def player_input():
    choice = ''
    player1 = ''
    player2 = ''

    while choice not in ['X', 'O']:
        choice = input("Welcome to Tic-Tac-Toe - Designed by Don Neely.\nPlayer1, please pick 'X' or 'O'.")

        if choice not in ['X', 'O']:
            print("Sorry, invalid choice! ")

        else:
            player1 = choice

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'You chose {player1}. Player2 you are {player2}.')
    return choice

####################################################################################
#Bastardized confirmation of Player 2 being 'O'
def player2_confirm():
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player2

####################################################################################
#Allowing player 1 interation in board cells
def player1_choice():
    choice = ['wrong']

    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        choice = input("Player1: Please select a position. ")

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, invalid choice! ")

    return choice

####################################################################################
#Player 1 cell replacement
def player1_replacement(game_board, position):
    user_placement = player1

    game_board = [w.replace(position, user_placement) for w in game_board]

    return game_board

####################################################################################
#Allowing player 2 interation in board cells
def player2_choice():
    choice = ['wrong']

    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        choice = input("Player2: Please select a position. ")

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, invalid choice! ")

    return choice

####################################################################################
#Player 2 cell replacement
def player2_replacement(game_board, position):
    user_placement = player2

    game_board = [w.replace(position, user_placement) for w in game_board]

    return game_board

####################################################################################
#Determine the winner
def check_winner():
    global win
    win = ''
    player1 = 'X'
    player2 = 'O'
    while win == '':
        #used to check the winner in row
        if (game_board[0] == game_board[1] and game_board[1] == game_board[2] and game_board[0] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[0] == game_board[1] and game_board[1] == game_board[2] and game_board[0] == player2):
            win = 'Player2 is the winner!'
        elif (game_board[3] == game_board[4] and game_board[4] == game_board[5] and game_board[3] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[3] == game_board[4] and game_board[4] == game_board[5] and game_board[3] == player2):
            win = 'Player2 is the winner!'
        elif (game_board[6] == game_board[7] and game_board[7] == game_board[8] and game_board[6] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[6] == game_board[7] and game_board[7] == game_board[8] and game_board[6] == player2):
            win = 'Player2 is the winner!'
        #used to check the winner in column
        elif (game_board[0] == game_board[3] and game_board[3] == game_board[6] and game_board[0] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[0] == game_board[3] and game_board[3] == game_board[6] and game_board[0] == player2):
            win = 'Player2 is the winner!'
        elif (game_board[1] == game_board[4] and game_board[4] == game_board[7] and game_board[1] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[1] == game_board[4] and game_board[4] == game_board[7] and game_board[1] == player2):
            win = 'Player2 is the winner!'
        elif (game_board[2] == game_board[5] and game_board[5] == game_board[8] and game_board[2] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[2] == game_board[5] and game_board[5] == game_board[8] and game_board[2] == player2):
            win = 'Player2 is the winner!'
        #used to check the winner in diagonal
        elif (game_board[0] == game_board[4] and game_board[4] == game_board[8] and game_board[0] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[0] == game_board[4] and game_board[4] == game_board[8] and game_board[0] == player2):
            win = 'Player2 is the winner!'
        elif (game_board[2] == game_board[4] and game_board[4] == game_board[6] and game_board[2] == player1):
            win = 'Player1 is the winner!'
        elif (game_board[2] == game_board[4] and game_board[4] == game_board[6] and game_board[2] == player2):
            win = 'Player2 is the winner!'
        else:
            win = ''
        return win

####################################################################################
#Letting players choose to keep playing or not.
def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, please choose Y or N ")

    if choice == 'Y':
        return True

    else:
        return False

####################################################################################
#Code to run all function for the game
game_on = True
game_board = ['1','2','3','4','5','6','7','8','9']

while game_on:
    display_board(game_board)
    player1 = player_input()
    player2 = player2_confirm()
    check_winner()
    while win == '':
        position = player1_choice()
        game_board = player1_replacement(game_board,position)
        os.system('cls')
        display_board(game_board)
        win = check_winner()
        if win == 'Player1 is the winner!':
            break
        else:
            pass
        position = player2_choice()
        game_board = player2_replacement(game_board,position)
        os.system('cls')
        display_board(game_board)
        win = check_winner()
        if win == 'Player2 is the winner!':
            break
        else:
            continue

    print(win)
    game_on = gameon_choice()

print('Thanks for playing!')
time.sleep(1)
os.system('cls')