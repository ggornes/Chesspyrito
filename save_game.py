import board as board
import os
import utils

def create_game_file(board, b):
    if not os.path.exists('saved_games'):
        os.makedirs('saved_games')

    with open(file='saved_games/new_game.txt', mode='w', encoding='utf-8') as file:
        file.writelines([utils.list_of_list_board_to_str(b)])

def save_turn(moving_piece, position_from, position_to):
    with open(file='saved_games/new_game.txt', mode='r+', encoding='utf-8') as file:
        initial_position = file.tell()
        file.seek(position_from - 1, initial_position)
        #print("file seek p_from: ", from_value)
        # when moving a piece, it always leaves a blank space behind
        file.write(".")
        file.seek(position_to - 1, initial_position)
        # print("file seek p_to: ", to_value)
        file.write(moving_piece)

