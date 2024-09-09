from game.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"

    def __str__(self):
        return " ♞" if self.__color__ == "WHITE" else " ♘"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]

        if piece.__type__ == "KNIGHT":

            valid_moves = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
            if (from_row - to_row, from_col - to_col) in valid_moves:
                return True
            else:
                return False
