from game.piece import Piece

class Bishop(Piece):
    __type__ = "BISHOP"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        permited_move_diag = self.permited_move_diagonal(from_row, from_col, to_row, to_col, board)

        if permited_move_diag == True:
            return True
        else:
            return False
        
    def show(self):
        if self.__color__ == "WHITE":
            return "♝"
        else:
            return "♗"