from board import Board
from save_game import create_game_file, save_turn


def start_game():
    print("Starting new chess game")
    board = Board()
    b = board.board_to_list_of_list()
    game_input = ''
    create_game_file(board, b)

    # game loop
    while game_input != "quit":
        board.print_board()
        # board.board_to_str()
        print("Board representation as a list: ")
        print(board.board_to_list())
        print("Board representation as a list of list: ")
        b = board.board_to_list_of_list()
        print(b)
        print("Board representation in one single line: ")
        print(board.board_to_str())
        print("Board representation in one single line 2: ")
        print(board.list_of_list_board_to_str(b))

        move = input("Move:")
        print("file, rank, x, y")
        # file, rank, x, y = board.square_to_list_index_position(move)
        # print(file + ', ' + rank + ', ' + str(x) + ', ' + str(y))
        square_from, square_to = board.parse_move_to_square(move)
        print(square_from, square_to)
        file_from, rank_from, x_from, y_from = board.parse_square_to_list_index_position(str(square_from))
        print(file_from + ', ' + rank_from + ', ' + str(x_from) + ', ' + str(y_from))
        file_to, rank_to, x_to, y_to = board.parse_square_to_list_index_position(str(square_to))
        print(file_to + ', ' + rank_to + ', ' + str(x_to) + ', ' + str(y_to))

        print("piece at board string")
        board_as_string = board.list_of_list_board_to_str(b)
        print(board_as_string[8*x_from + y_from])
        print(board_as_string[8 * x_to + y_to])
        print("piece index")
        index_from = 8*x_from + y_from + 1
        print(index_from, "index_from: ")
        index_to = 8*x_to + y_to + 1
        print(index_to, "index_to: ")


        game_input = move
        board.move(move)

        save_turn(index_from, index_to)


start_game()
