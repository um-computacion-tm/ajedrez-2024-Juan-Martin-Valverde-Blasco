from game.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self,from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)

        if piece == "No piece":
            print("You can't move a piece that doesn't exist")
            return "You can't move a piece that doesn't exist"

    
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
       
    def move_correct_color(self, from_row, from_col):

        # piece = self.__board__.get_piece(from_row, from_col)
        print(self.__board__.get_piece(from_row, from_col))
        piece = self.__board__.get_piece(from_row, from_col)

        # Desempacamos la tupla en tipo de pieza y color
        piece_type, piece_color = piece
        
        # Convertimos el conjunto del color a una lista y accedemos al primer elemento
        color = list(piece_color)[0]

        if color == self.__turn__:
            True
        else:
            #print("You can't move a piece that is not your color, your color is: ", self.__turn__, "You are trying to move: ", color)
            return "You can't move a piece that is not your color"

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"