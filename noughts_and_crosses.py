# noughts_and_crosses.py
# Copyright (c) 2024-2025 dhpoware. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""Noughts and Crosses implementation for a single player versus a computer ai."""

import copy
import random

EMPTY_GAME_BOARD_SQUARE = " "
PLAYER_1_GAME_PIECE = "X"
PLAYER_2_GAME_PIECE = "O"

game_board = [EMPTY_GAME_BOARD_SQUARE for i in range(9)]

def print_game_board():
    top_row = f"| {game_board[0]} | {game_board[1]} | {game_board[2]} |"
    middle_row = f"| {game_board[3]} | {game_board[4]} | {game_board[5]} |"
    bottom_row = f"| {game_board[6]} | {game_board[7]} | {game_board[8]} |"
    print()
    print(top_row)
    print(middle_row)
    print(bottom_row)
    print()

def is_draw():
    return EMPTY_GAME_BOARD_SQUARE not in game_board

def player_move(player_piece):
    while True:
        move = int(input(f"Player {player_piece}, what is your move: 1-9 (1=top left, 9 = bottom right)? ").strip()) - 1
        if game_board[move] == EMPTY_GAME_BOARD_SQUARE:
            game_board[move] = player_piece
            break
        else:
            print("That square is already occupied. Try again!")

def computer_move(computer_piece, player_piece=PLAYER_1_GAME_PIECE):
    """The algorithm is based on this: https://inventwithpython.com/chapter10.html"""
    
    moved = False
    
    # Check if we can win in the next move.
    for move in range(len(game_board)):
        game_board_copy = copy.deepcopy(game_board)
        if game_board_copy[move] == EMPTY_GAME_BOARD_SQUARE:
            game_board_copy[move] = computer_piece
            if has_won(computer_piece, game_board_copy):
                game_board[move] = computer_piece
                moved = True
                print(f"Computer moved to {move + 1}. Computer is moving to win.")
                break
                
    # Check if player can win in their next move. If so, block them.
    if not moved:
        for move in range(len(game_board)):
            game_board_copy = copy.deepcopy(game_board)
            if game_board_copy[move] == EMPTY_GAME_BOARD_SQUARE:
                game_board_copy[move] = player_piece
                if has_won(player_piece, game_board_copy):
                    game_board[move] = computer_piece
                    moved = True
                    print(f"Computer moved to {move + 1}. Computer is blocking player's next move.")
                    break
        
        # Try to take one of the corner squares.
        if not moved:
            for move in [0, 2, 6, 8]:
                if game_board[move] == EMPTY_GAME_BOARD_SQUARE:
                    game_board[move] = computer_piece
                    moved = True
                    print(f"Computer moved to {move + 1}. Computer is taking a corner.")
                    break
                
            # Try to take the centre square.    
            if not moved:
                if game_board[4] == EMPTY_GAME_BOARD_SQUARE:
                    game_board[4] = computer_piece
                    moved = True
                    print("Computer moved to 5. Computer is taking the centre.")
                    
                # Take the middle square of one of the sides.
                if not moved:
                    for move in [1, 3, 5, 7]:
                        if game_board[move] == EMPTY_GAME_BOARD_SQUARE:
                            game_board[move] = computer_piece
                            print(f"Computer moved to {move + 1}. Computer is taking a side.")
                            break

def has_won(player_piece, board=game_board):
    return (board[0] == board[1] == board[2] == player_piece) or \
           (board[3] == board[4] == board[5] == player_piece) or \
           (board[6] == board[7] == board[8] == player_piece) or \
           (board[0] == board[3] == board[6] == player_piece) or \
           (board[1] == board[4] == board[7] == player_piece) or \
           (board[2] == board[5] == board[8] == player_piece) or \
           (board[0] == board[4] == board[8] == player_piece) or \
           (board[2] == board[4] == board[6] == player_piece)

def player_goes_first():
    player_game_piece = PLAYER_1_GAME_PIECE
    computer_game_piece = PLAYER_2_GAME_PIECE
    
    while True:
        player_move(player_game_piece)
        print_game_board()
        if has_won(player_game_piece):
            print(f"Player {player_game_piece} won!")
            break;
        if is_draw():
            print("Draw!")
            break

        computer_move(computer_game_piece, player_piece=player_game_piece)
        print_game_board()
        if has_won(computer_game_piece):
            print(f"Computer {computer_game_piece} won!")
            break
        if is_draw():
            print("Draw!")
            break

def computer_goes_first():
    computer_game_piece = PLAYER_1_GAME_PIECE
    player_game_piece = PLAYER_2_GAME_PIECE

    while True:
        computer_move(computer_game_piece, player_piece=player_game_piece)
        print_game_board()
        if has_won(computer_game_piece):
            print(f"Computer {computer_game_piece} won!")
            break
        if is_draw():
            print("Draw!")
            break
            
        player_move(player_game_piece)
        print_game_board()
        if has_won(player_game_piece):
            print(f"Player {player_game_piece} won!")
            break;
        if is_draw():
            print("Draw!")
            break

def main():
    print("Let's play Noughts and Crosses!")
    print_game_board()
    computer_moves_first = random.choice([True, False])
    if computer_moves_first:
        computer_goes_first()
    else:
        player_goes_first()
    
if __name__ == "__main__":
    main()