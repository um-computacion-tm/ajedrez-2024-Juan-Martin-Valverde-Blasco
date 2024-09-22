from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self,from_row, from_col, to_row, to_col):
        
        piece = self.__board__.get_piece(from_row, from_col)
        if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
        return ("Esto devuelve move: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
        
    def move_correct_color(self, from_row, from_col):

        print(self.__board__.get_piece(from_row, from_col))
        piece = self.__board__.get_piece(from_row, from_col)

        piece_type, piece_color = piece
        
        
        color = list(piece_color)[0]

        if color == self.__turn__:
            True
        else:
            
            return "You can't move a piece that is not your color"

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
            
    def change_pawn_for_other(self, from_row, from_col, to_row, to_col):
        destination = self.__board__.get_piece(to_row, to_col)  
        if "PAWN" in destination[0] and "WHITE" in destination[1] and to_row == 0:
            if self.__board__.pieces_from_black_piece:  
                self.define_new_piece_white(from_row, from_col, to_row, to_col)
            else:
                raise NotPieceToReplace("No pieces have been eaten from WHITE")        
        elif "PAWN" in destination[0] and "BLACK" in destination[1] and to_row == 7:
            if self.__board__.pieces_from_white_piece: 
                self.define_new_piece_black(from_row, from_col, to_row, to_col)
            else:
                raise NotPieceToReplace("No pieces have been eaten from BLACK")
    def define_new_piece_white(self, from_row, from_col, to_row, to_col):
                print("Las piezas a elegir son: ", self.__board__.pieces_from_white)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =self.__board__.pieces_from_white_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.__str__())

                return new_piece
    
    def define_new_piece_black(self, from_row, from_col, to_row, to_col):
                print("Las piezas a elegir son: ", self.__board__.pieces_from_black)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =self.__board__.pieces_from_black_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.__str__())

                return new_piece