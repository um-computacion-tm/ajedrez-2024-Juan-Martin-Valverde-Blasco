from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove, NotPieceToReplace

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    def move(self,from_row, from_col, to_row, to_col):

        self.verify_out_of_range(to_row, to_col)

        return ("Esto devuelve move: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
        

    def verify_out_of_range(self, row, col):
        # Validar que los valores estén dentro de los límites del tablero
        if not (0 <= row <= 7) or not (0 <= col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
        

    def move_correct_color(self, from_row, from_col):

        piece = self.__board__.get_piece(from_row, from_col)
        if piece == "No piece":
            return "You can't move a piece that doesn't exist"
            
        if piece.__color__ == self.__turn__:
            True
        else:
            #print("You can't move a piece that is not your color, your color is: ", self.__turn__, "You are trying to move: ", color)
            return "You can't move a piece that is not your color"

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def show_eaten_pieces(self):
         if self.__turn__ == "WHITE" and len(self.__board__.pieces_from_black) > 0:
              return "The eaten pieces from black are: ", self.__board__.pieces_from_black
         elif self.__turn__ == "BLACK" and len(self.__board__.pieces_from_white) > 0:
              return "The eaten pieces from white are: ", self.__board__.pieces_from_white
         else:
              return "No pieces have been eaten yet"
         
    def verify_winner(self):
         if len(self.__board__.pieces_from_black_piece) == 16:
              return "WHITE WINS"
         elif len(self.__board__.pieces_from_white_piece) == 16:
              return "BLACK WINS"
         else:
              return False
              

# BIEN, PERO SUGIERE PARA CAMBIAR PIEZAS QUE COMIO BLANCO DEL NEGRO Y LA CAMBIA POR UNA PIEZA DEL NEGRO Y NO DEL BLANCO

    def change_pawn_for_other(self, from_row, from_col, to_row, to_col):
        destination = self.__board__.get_piece(to_row, to_col)  # Obtener la pieza en la posición final
        
        # Verificar si el peón es blanco y ha llegado a la fila 0
        if destination.__type__ == "PAWN" and destination.__color__ == "WHITE" and to_row == 0:
            pieces_from_piece = self.__board__.pieces_from_white_piece
        elif destination.__type__ == "PAWN" and destination.__color__ == "BLACK" and to_row == 7:
            pieces_from_piece = self.__board__.pieces_from_black_piece
        else:
            return
    
        if pieces_from_piece:  # Verificar si hay piezas disponibles
            self.define_new_piece(from_row, from_col, to_row, to_col, pieces_from_piece)
        else:
            raise NotPieceToReplace("No pieces have been eaten from " + destination[0])
        
        # Verificar si el peón es negro y ha llegado a la fila 7

    def define_new_piece(self, from_row, from_col, to_row, to_col, pieces_from_piece):
                print("Las piezas a elegir son: ", pieces_from_piece)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =pieces_from_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.show())
                
                return new_piece
    

