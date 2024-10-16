from game.piece import Piece

class Pawn(Piece):
    __type__ = "PAWN"
    __white_str__ = "♟" 
    __black_str__ = "♙"


    #habilita el ataque en caso de que un enemigo este cerca
    def init_position_valid(self, from_row):
        return (from_row == 6 and self.__color__ == "WHITE") or (from_row == 1 and self.__color__ == "BLACK")


    #Doble salto cuando es su primer movimiento
    def first_move(self, from_row, to_row, direction):
        return (to_row - from_row) == 2 * direction


    #verifica que el lugar este vacio
    def empty_space(self, board, to_row, to_col):
        return board.get_piece(to_row, to_col) == "No piece"


    #verifica que este bien puesta la pieza
    def enemy_piece_nerby(self, board, to_row, to_col):
        destination_piece = board.get_piece(to_row, to_col)
        return destination_piece != "No piece" and destination_piece.__color__ != self.__color__


    #Esta funcion lo que hace es el movimiento del peon utilizando la funciones que tenemos en piece y las que creamos aca
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1
        if to_col == from_col:
            if (to_row - from_row) == direction and board.get_piece(to_row, to_col) == "No piece":
                return True
            if self.init_position_valid(from_row) and self.first_move(from_row, to_row, direction) and self.empty_space(board, to_row, to_col):
                return True                
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            if self.enemy_piece_nerby(board, to_row, to_col):
                return True        

        return False

