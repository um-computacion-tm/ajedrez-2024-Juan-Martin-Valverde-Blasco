# game/bishop.py
from game.piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

    def __str__(self):
        return " ♝" if self.__color__ == "WHITE" else " ♗"

    def permited_move(self, board, from_row, from_col, to_row, to_col):
        piece = board.__positions__[from_row][from_col]
        
        if piece.__type__ == "BISHOP":
            if abs(to_row - from_row) == abs(to_col - from_col):
                row_step = 1 if to_row > from_row else -1
                col_step = 1 if to_col > from_col else -1
                current_row, current_col = from_row + row_step, from_col + col_step
                
                while current_row != to_row and current_col != to_col:
                    if board.__positions__[current_row][current_col] is not None:
                        return False
                    current_row += row_step
                    current_col += col_step
                
                return True
            else:
                return False