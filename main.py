from board import Board
from save_game import create_game_file


def start_game():
    print("Starting new chess game")
    board = Board()
    game_input = ''
    create_game_file(board)

    # game loop
    while game_input != "quit":
        board.print_board()
        # board.board_to_str()
        print("Board representation in one single line: ")
        print(board.board_to_str())

        move = input("Move:")
        game_input = move
        board.move(move)

        # ToDo: write to file
        # create_game_file(board) # this overrides the current file, must use seek()


start_game()
