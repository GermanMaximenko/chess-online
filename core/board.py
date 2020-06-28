"""
Base board class
Glossary:
R - Rook
N - Knight
B - Bishop
Q - Queen
K - King
. - blank field
lowercase for black figures
uppercase for white figures
"""

from utils.utils import del_all_spaces



class Board:
    fields = {}

    @staticmethod
    def fill_blank_fields(string):
        if len(string) < 32:
            return string + '.' * (32 - len(string))

    @staticmethod
    def validate_board_str(init_board_str):
        availiable = '.rnbqk'
        if len(init_board_str) != 64:
            raise ValueError('Incorrect init str')
        else:
            for letter in init_board_str:
                if letter not in availiable:
                    raise ValueError('Incorrect init str')

    def parse_board_str(self, init_board_str):
        init_board_str = del_all_spaces(init_board_str)
        res = ''
        for letter in init_board_str:
            if letter.isdigit():
                res += '.' * int(letter)
            else:
                res += letter
        left, right = res.split('/')
        return self.fill_blank_fields(left) + self.fill_blank_fields(right)

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
        init_board_str = self.parse_board_str(init_board_str)
        self.validate_board_str(init_board_str)




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
