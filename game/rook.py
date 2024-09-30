from game.piece import Piece as piece

class Rook(piece):
    __type__ = "ROOK" 
    __white_str__  = " ♜"
    __black_str__  = " ♖"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board):
            return True
        return False