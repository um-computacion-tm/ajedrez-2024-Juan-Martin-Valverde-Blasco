from game.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK"

    def __str__(self):
        return " ♜" if self.__color__ == "WHITE" else " ♖"

 
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if to_row == from_row and to_col != from_col:
            return True
        elif to_col == from_col and to_row != from_row:
            return True
        return False
    