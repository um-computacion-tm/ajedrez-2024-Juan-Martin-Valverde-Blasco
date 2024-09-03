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
    
    
    # Esta funcion establece el como se va a mover cada pieza alta fiaca explicarlo uno por uno
    def permited_move(self, from_row, from_col, to_row, to_col): #me va a romper las pelotas con la complejidad? que me conviene mas en board o en pieces
        piece = self.__positions__[from_row][from_col]

        if piece.__type__ == 'PAWN':
            direction = -1 if piece.__color__ == "white" else 1
            if to_col == from_col: 
                if (to_row - from_row) == direction and self.get_piece(to_row, to_col) == "No piece":
                    return True
                if (from_row == 6 and piece.__color__ == "white") or (from_row == 1 and piece.__color__ == "black"):
                    if (to_row - from_row) == 2 * direction and self.get_piece(to_row, to_col) == "No piece":
                        return True
            if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
                destination_piece = self.get_piece(to_row, to_col)
                if destination_piece != "No piece" and destination_piece.__color__ != piece.__color__:
                    return True
            else:
                return False
            

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
        
        
    # Esta funcion lo que hace es mover las piezas        
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


    # Esta funcion lo que hace es mostrar el tablero
    def show_board(self):

        top_border = "╔══╤══╤══╤══╤══╤══╤══╤══╗"
        middle_border = "╟──┼──┼──┼──┼──┼──┼──┼──╢"
        bottom_border = "╚══╧══╧══╧══╧══╧══╧══╧══╝"
        
        print(top_border)
        
        for row in range(8):
            
            print("║", end="")
            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    
                    if (row + col) % 2 == 0:
                        print("  │", end="")
                    else:
                        print("░░│", end="")
                else:
                    print(f"{piece.__str__()}│", end="")

            print(f"║{8 - row}")  

            if row < 7:
                print(middle_border)  

        print(bottom_border)  

        
        print("╰a─┈b─┈c─┈d─┈e─┈f─┈g─┈h─┈╯")
    
    # Esta funcion lo que hace es verificar si el movimiento de la torre es valido
    def is_valid_rook_move(board, from_row, from_col, to_row, to_col):
        
        if from_row != to_row and from_col != to_col:
            return False
        
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board[from_row][col] is not None:
                    return False
        
        elif from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board[row][from_col] is not None:
                    return False

        return True
