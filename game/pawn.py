from game.piece import Piece

class Pawn(Piece):
    __type__ = "PAWN"
    __white_str__ = "♟" 
    __black_str__ = "♙"


    #Doble salto cuando es su primer movimiento
    def first_movement(self, from_row, to_row, direction):
        return (to_row - from_row) == 2 * direction


    #habilita el ataque en caso de que un enemigo este cerca
    def enemy_piece_nerby(self, board, to_row, to_col):
        destination_piece = board.get_piece(to_row, to_col)
        return destination_piece != "No piece" and destination_piece.__color__ != self.__color__


    #verifica que el lugar este vacio
    def empty_place(self, board, to_row, to_col):
        return board.get_piece(to_row, to_col) == "No piece"


    #verifica que este bien puesta la pieza
    def init_position_valid(self, from_row):
        return (from_row == 6 and self.__color__ == "WHITE") or (from_row == 1 and self.__color__ == "BLACK")


    #Esta funcion lo que hace es el movimiento del peon utilizando la funciones que tenemos en piece y las que creamos aca
    def permited_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1
        
        if self.is_valid_orthogonal_move(from_row, from_col, to_row, to_col, board, direction):
            return True
        
        if self.is_valid_diagonal_move(from_row, from_col, to_row, to_col, board, direction):
            return True
        
        return False
    
    def is_valid_orthogonal_move(self, from_row, from_col, to_row, to_col, board, direction):
        if self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board):
            return self.is_valid_move(from_row, to_row, direction, board, to_col, self.empty_place)
        return False
    
    def is_valid_diagonal_move(self, from_row, from_col, to_row, to_col, board, direction):
        if self.permited_move_diagonal(from_row, from_col, to_row, to_col, board):
            return self.is_valid_move(from_row, to_row, direction, board, to_col, self.enemy_piece_nerby)
        return False
    
    def is_valid_move(self, from_row, to_row, direction, board, to_col, condition_func):
        if (to_row - from_row) == direction and condition_func(board, to_row, to_col):
            return True
        if self.init_position_valid(from_row) and self.first_movement(from_row, to_row, direction) and condition_func(board, to_row, to_col):
            return True
        return False