"""
Base board class
Glossary:
R - Rook
N - Knight
B - Bishop
Q - Queen
K - King
P - Pawn
. - blank field
lowercase for black pieces
uppercase for white pieces
"""

from utils.utils import del_all_spaces
from itertools import product
from collections import Counter


class Field:
    available_moves = set([])
    count_attack = 0
    position = None
    piece = None

    def __init__(self, position, piece):
        self.position = position
        self.piece = piece

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def add_available_move(self, available_move):
        self.available_moves.add(available_move)

    def get_available_moves(self):
        return self.available_moves

    def reset_available_moves(self):
        self.available_moves.clear()

    def __str__(self):
        return self.piece


class Board:
    fields = {}

    @staticmethod
    def fill_blank_fields(string, ):
        if len(string) < 32:
            return string + '.' * (32 - len(string))

    @staticmethod
    def validate_board_str(init_board_str):
        availiable = '.rnbqkp'
        if len(init_board_str) != 64:
            raise ValueError('Give more than 64 fields to board')
        else:
            for letter in init_board_str:
                if letter.lower() not in availiable:
                    raise ValueError('Give incorrect symbols')

            count = Counter(init_board_str)
            if count['k'] > 1 or count['K'] > 1:
                raise ValueError('There are more than 1 king with same color')

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

    def print_board(self):
        count = 0
        rows = 8
        print(rows, ')', '  ', end='', sep='')

        for field in product('87654321', 'abcdefgh'):
            if count and count % 8 == 0:
                rows -= 1
                print()
                print(rows, ')', '  ', end='', sep='')

            print(self.fields[field[1]+field[0]], '', end='')
            count += 1
        print()
        print('-' * 19)
        print('    a b c d e f g h')

    def _init_fields(self, init_board_str):
        index = 0
        for field in product('1234', 'abcdefgh'):
            name_field = field[1]+field[0]
            self.fields[name_field] = Field(name_field, init_board_str[index])
            index += 1

        for field in product('8765', 'abcdefgh'):
            name_field = field[1]+field[0]
            self.fields[name_field] = Field(name_field, init_board_str[index])
            index += 1

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
        self._init_fields(init_board_str)


