
from game.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"

    def __str__(self):
        return " ♚" if self.__color__ == "WHITE" else " ♔"
        
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            if self.permited_move_diagonal(from_row, from_col, to_row, to_col, board) or self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board):
                return True
        return False

        

