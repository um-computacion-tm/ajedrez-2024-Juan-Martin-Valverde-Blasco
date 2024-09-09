from game.piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

    def __str__(self):
        return " ♝" if self.__color__ == "WHITE" else " ♗"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]
        
        if piece.__type__ == "BISHOP":
            if abs(to_row - from_row) == abs(to_col - from_col):
                return True
            else:
                return False
