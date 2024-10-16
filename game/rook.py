from game.piece import Piece


class Rook(Piece):
    __type__ = "ROOK" 
    __white_show__ = "♜"
    __black_show__ = "♖"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        return self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board)

    
