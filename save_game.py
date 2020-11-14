import board as board
import os

def create_game_file(board):
    if not os.path.exists('saved_games'):
        os.makedirs('saved_games')

    with open(file='saved_games/new_game.txt', mode='w', encoding='utf-8') as file:
        file.writelines([board.board_to_str()])

# def save_turn(board):
