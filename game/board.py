from game.piece import Piece
from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn
from game.exceptions import NotPieceToMove, NotPermitedMove

class Board:
   
    #esta funcion inicia el tablero y establece las posiciones de las piezas
    def __init__(self): #Asi inicia el tablero
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        
        self.pieces_from_white = [] #las piezas que capturo BLACK
        
        self.pieces_from_black = [] #las piezas que capturo WHITE
        
        
        self.pieces_from_white_piece = [] #las piezas que capturo BLACK
        
        self.pieces_from_black_piece = [] #las piezas que capturo WHITE
        
        
        self.__positions__[0][0] = Rook("BLACK") #torre negra
        self.__positions__[0][7] = Rook("BLACK") #torre negra
        
        self.__positions__[7][7] = Rook("WHITE") #torre blanca
        self.__positions__[7][0] = Rook("WHITE") #torre blanca


        #Areglo para ahorrar el hardcode
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK") #peon negro
        
            self.__positions__[6][col] = Pawn("WHITE") #peon blanco
        
        
        self.__positions__[0][1] = Knight("BLACK") #caballo negro
        self.__positions__[0][6] = Knight("BLACK") #caballo negro
        
        self.__positions__[7][1] = Knight("WHITE") #caballo blanco
        self.__positions__[7][6] = Knight("WHITE") #caballo blanco

        
        self.__positions__[0][2] = Bishop("BLACK") #alfil negro
        self.__positions__[0][5] = Bishop("BLACK") #alfil negro

        self.__positions__[7][2] = Bishop("WHITE") #alfil blanco
        self.__positions__[7][5] = Bishop("WHITE") #alfil blanco

        
        self.__positions__[0][3] = Queen("BLACK") #reina negra

        self.__positions__[7][3] = Queen("WHITE") #reina blanca

    
        self.__positions__[0][4] = King("BLACK") #rey negro

        self.__positions__[7][4] = King("WHITE") #rey blanco


    # Esta funcion lo que hace es obtener las piezas y los equipos
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]

        if piece is None:
            return "No piece"
        else:
            return piece
    

    # Esta funcion lo que hace es mover las piezas        
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            raise NotPieceToMove("No hay una pieza para mover")
        destination = self.__positions__[to_row][to_col]
        if destination is not None and destination.__color__ == piece.__color__:
            raise NotPermitedMove("Cannot move to a position occupied by a piece with the same color")
        if not self.permited_move(from_row, from_col, to_row, to_col):
            raise NotPermitedMove("The piece cannot be moved in this position")
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None
        print(f"Moved piece from: ", {from_row}, {from_col},     "to: ", {to_row}, {to_col})


    def show_board(self):

        print("    ", end="")
        for col in range(8):
            print(f"    {col} ", end="")
        print() 

        for row in range(8):
            print(f" {row} ║", end="")  

            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    print("     ", end="║")  # Espacio en blanco si no hay pieza
                else:
                    print(" ", piece.__str__()," ",  end="║")  # Muestra inicial del tipo y color de la pieza
            print()
            print("    " + "══════" * 8 + "")  # Línea separadora entre filas
        
        
    # Esta funcion lo que hace es verificar si el movimiento es permitido
    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]

        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False  # No hay pieza para mover
        return piece.permited_move(from_row, from_col, to_row, to_col, self)


    # Con esta funcion damos vida al sistema de ataque
    def capture_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        destination = self.__positions__[to_row][to_col]
        if destination is not None:
            if destination.__color__ != piece.__color__:
                if piece.__color__ == "WHITE":
                    self.pieces_from_black.append(destination.__str__())
                    self.pieces_from_black_piece.append(destination)
                    print("La pieza que blanco capturo es: ")
                    return (self.pieces_from_black)
                else:
                    self.pieces_from_white.append(destination.__str__())
                    self.pieces_from_white_piece.append(destination)
                    print("La pieza que negro capturo es: ")
                    return (self.pieces_from_white)
        else:
            return False

    #Esta funcion lo que hace es mostrar con el str la pieza que elejiste en el tablero, en caso de aberte equivocado al elegir la pieza te va a decir que no hay ninguna    
    def piece_to_STR(self, row, col):
        piece = self.__positions__[row][col]
        
        if piece is None:
            return "No piece"
        else:
            return ({piece.__type__}, {piece.__color__})
        