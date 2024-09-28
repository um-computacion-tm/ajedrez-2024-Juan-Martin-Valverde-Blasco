from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Chess:
    # Esta funcion inicia el funcionamiento del ajedrez como iniciar el tablero y el turno de blanco que es el que siempre mueve primero
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    # Esta funcion es otra verificacion de que la pieza a mover entre en el tablero
    def movement_fits(self,from_row, from_col, to_row, to_col):
        
        piece = self.__board__.get_piece(from_row, from_col)
        if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
        return ("The movement will be: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
        
    # Esta funcion verifica que la pieza que se va a mover pertenese a tu equipo
    def move_correct_color(self, from_row, from_col):

        print(self.__board__.get_piece(from_row, from_col))
        piece = self.__board__.get_piece(from_row, from_col)
        piece_type, piece_color = piece
        color = list(piece_color)[0]
        if color == self.__turn__:
            True
        else:
            return "You can't move a piece that is not your color"

    # Esta funcion es la que proboca que los turnos cambien
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
            
            
    # Esta funcion me costo un huevo hacerla y tambien pedircela a copilot 
    # Es para que el peon que llega al otro lado se convierta en otra pieza diferente
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


    # Esta funcion lo que hace es que una vez que el peon cambia de pieza
    # aca podes elejir a cual del equipo que le corresponde a cada uno
    # es la misma que tenia antes partida por equipo pero ahora en una sola para que la complejidad no me salte jajajaajaj
    def define_new_piece(self, from_row, from_col, to_row, to_col, pieces_from_piece):
                print("Las piezas a elegir son: ", pieces_from_piece)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =pieces_from_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.show())
                
                return new_piece
    

    #Esto hace que se levante el tema de que no entra en el tablero        
    def error_out_of_range(self, row, col):
        if not (0 <= row <= 7) or not (0 <= col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")

     
    def show_captured_pieces(self):
         if self.__turn__ == "WHITE" and len(self.__board__.pieces_from_black) > 0:
              return "The captured pieces from black are: ", self.__board__.pieces_from_black
         elif self.__turn__ == "BLACK" and len(self.__board__.pieces_from_white) > 0:
              return "The captured pieces from white are: ", self.__board__.pieces_from_white
         else:
              return "No pieces have been captured yet"
         
         
    def verify_winner(self):
         if len(self.__board__.pieces_from_black_piece) == 16:
              return "WHITE IS THE OUTLAW KING"
         elif len(self.__board__.pieces_from_white_piece) == 16:
              return "BLACK IS THE OUTLAW KING"
         else:
              return False
              