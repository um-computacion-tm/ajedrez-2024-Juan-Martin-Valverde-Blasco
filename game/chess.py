from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace, IsNotYourColor

class Chess:
    # Esta funcion inicia el funcionamiento del ajedrez como iniciar el tablero y el turno de blanco que es el que siempre mueve primero
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    # Esta funcion es otra verificacion de que la pieza a mover entre en el tablero
    def movement_fits(self,from_row, from_col, to_row, to_col):

        self.error_out_of_range(to_row, to_col)

        return ("El movimiento va a aser: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
                        
    # Esta funcion verifica que la pieza que se va a mover pertenese a tu equipo
    def right_color(self, from_row, from_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise NotPieceToMove("No hay una pieza en la posicion especificada.")

        __type__, piece_color = piece
        color = list(piece_color)[0]

        if color != self.__turn__:
            raise IsNotYourColor(f"No podes mover una pieza que no es la de tu color, tiene que ser color {self.__turn__}.")

        return True
    
    # Esta funcion es la que proboca que los turnos cambien
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
            
            
    # Esta funcion me costo un huevo hacerla y tambien pedircela a copilot 
    # Es para que el peon que llega al otro lado se convierta en otra pieza diferente
    def change_pawn(self, from_row, from_col, to_row, to_col):
        destination = self.__board__.get_piece(to_row, to_col)
        
        if destination.__type__ == "PAWN" and destination.__color__ == "WHITE" and to_row == 0:
            pieces_from_piece = self.__board__.pieces_from_white_piece
        elif destination.__type__ == "PAWN" and destination.__color__ == "BLACK" and to_row == 7:
            pieces_from_piece = self.__board__.pieces_from_black_piece
        else:
            return
    
        if pieces_from_piece:
            self.define_new_piece(from_row, from_col, to_row, to_col, pieces_from_piece)
        else:
            raise NotPieceToReplace("No hay piezas capturadas por las que cambiar al " + destination[0])
        

    # Esta funcion lo que hace es que una vez que el peon cambia de pieza
    # aca podes elejir a cual del equipo que le corresponde a cada uno
    # es la misma que tenia antes partida por equipo pero ahora en una sola para que la complejidad no me salte jajajaajaj
    def define_new_piece(self, from_row, from_col, to_row, to_col, pieces_from_piece):
                print("Las piezas a elegir son: ", pieces_from_piece)
                index = int(input("Ingresa un numero en la lista por el que quieras cambiar al peon: "))
                new_piece =pieces_from_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("La pieza elejida es : ", new_piece.__str__())
                
                return new_piece
    

    #Esto hace que se levante el tema de que no entra en el tablero        
    def error_out_of_range(self, row, col):
        if not (0 <= row <= 7) or not (0 <= col <= 7):
            raise InvalidPosition("Posicion invalida, tiene que estar entre los valores 0 a 7.")

     
    def STR_captured_pieces(self):
         if self.__turn__ == "WHITE" and len(self.__board__.pieces_from_black) > 0:
              return "Las piezas capturadas del BLACK son: ", self.__board__.pieces_from_black
         elif self.__turn__ == "BLACK" and len(self.__board__.pieces_from_white) > 0:
              return "Las piezas capturadas del WHITE son: ", self.__board__.pieces_from_white
         else:
              return "El equipo esta completo"
         
         
    def verify_winner(self):
        # Verificar si todas las piezas negras han sido capturadas
        if len(self.__board__.pieces_from_black_piece) == 16:
            return "Equipo WHITE gana"
        # Verificar si todas las piezas blancas han sido capturadas
        elif len(self.__board__.pieces_from_white_piece) == 16:
            return "Equipo BLACK gana"
        # Verificar si el rey negro ha sido capturado
        elif not any(piece.__type__ == 'KING' and piece.__color__ == 'BLACK' for piece in self.__board__.pieces_from_black_piece):
            return "Equipo WHITE gana"
        # Verificar si el rey blanco ha sido capturado
        elif not any(piece.__type__ == 'KING' and piece.__color__ == 'WHITE' for piece in self.__board__.pieces_from_white_piece):
            return "Equipo BLACK gana"
        else:
            return False          