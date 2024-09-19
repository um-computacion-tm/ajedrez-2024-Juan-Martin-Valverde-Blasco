from game.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"

    def __str__(self):
        return " ♟" if self.__color__ == "WHITE" else " ♙"
        
    def can_do_double_step(self, from_row, to_row, direction):
        return (to_row - from_row) == 2 * direction

    def is_valid_starting_row(self, from_row):
        return (from_row == 6 and self.__color__ == "WHITE") or (from_row == 1 and self.__color__ == "BLACK")

    def empty_square(self, board, to_row, to_col):
        return board.get_piece(to_row, to_col) == "No piece"


    def is_enemy_piece(self, board, to_row, to_col):
        destination_piece = board.get_piece(to_row, to_col)
        return destination_piece != "No piece" and destination_piece[1] != self.__color__

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1
        
        # Movimiento ortogonal (avance)
        if self.permited_move_orthogonal(from_row, from_col, to_row, to_col, board):
            if (to_row - from_row) == direction and self.empty_square(board, to_row, to_col):
                return True
            if self.is_valid_starting_row(from_row) and self.can_do_double_step(from_row, to_row, direction) and self.empty_square(board, to_row, to_col):
                return True
        
        # Movimiento diagonal (captura)
        if self.permited_move_diagonal(from_row, from_col, to_row, to_col, board):
            if (to_row - from_row) == direction and self.is_enemy_piece(board, to_row, to_col):
                return True
        
        return False

        
