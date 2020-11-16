import board as board
import os

def create_game_file(board, b):
    if not os.path.exists('saved_games'):
        os.makedirs('saved_games')

    with open(file='saved_games/new_game.txt', mode='w', encoding='utf-8') as file:
        file.writelines([board.list_of_list_board_to_str(b)])

def save_turn(p_from, p_to):
    with open(file='saved_games/new_game.txt', mode='r+', encoding='utf-8') as file:
        initial_position = file.tell()
        print("Initial position: ", initial_position)

        from_value = file.seek(p_from - 1, initial_position)
        print("file seek p_from: ", from_value)
        file.write("#")

        to_value = file.seek(p_to - 1, initial_position)
        print("file seek p_to: ", to_value)
        file.write("@")

