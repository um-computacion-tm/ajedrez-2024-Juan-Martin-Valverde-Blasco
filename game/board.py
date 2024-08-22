from game.piece import Rook, Pawn, Knight, Bishop, Queen, King

#esta funcion inicia el tablero y establece las posiciones de las piezas
class Board:
    def __init__(self): 
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #lugar de los alfiles
        self.__positions__[0][0] = Rook("BLACK") #alfil negro
        self.__positions__[0][7] = Rook("BLACK") #alfil negro
        self.__positions__[7][7] = Rook("WHITE") #alfil balnco
        self.__positions__[7][0] = Rook("WHITE") #alfil blanco

        #lugares peon
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

        
        self.__positions__[0][1] = Knight("BLACK") 
        self.__positions__[0][6] = Knight("BLACK") 
        self.__positions__[7][1] = Knight("WHITE") 
        self.__positions__[7][6] = Knight("WHITE") 

        
        self.__positions__[0][2] = Bishop("BLACK") 
        self.__positions__[0][5] = Bishop("BLACK") 
        self.__positions__[7][2] = Bishop("WHITE") 
        self.__positions__[7][5] = Bishop("WHITE") 

    
        self.__positions__[0][3] = Queen("BLACK") 
        self.__positions__[7][3] = Queen("WHITE") 


        
        self.__positions__[0][4] = King("BLACK") 
        self.__positions__[7][4] = King("WHITE") 
    
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]
        if piece is None:
            return "No piece"
        return ({piece.__type__}, {piece.__color__})
    
    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]


        if piece.__type__ == "ROOK":
            if to_row == from_row and to_col != from_col:
                return True
            elif to_col == from_col and to_row != from_row:
                return True
            else:
                return False
        if piece.__type__ == "KNIGHT":

            valid_moves = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
            if (from_row - to_row, from_col - to_col) in valid_moves:
                return True
            else:
                return False

        
        if piece.__type__ == "BISHOP":
            if abs(to_row - from_row) == abs(to_col - from_col):
                return True
            else:
                return False
        
        
        if piece.__type__ == "QUEEN":

        
            n = []
            if to_row == from_row and to_col != from_col:
                return True
            elif to_col == from_col and to_row != from_row:
                return True
            elif abs(to_row - from_row) == abs(to_col - from_col):
                return True
            else:
                return False

        
        if piece.__type__ == "KING":

            if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1 and not (from_row == to_row and from_col == to_col):
                return True
            else: 
                return False
        
    def move_piece(self, from_row, from_col, to_row, to_col):
        
        piece = self.__positions__[from_row][from_col]

        if piece is None:
            print("No piece to move")
            return "No piece to move"
        elif self.permited_move(from_row, from_col, to_row, to_col) == False:
            print("The piece cannot be moved in this position")
            return "The piece cannot be moved in this position"

        self.__positions__[to_row][to_col] = piece

        self.__positions__[from_row][from_col] = None

        print(f"Moved piece from: ", {from_row}, {from_col}, "to: ", {to_row}, {to_col})

        self.show_board()

    
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
                    print("    ", end=" |")  
                else:
                    print(f" {piece.__type__[0]}{piece.__color__[0]} ", end=" |")  
            print()
            print("    " + "------" * 8 + "")  

# board = Board()
# board.show_board()
# print(board.get_piece(0,0))
# print(board.get_piece(7,0))
#   def inicializar_tablero(self):
#       return [
#            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
#            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
#            [" ", " ", " ", " ", " ", " ", " ", " "],
#            [" ", " ", " ", " ", " ", " ", " ", " "],
#            [" ", " ", " ", " ", " ", " ", " ", " "],
#            [" ", " ", " ", " ", " ", " ", " ", " "],
#            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
#            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
#        ]
#print[
#╔═╤═╤═╤═╤═╤═╤═╤═╗╮
#║♜│♞│♝│♛│♚│♝│♞│♜║8
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║♟│♟│♟│♟│♟│♟│♟│♟║7
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║ │░│ │░│ │░│ │░║6
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║░│ │░│ │░│ │░│ ║5
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║ │░│ │░│ │░│ │░║4
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║░│ │░│ │░│ │░│ ║3
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║♙│♙│♙│♙│♙│♙│♙│♙║2
#╟─┼─┼─┼─┼─┼─┼─┼─╢┊
#║♖│♘│♗│♕│♔│♗│♘│♖║1
#╚═╧═╧═╧═╧═╧═╧═╧═╝┊
#╰a┈b┈c┈d┈e┈f┈g┈h┈╯

