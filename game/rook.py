from game.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK"

    def __str__(self):
        return " ♜" if self.__color__ == "WHITE" else " ♖"

 
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if from_row != to_row and from_col != to_col:
            return False
        
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board.__positions__[from_row][col] is not None:
                    return False
        else:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board.__positions__[row][from_col] is not None:
                    return False
        
        return True