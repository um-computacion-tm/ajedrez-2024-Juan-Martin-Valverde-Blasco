from game.piece import Piece
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King

from game.exceptions import NotPermitedMove, NotPieceToMove

#Que hacer con los permited_move, donde los pongo?



class Board:
    def __init__(self): #Asi inicia el tablero
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        # ESte es el mejor lugar para poner la funcion de comer piezas??????????????????????????????????
        self.pieces_from_white = [] #Las piezas que se comio el NEGRO del BLANCO
        self.pieces_from_black = [] #Las piezas que se comio el BLANCO del NEGRO
        self.pieces_from_white_piece = [] #Las piezas que se comio el NEGRO del BLANCO
        self.pieces_from_black_piece = [] #Las piezas que se comio el BLANCO del NEGRO

        #lugares rook
        self.__positions__[0][0] = Rook("BLACK") #"Rook Black"
        self.__positions__[0][7] = Rook("BLACK") #"Rook Black"
        self.__positions__[7][7] = Rook("WHITE") #"Rook White"
        self.__positions__[7][0] = Rook("WHITE") #"Rook White"


        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK") #"PawnBlack"
            self.__positions__[6][col] = Pawn("WHITE") #"PawnWhite"

        #lugares knight
        self.__positions__[0][1] = Knight("BLACK") #"KnightBlack"
        self.__positions__[0][6] = Knight("BLACK") #"KnightBlack"
        self.__positions__[7][1] = Knight("WHITE") #"KnightWhite"
        self.__positions__[7][6] = Knight("WHITE") #"KnightWhite"

        #lugares bushop
        self.__positions__[0][2] = Bishop("BLACK") #"BishopBlack"
        self.__positions__[0][5] = Bishop("BLACK") #"BishopBlack"
        self.__positions__[7][2] = Bishop("WHITE") #"BishopWhite"
        self.__positions__[7][5] = Bishop("WHITE") #"BishopWhite"

        #lugares queen
        self.__positions__[0][3] = Queen("BLACK") #"QueenBlack"
        self.__positions__[7][3] = Queen("WHITE") #"QueenWhite"


        #lugares king
        self.__positions__[0][4] = King("BLACK") #"KingBlack"
        self.__positions__[7][4] = King("WHITE") #"KingWhite"
    

    def get_piece_for_show(self, row, col):
        piece = self.__positions__[row][col]
        
        if piece is None:
            return "No piece"
        else:
            return ({piece.__type__}, {piece.__color__})
        
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]

        if piece is None:
            return "No piece"
        else:
            return piece
    
    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]

        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False  # No hay pieza para mover
        return piece.permited_move(from_row, from_col, to_row, to_col, self)

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            #self.show_board()
            raise NotPieceToMove("No piece to move")

        destination = self.__positions__[to_row][to_col]

        # Verificamos si la posición de destino tieneom_row, from_col,to_row,to_col)) una pieza del mismo color
        if destination is not None and destination.__color__ == piece.__color__:
            #self.show_board()
            raise NotPermitedMove("Cannot move to a position occupied by a piece of the same color")

        if self.permited_move(from_row, from_col, to_row, to_col) == False:
            #self.show_board()
            raise NotPermitedMove("The piece cannot be moved in this position")

        self.__positions__[to_row][to_col] = piece

        self.__positions__[from_row][from_col] = None

        print(f"Moved piece from: ", {from_row}, {from_col}, "to: ", {to_row}, {to_col})

        #self.show_board()
    
    def eat_piece(self, from_row, from_col, to_row, to_col):

        piece = self.__positions__[from_row][from_col]
        destination = self.__positions__[to_row][to_col]
        if destination is not None:
            if destination.__color__ != piece.__color__:
                if piece.__color__ == "WHITE":
                    self.pieces_from_black.append(destination.show())
                    self.pieces_from_black_piece.append(destination)
                    print("Las piezas que BLANCO se comio de NEGRO son: ")
                    return (self.pieces_from_black)
                else:
                    self.pieces_from_white.append(destination.show())
                    self.pieces_from_white_piece.append(destination)
                    print("Las piezas que NEGRO se comio de BLANCO son: ")
                    return (self.pieces_from_white)
        else:
            return False



    def show_board(self):

        print("    ", end="")
        for col in range(8):
            print(f"    {col} ", end="")
        print() 

        for row in range(8):
            print(f" {row} |", end="")  

            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    print("    ", end=" |")  # Espacio en blanco si no hay pieza
                else:
                    print(" ", piece.show()," ",  end="|")  # Muestra inicial del tipo y color de la pieza
            print()
            print("    " + "------" * 8 + "")  # Línea separadora entre filas



board = Board()
# board.show_board()
# print(board.get_piece(0,0))
# print(board.get_piece(7,0))
 