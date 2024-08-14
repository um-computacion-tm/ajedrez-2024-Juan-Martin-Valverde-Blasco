from rook import Rook

class Board:
    def __init__(self):
        self.positions = []
        for _ in range (8):
            col = []
            for _ in range (8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][0] = Rook("Black")
        self.positions[7][7] = Rook("black")
        self.positions[7][0] = Rook("White")
        self.positions[0][7] = Rook("White")
    def get_piece(self, row, col):

        return self.__positions__[row][col]
    