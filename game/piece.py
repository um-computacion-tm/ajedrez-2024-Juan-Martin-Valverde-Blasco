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
        return "♜" if self.__color__ == "white" else "♖"

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"

    def __str__(self):
        return "♞" if self.__color__ == "white" else "♘"

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

    def __str__(self):
        return "♝" if self.__color__ == "white" else "♗"

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "QUEEN"

    def __str__(self):
        return "♛" if self.__color__ == "white" else "♕"

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"

    def __str__(self):
        return "♚" if self.__color__ == "white" else "♔"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"

    def __str__(self):
        return "♟" if self.__color__ == "white" else "♙"
        
        
        
        
        
