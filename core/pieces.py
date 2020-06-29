from itertools import product

COLUMNS = 'abcdefgh'
ROWS = '12345678'


def get_position_indeces(position):
    return COLUMNS.index(position[0]), ROWS.index(position[1])


def get_piece_color(piece):
    return 'black' if piece.islower() else 'white'


def get_rook_steps(position: str, blocks=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible rook steps considering blocks
    """

    steps = set()
    steps.update([el[0] + el[1] for el in product(position[0], ROWS)])
    steps.update([el[0] + el[1] for el in product(COLUMNS, position[1])])
    steps.remove(position)
    return steps


def get_knight_steps(position: str, blocks=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible knight steps
    """

    steps = set()
    cols = '  ' + COLUMNS + '  '
    rows = '  ' + ROWS + '  '
    index_col, index_row = cols.index(position[0]), rows.index(position[1])

    buff = [cols[index_col - 2] + rows[index_row + 1], cols[index_col - 2] + rows[index_row - 1],
            cols[index_col - 1] + rows[index_row + 2], cols[index_col - 1] + rows[index_row - 2],
            cols[index_col + 1] + rows[index_row + 2], cols[index_col + 1] + rows[index_row - 2],
            cols[index_col + 2] + rows[index_row + 1], cols[index_col + 2] + rows[index_row - 1]]

    steps.update([el for el in buff if ' ' not in el])
    return steps


def get_bishop_steps(position: str, blocks=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible bishop steps
    """
    steps = set()
    index_col, index_row = get_position_indeces(position)

    def next_indeces(mode, col, row):
        if mode == 0:
            col -= 1
            row += 1
        elif mode == 1:
            col += 1
            row += 1
        elif mode == 2:
            col += 1
            row -= 1
        elif mode == 3:
            col -= 1
            row -= 1
        return col, row

    for i in range(4):
        index_col, index_row = next_indeces(i, index_col, index_row)
        while 0 <= index_col < 8 and 0 <= index_row < 8:
            steps.add(COLUMNS[index_col] + ROWS[index_row])
            index_col, index_row = next_indeces(i, index_col, index_row)
        index_col, index_row = get_position_indeces(position)

    return steps


def get_queen_steps(position: str, blocks_rook=None, blocks_bish=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible queen steps
    """
    return get_rook_steps(position, blocks_rook) | get_bishop_steps(position, blocks_bish)


def get_king_steps(position: str, color: str, blocks=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible king steps
    """
    steps = set()
    index_col, index_row = get_position_indeces(position)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= index_col + i < 8 and 0 <= index_row - j < 8:
                steps.add(COLUMNS[index_col + i] + ROWS[index_row - j])
    steps.remove(position)
    if color == 'white' and position == 'e1':
        steps.add('c1')
        steps.add('g1')
    elif color == 'black' and position == 'e8':
        steps.add('c8')
        steps.add('g8')
    return steps


def get_pawn_steps(position: str, color: str, blocks=None) -> set:
    """
    :param position:
    :param blocks:  possible keys top, right, down, left, all. key->blocked_position
    :return: return all possible pawn steps
    """
    steps = set()
    index_col, index_row = get_position_indeces(position)

    if color == 'white':

        for i in range(-1, 2):
            if 0 <= index_col + i < 8 and index_row + 1 < 8:
                steps.add(COLUMNS[index_col + i] + ROWS[index_row + 1])
        if index_row == 1:
            steps.add(COLUMNS[index_col] + ROWS[index_row + 2])

    elif color == 'black':

        for i in range(-1, 2):
            if 0 <= index_col + i < 8 and index_row - 1 >= 0:
                steps.add(COLUMNS[index_col + i] + ROWS[index_row - 1])
        if index_row == 6:
            steps.add(COLUMNS[index_col] + ROWS[index_row - 2])
    return steps


def get_rook_blocks(position, color, fields):
    cols = ' ' + COLUMNS + ' '
    rows = ' ' + ROWS + ' '
    index_col, index_row = cols.index(position[0]), rows.index(position[1])

    for k, v in fields:
        pass


def get_knight_blocks(position, color,  fields):
    pass


def get_bishop_blocks(position, color,  fields):
    pass


def get_queen_blocks(position, color,  fields):
    pass


def get_king_blocks(position, color,  fields):
    pass


def get_pawn_blocks(position, color,  fields):
    pass


def get_piece_step(piece, position, fields):
    color = get_piece_color(piece)
    piece = piece.lower()
    if piece == 'p':
        return get_pawn_steps(position, color, get_pawn_blocks(position, fields, color))
    elif piece == 'r':
        return get_rook_steps(position, get_rook_blocks(position, fields, color))
    elif piece == 'n':
        return get_knight_steps(position, get_knight_blocks(position, fields, color))
    elif piece == 'b':
        return get_bishop_steps(position, get_bishop_blocks(position, fields, color))
    elif piece == 'q':
        rook_blocks = get_rook_blocks(position, fields, color)
        bish_blocks = get_bishop_blocks(position, fields, color)
        return get_queen_steps(position, rook_blocks, bish_blocks)
    elif piece == 'k':
        return get_king_steps(position, color, get_king_blocks(position, fields, color))
