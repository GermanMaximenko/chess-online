from itertools import product

COLUMNS = 'abcdefgh'
ROWS = '12345678'


def get_rook_steps(position):
    steps = set()
    steps.update([el[0] + el[1] for el in product(position[0], COLUMNS)])
    steps.update([el[0] + el[1] for el in product(ROWS, position[1])])
    steps.remove(position)
    return steps


def get_knight_steps(position):
    steps = set()
    cols = '  ' + COLUMNS + '  '
    rows = '  ' + ROWS + '  '
    index_col = cols.index(position[0])
    index_row = rows.index(position[1])

    buff = [cols[index_col - 2] + rows[index_row + 1], cols[index_col - 2] + rows[index_row - 1],
            cols[index_col - 1] + rows[index_row + 2], cols[index_col - 1] + rows[index_row - 2],
            cols[index_col + 1] + rows[index_row + 2], cols[index_col + 1] + rows[index_row - 2],
            cols[index_col + 2] + rows[index_row + 1], cols[index_col + 2] + rows[index_row - 1]]

    steps.update([el for el in buff if ' ' not in el])
    return steps


