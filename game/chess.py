from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self,from_row, from_col, to_row, to_col):
        
        piece = self.__board__.get_piece(from_row, from_col)
        if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
        return ("Esto devuelve move: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
        
    def move_correct_color(self, from_row, from_col):

        print(self.__board__.get_piece(from_row, from_col))
        piece = self.__board__.get_piece(from_row, from_col)

        piece_type, piece_color = piece
        
        
        color = list(piece_color)[0]

        if color == self.__turn__:
            True
        else:
            
            return "You can't move a piece that is not your color"

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
            