from itertools import product

COLUMNS = 'abcdefgh'
ROWS = '12345678'


def get_position_indeces(position):
    return COLUMNS.index(position[0]), ROWS.index(position[1])


def get_rook_steps(position):
    """
    :param position:
    :return: return all possible rook steps
    """
    steps = set()
    steps.update([el[0] + el[1] for el in product(position[0], ROWS)])
    steps.update([el[0] + el[1] for el in product(COLUMNS, position[1])])
    steps.remove(position)
    return steps


def get_knight_steps(position):
    """
    :param position:
    :return: return all possible knight steps
    """
    steps = set()
    cols = '  ' + COLUMNS + '  '
    rows = '  ' + ROWS + '  '
    index_col, index_row = get_position_indeces(position)

    buff = [cols[index_col - 2] + rows[index_row + 1], cols[index_col - 2] + rows[index_row - 1],
            cols[index_col - 1] + rows[index_row + 2], cols[index_col - 1] + rows[index_row - 2],
            cols[index_col + 1] + rows[index_row + 2], cols[index_col + 1] + rows[index_row - 2],
            cols[index_col + 2] + rows[index_row + 1], cols[index_col + 2] + rows[index_row - 1]]

    steps.update([el for el in buff if ' ' not in el])
    return steps


def get_bishop_steps(position):
    """
    :param position:
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


def get_queen_steps(position):
    """
    :param position:
    :return: return all possible queen steps
    """
    return get_rook_steps(position) | get_bishop_steps(position)


def get_king_steps(position, color):
    """
    :param position:
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


def get_pawn_steps(position, color):
    """
    :param position:
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


