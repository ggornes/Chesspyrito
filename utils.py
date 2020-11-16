def split_string_to_chars(_string):
    """
    Split string characters and store them in an List[chr: c]
    :param _string: a string variable
    Example" split()
    :return:
    """
    return [char for char in _string]

def list_of_list_board_to_str(b):
    """
    Parse Board b List[List[Square]]
    b is a board represented as a list of lists
    b = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ...]
    :return: String:
    'rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR'
    Alternative:
    'rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR'
    """

    # line = ''.join(b[0]) + '/' + ''.join(b[1]) + '/' + ''.join(b[2]) + '/' + ''.join(b[3]) + '/' + ''.join(b[4]) + '/' + ''.join(b[5]) + '/' + ''.join(b[6]) + '/' + ''.join(b[7])
    # alternative
    line = ''.join(b[0]) + ''.join(b[1]) + ''.join(b[2]) + ''.join(b[3]) + ''.join(b[4]) + ''.join(b[5]) + ''.join(b[6]) + ''.join(b[7])
    return line
