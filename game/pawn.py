from game.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"

    def __str__(self):
        return " ♟" if self.__color__ == "WHITE" else " ♙"
        
    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]

        if piece.__type__ == 'PAWN':
            direction = -1 if piece.__color__ == "white" else 1
        if to_col == from_col: 
            if (to_row - from_row) == direction and self.get_piece(to_row, to_col) == "No piece":
                return True
            if (from_row == 6 and piece.__color__ == "white") or (from_row == 1 and piece.__color__ == "black"):
                if (to_row - from_row) == 2 * direction and self.get_piece(to_row, to_col) == "No piece":
                    return True
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            destination_piece = self.get_piece(to_row, to_col)
            if destination_piece != "No piece" and destination_piece.__color__ != piece.__color__:
                return True
        else:
            return False
        
        
        
