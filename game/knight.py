from game.piece import Piece

class Knight(Piece):
    __type__ = "KNIGHT"
    __white_str__ = "♞"
    __black_str__ = "♘"


    #Esta funcion lo que hace es el movimiento del caballo utilizando la funciones que tenemos en piece
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        valid_moves = [
            (2, 1), (-2, -1), (2, -1), (-2, 1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
        return (to_row - from_row, to_col - from_col) in valid_moves
    
#COMPLETE