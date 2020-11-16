from board import Board
from save_game import create_game_file, save_turn
import utils
import os


def start_game():
    turn_counter = 0
    print("Starting new chess game")
    board = Board()
    initial_board = board.board_to_list_of_list()
    game_input = ''
    create_game_file(board, initial_board)

    # game loop
    while game_input != "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        board.print_board()
        # board.board_to_str()
        # print("Board representation as a list: ")
        # print(board.board_to_list())


        # print("Board representation as a list of list: ")
        b = board.board_to_list_of_list()
        #print(b)


        # print("Board representation in one single line: ")
        # print(board.board_to_str())
        # print("Board representation in one single line: ")
        # print(utils.list_of_list_board_to_str(b))

        if turn_counter % 2 == 0:
            print("White turn")
        else:
            print("Black turn")
        move = input("Move:")

        square_from, square_to = board.parse_move_to_square(move)
        file_from, rank_from, x_from, y_from = board.parse_square_to_list_index_position(str(square_from))
        file_to, rank_to, x_to, y_to = board.parse_square_to_list_index_position(str(square_to))
        print("Moving " + square_from + " (" + str(x_from) + ", " + str(y_from) + ")" + " to " + square_to + " (" + str(
            x_to) + ", " + str(y_to) + ")")

        # Convert the matrix board to string
        board_as_string = utils.list_of_list_board_to_str(b)
        index_from = 8 * x_from + y_from + 1
        index_to = 8 * x_to + y_to + 1
        print("Moving " + board_as_string[8 * x_from + y_from] + " str_position: " + str(index_from - 1) + " to " +
              board_as_string[8 * x_to + y_to] + " str_position: " + str(index_to - 1))

        game_input = move
        # ToDo: validate move
        if board.validate_move(move):
            board.move(move)
            # The moving piece
            moving_piece = board_as_string[8 * x_from + y_from]
            save_turn(moving_piece, index_from, index_to)
            turn_counter += 1
        else:
            print("----- WARNING: Illegal move, please try again: ------")
            input("Press Enter to continue...")


start_game()
