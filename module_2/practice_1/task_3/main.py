'''Напишите программу, которая реализует игру «Крестики-нолики». '''
from cell import *
from board import *
from player import Player

screen = Screen()
screen.setup(window_size + 20, window_size + 20)

def ask_player(player_name, gameboard, size):
    '''Asks the player how he wants to move, if the cell is free, 
    he writes it down and draws it, otherwise he informs about an error 
    and asks for a move again
    :return: None
    '''
    while True:
        try:
            turn = player_name.ask_turn()
            error_status = False
            for num in turn:
                if num > size:
                    print('Value is more, than boardsize. Try again!')
                    error_status = 1
                    break
                else:
                    continue

            if error_status:
                continue
            
            break
        except:
            print('Incorrect input! Try again!')
            continue

    for cell in gameboard.cells:
        if cell.order == player_name.turn:
            if cell.occupied == True:
                print('This cell is occupied! Choose another')
                player_name.ask_turn()
            else:
                cell.occupied = True
                gameboard.draw_turn(
                    player_name.turn[0], player_name.turn[1],\
                        player_name.side)

if __name__ == '__main__':
    while True:
        #Ask gameboard size
        try:
            gameboard_size = int(input('Enter the N of NxN board(3-9): '))
            if gameboard_size in range(3, 10):
                break
            else:
                print('Incorrect input! Try again!')
                continue
        except:
            print('Incorrect input! Try again!')
            continue
    
    #Create a board instance, draws a numbered board on the screen
    current_gameboard = Board(gameboard_size)
    
    #Create an instance of the 1st player, ask and write down the name
    player_1 = Player()
    if not player_1.name:
        player_1.ask_name()
    if not player_1.side:
        while True:
            try:
                player_1.ask_side()
                if player_1.side in [0, 1]:
                    break
                else:
                    print('Incorrect input! Try again!')
                    continue
            except:
                print('Incorrect input! Try again!')
                continue
    
    #Create an instance of the 2nd player, ask and write down the name        
    player_2 = Player()
    if not player_2.name:
        player_2.ask_name()
    
    if player_1.side == 0:
        player_2.side = 1
        player_1, player_2 = player_2, player_1
    else:
        player_2.side = 0
                
    while True:
        ask_player(player_1, current_gameboard, gameboard_size)
        ask_player(player_2, current_gameboard, gameboard_size)