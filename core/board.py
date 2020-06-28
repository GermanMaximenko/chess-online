"""
Base board class
Glossary:
R - Rook
N - Knight
B - Bishop
Q - Queen
K - King
lowercase for black figures
uppercase for white figures
"""

class Board:
    fields = {}

    def __init__(self, init_board_str):
        """
        :param init_board_str: get str to initialize chess board
        str must contain 32 or less fields from 1a to 4h
            and 32 or less fields from 8a to 5h separated by '/'
            the numbers in the str mean the quantity of blank fields
            but if you dont give the numbers they will be blank by default
            spaces and end of line mean nothing in str, so you can use them to visual highlight
        example: 'RNBQKBNR PPPPPPPP/rnbqkbnr pppppppp' -base chess init
        """
        pass


class Field:
    availible_move = set([])
    count_attack = 0
    figure = None

    def __init__(self, figure):
        self.figure = figure

    def set_figure(self, figure):
        self.figure = figure

    def get_figure(self):
        return self.figure
