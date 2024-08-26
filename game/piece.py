
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None

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