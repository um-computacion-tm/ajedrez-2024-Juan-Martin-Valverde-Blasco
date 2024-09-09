
from game.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"

    def __str__(self):
        return " ♚" if self.__color__ == "WHITE" else " ♔"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]

        if piece.__type__ == "KING":

            if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1 and not (from_row == to_row and from_col == to_col):
                return True
            else: 
                return False
        

