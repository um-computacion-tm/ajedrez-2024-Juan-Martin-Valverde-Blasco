from game.piece import Piece

class Queen(Piece):
    __type__ = "QUEEN"
    __white_show__ = "♛"
    __black_show__ = "♕"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        
        permited_move_diag = self.permited_move_diagonal(from_row, from_col, to_row, to_col, board)
        permitted_move_orthogonal = self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board)


        if permited_move_diag or permitted_move_orthogonal == True:
            return True
        else:
            return False
