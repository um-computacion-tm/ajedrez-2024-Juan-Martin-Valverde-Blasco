from game.piece import Piece as piece

class Rook(piece):
    __type__ = "ROOK" 

    def __str__(self):
        return " ♜" if self.__color__ == "WHITE" else " ♖"
    
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board):
            return True
        return False