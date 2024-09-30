from game.piece import Piece

class Bishop(Piece):
    __type__ = "BISHOP"
    __white_str__ = " ♝"
    __black_str__ = " ♗"


    def permited_move(self, from_row, from_col, to_row, to_col, board):
        permited_move_diag = self.permited_move_diagonal(from_row, from_col, to_row, to_col, board)
        if permited_move_diag == True:
            return True
        else:
            return False
 