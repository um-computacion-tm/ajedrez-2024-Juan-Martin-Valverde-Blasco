
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK" 

# No puedo hacer la funcion aca porque me da un error de importacion circular (En board importo piece y en piece importo board)
    # def permited_move_rook(self, from_row, from_col, to_row, to_col):
    #     piece = self.board.get_piece(from_row, from_col)
    #     if piece.__type__ == "ROOK":
    #         if to_row == from_row and to_col != from_col:
    #             return True
    #         elif to_col == from_col and to_row != from_row:
    #             return True
    #         else:
    #             return False


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "QUEEN"

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"