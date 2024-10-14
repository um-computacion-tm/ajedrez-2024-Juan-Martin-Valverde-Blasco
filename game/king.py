
from game.piece import Piece

class King(Piece):
    __type__ = "KING"
    __white_str__ = "♚"
    __black_str__ = "♔"


    #Esta funcion lo que hace es el movimiento del rey utilizando la funciones que tenemos en piece
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1 and not (from_row == to_row and from_col == to_col):
            return True
        else: 
            return False
        

