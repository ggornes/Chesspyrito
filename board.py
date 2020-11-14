import chess


class Board:

    def __init__(self):
        self.__board = chess.Board()

    def print_board(self):
        print(self.__board)

    def move(self, uci_move):
        m = chess.Move.from_uci(uci_move)
        self.__board.push(m)

    def board_to_str(self):
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        line_board = '/'.join(list_board)
        return line_board
