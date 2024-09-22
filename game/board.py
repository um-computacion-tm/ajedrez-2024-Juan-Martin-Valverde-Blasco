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
    def __init__(self): 
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        
        self.pieces_from_white = [] #Las piezas que capturo Negro
        
        self.pieces_from_black = [] #La piezas que capturo Blanco
       
       
        self.pieces_from_white_piece = [] #Las piezas que tiene Blanco
       
        self.pieces_from_black_piece = [] #Las piezas que tiene NEGRO
     
     
        self.__positions__[0][0] = Rook("BLACK") #alfil negro
        self.__positions__[0][7] = Rook("BLACK") #alfil negro
       
        self.__positions__[7][7] = Rook("WHITE") #alfil balnco
        self.__positions__[7][0] = Rook("WHITE") #alfil blanco


        self.__positions__[1][0] = Pawn("BLACK") #peon negro
        self.__positions__[1][1] = Pawn("BLACK") #peon negro
        self.__positions__[1][2] = Pawn("BLACK") #peon negro
        self.__positions__[1][3] = Pawn("BLACK") #peon negro
        self.__positions__[1][4] = Pawn("BLACK") #peon negro
        self.__positions__[1][5] = Pawn("BLACK") #peon negro
        self.__positions__[1][6] = Pawn("BLACK") #peon negro
        self.__positions__[1][7] = Pawn("BLACK") #peon negro
       
        self.__positions__[6][0] = Pawn("WHITE") #peon blanco
        self.__positions__[6][1] = Pawn("WHITE") #peon blanco
        self.__positions__[6][2] = Pawn("WHITE") #peon blanco
        self.__positions__[6][3] = Pawn("WHITE") #peon blanco
        self.__positions__[6][4] = Pawn("WHITE") #peon blanco
        self.__positions__[6][5] = Pawn("WHITE") #peon blanco
        self.__positions__[6][6] = Pawn("WHITE") #peon blanco
        self.__positions__[6][7] = Pawn("WHITE") #peon blanco

        
        self.__positions__[0][1] = Knight("BLACK") #caballo negro 
        self.__positions__[0][6] = Knight("BLACK") #caballo negro
       
        self.__positions__[7][1] = Knight("WHITE") #caballo blanco
        self.__positions__[7][6] = Knight("WHITE") #caballo blanco

        
        self.__positions__[0][2] = Bishop("BLACK") #torre negra
        self.__positions__[0][5] = Bishop("BLACK") #torre negra
       
        self.__positions__[7][2] = Bishop("WHITE") #torre blanca
        self.__positions__[7][5] = Bishop("WHITE") #torre blanca

    
        self.__positions__[0][3] = Queen("BLACK") #reina negra
       
        self.__positions__[7][3] = Queen("WHITE") #reina blanca


        self.__positions__[0][4] = King("BLACK") #rey negro
       
        self.__positions__[7][4] = King("WHITE") #rey blanco
    


    # Esta funcion lo que hace es obtener las piezas y los equipos
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]
        if piece is None:
            return "No piece"
        return ({piece.__type__}, {piece.__color__})
    


    # Esta funcion lo que hace es mover las piezas        
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            raise NotPieceToMove("No piece to move")
        destination = self.__positions__[to_row][to_col]
        if destination is not None and destination.__color__ == piece.__color__:
            raise NotPermitedMove("Cannot move to a position occupied by a piece with the same color")
        if not self.permited_move(from_row, from_col, to_row, to_col):
            raise NotPermitedMove("The piece cannot be moved in this position")
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None
        print(f"Moved piece from: {from_row}, {from_col} to: {to_row}, {to_col}")


    # Esta funcion lo que hace es mostrar el tablero
    def show_board(self):
            print("╔══╤══╤══╤══╤══╤══╤══╤══╗")
            for row in range(8):
                print("║", end="")
                for col in range(8):
                    piece = self.__positions__[row][col]
                    if piece is None:
                        if (row + col) % 2 == 0:
                            print("  ", end="")
                        else:
                            print("░░", end="")
                    else:
                        print(f" {piece}", end="")
                    if col < 7:
                        print("│", end="")
                print(f"║{8 - row}")
                if row < 7:
                    print("╟──┼──┼──┼──┼──┼──┼──┼──╢")
            print("╚══╧══╧══╧══╧══╧══╧══╧══╝")
            print("╰a─┈b─┈c─┈d─┈e─┈f─┈g─┈h─┈╯")    

    # Esta funcion lo que hace es verificar si el movimiento es permitido
    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False
        return piece.permited_move(from_row, from_col, to_row, to_col, self)

    # Con esta funcion damos vida al sistema de ataque
    def eat_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        destination = self.__positions__[to_row][to_col]
        if destination is not None:
            if destination.__color__ != piece.__color__:
                if piece.__color__ == "WHITE":
                    self.pieces_from_black.append(destination.__str__())
                    self.pieces_from_black_piece.append(destination)
                    print("Las piezas que Blanco capturo son: ")
                    return self.pieces_from_black
                else:
                    # Código para piezas negras capturando piezas blancas
                    pass