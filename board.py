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
        """
        Parse chess.Board() to a List[str: Rank]
        :return:
        ['rnbqkbnr',
        'pppppppp',
        '........',
        '........',
        '........',
        '........',
        'PPPPPPPP',
        'RNBQKBNR']
        """
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        return list_board

    @staticmethod
    def split_string_to_chars(_string):
        """
        Split string characters and store them in an List[chr: c]
        :param _string: a string variable
        Example" split()
        :return:
        """
        return [char for char in _string]

    def board_to_list_of_list(self):
        """
        Parse chess.Board() to a List[List[chr]]
        :return:
        [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        """
        # def split(_string):
        #     return [char for char in _string]

        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        list_of_list_board1 =[line.split(",") for line in list_board]
        list_of_list_board =[self.split_string_to_chars(l) for [l] in list_of_list_board1]
        return list_of_list_board

    def board_to_str(self):
        str_board = str(self.__board).replace(" ", "")
        list_board = str_board.split("\n")
        line_board = '/'.join(list_board)
        return line_board

    def list_of_list_board_to_str(self, b):
        """
        Parse Board b List[List[Square]]
        b = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ...]
        :return: String:
        'rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR'
        Alternative:
        'rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR'
        """
        # b is a board representation as a list of lists
        # [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ...]
        line = ''.join(b[0]) + '/' + ''.join(b[1]) + '/' + ''.join(b[2]) + '/' + ''.join(b[3]) + '/' + ''.join(b[4]) + '/' + ''.join(b[5]) + '/' + ''.join(b[6]) + '/' + ''.join(b[7])
        # alternative
        line = ''.join(b[0]) + ''.join(b[1]) + ''.join(b[2]) + ''.join(b[3]) + ''.join(b[4]) + ''.join(b[5]) + ''.join(b[6]) + ''.join(b[7])
        return line

    def parse_square_to_list_index_position(self,  square: str):
        """
        Decompose a square into a tuple (file, rank, x, y)
        :param square: a string representation of a square. Ex. 'a1'
        :return: a tuple that represents a square as (file, rank, x, y), where (x,y) are the index positions
        of the board stored as a "matrix" or a list of a list
        """
        file = self.split_string_to_chars(square)[0]
        rank = self.split_string_to_chars(square)[1]
        x = 8 - int(rank)
        y = ord(file) - 97
        print("Piece: ")
        board_list = self.board_to_list_of_list()
        print(board_list[x][y])
        return file, rank, x, y

    def parse_move_to_square(self, uci_move: str):
        """
        Decompose a uci_move into a tuple of squares
        :param uci_move: string representing a move. Example: 'a2a3'
        :return: tuple of squares. Example: (a2, a3)
        """
        chars = self.split_string_to_chars(uci_move)
        square_from = ''.join(chars[0] + chars[1])
        square_to = ''.join(chars[2] + chars[3])
        return square_from, square_to



