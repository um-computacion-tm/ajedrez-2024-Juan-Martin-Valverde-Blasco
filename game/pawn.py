from game.piece import Piece

class Pawn(Piece):
    __type__ = "PAWN"
    __white_show__ = "♟" 
    __black_show__ = "♙"

    def is_double_step(self, from_row, to_row, direction):
        return (to_row - from_row) == 2 * direction

    def is_valid_starting_row(self, from_row):
        return (from_row == 6 and self.__color__ == "WHITE") or (from_row == 1 and self.__color__ == "BLACK")

    def is_empty_square(self, board, to_row, to_col):
        return board.get_piece(to_row, to_col) == "No piece"


    def is_enemy_piece(self, board, to_row, to_col):
        destination_piece = board.get_piece(to_row, to_col)
        return destination_piece != "No piece" and destination_piece.__color__ != self.__color__


    def permited_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1
        if to_col == from_col:  # Movimiento hacia adelante
            if (to_row - from_row) == direction and board.get_piece(to_row, to_col) == "No piece":
                return True
            
            if self.is_valid_starting_row(from_row) and self.is_double_step(from_row, to_row, direction) and self.is_empty_square(board, to_row, to_col):
                return True
                
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            if self.is_enemy_piece(board, to_row, to_col):
                return True        

        return False
