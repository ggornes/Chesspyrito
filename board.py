import chess


class Board:

    def __init__(self):
        self.__board = chess.Board()

    def print_board(self):
        print(self.__board)

    def move(self, uci_move):
        m = chess.Move.from_uci(uci_move)
        self.__board.push(m)

    def board_to_list(self):
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        return list_board

    def board_to_list_of_list(self):
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        list_of_list_board =[line.split(",") for line in list_board]
        return list_of_list_board

    def board_to_str(self):
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        line_board = '/'.join(list_board)
        return line_board
