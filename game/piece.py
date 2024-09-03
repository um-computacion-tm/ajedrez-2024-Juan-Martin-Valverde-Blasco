from game.board import Board, piece, from_col, from_row, to_col, to_row

class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None
    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK"

    def __str__(self):
        return " ♜" if self.__color__ == "WHIE" else " ♖"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]
   
        if piece.__type__ == "ROOK":
            if to_row == from_row and to_col != from_col:
                return True
            elif to_col == from_col and to_row != from_row:
                return True
            else:
                return False

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



class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

    def __str__(self):
        return " ♝" if self.__color__ == "WHITE" else " ♗"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]
        
        if piece.__type__ == "BISHOP":
            if abs(to_row - from_row) == abs(to_col - from_col):
                return True
            else:
                return False
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "QUEEN"

    def __str__(self):
        return " ♛" if self.__color__ == "WHITE" else " ♕"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]

        
        if piece.__type__ == "QUEEN":

        
            n = []
            if to_row == from_row and to_col != from_col:
                return True
            elif to_col == from_col and to_row != from_row:
                return True
            elif abs(to_row - from_row) == abs(to_col - from_col):
                return True
            else:
                return False



class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"

    def __str__(self):
        return " ♚" if self.__color__ == "WHITE" else " ♔"

    def permited_move(self, from_row, from_col, to_row, to_col): 
        piece = self.__positions__[from_row][from_col]

        if piece.__type__ == "KING":

            if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1 and not (from_row == to_row and from_col == to_col):
                return True
            else: 
                return False
        


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
        
        
        
        
