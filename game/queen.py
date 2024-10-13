from game.piece import Piece
        
class Queen(Piece):
    __type__ = "QUEEN"
    __white_str__  = " ♛"
    __black_str__  = " ♕"

    #Esta funcion lo que hace es el movimiento de la reina utilizando la funciones que tenemos en piece
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        permited_move_diag = self.permited_move_diagonal(from_row, from_col, to_row, to_col, board)
        permitted_move_orthogonal = self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board)
        if permited_move_diag or permitted_move_orthogonal == True:
            return True
        else:
            return False


