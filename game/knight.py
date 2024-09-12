from game.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"

    def __str__(self):
        return " ♞" if self.__color__ == "WHITE" else " ♘"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        valid_moves = [
            (2, 1), (-2, -1), (2, -1), (-2, 1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
        return (to_row - from_row, to_col - from_col) in valid_moves
    