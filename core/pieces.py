from itertools import product

COLUMNS = 'abcdefgh'
ROWS = '12345678'


def get_position_indeces(position):
    return COLUMNS.index(position[0]), ROWS.index(position[1])


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
    index_col, index_row = get_position_indeces(position)

    buff = [cols[index_col - 2] + rows[index_row + 1], cols[index_col - 2] + rows[index_row - 1],
            cols[index_col - 1] + rows[index_row + 2], cols[index_col - 1] + rows[index_row - 2],
            cols[index_col + 1] + rows[index_row + 2], cols[index_col + 1] + rows[index_row - 2],
            cols[index_col + 2] + rows[index_row + 1], cols[index_col + 2] + rows[index_row - 1]]

    steps.update([el for el in buff if ' ' not in el])
    return steps


def get_bishop_steps(position):
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


print(get_bishop_steps('h1'))

