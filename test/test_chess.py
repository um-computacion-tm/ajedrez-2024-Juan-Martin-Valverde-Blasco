import unittest
from unittest.mock import patch
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.king import King
from game.queen import Queen
from game.chess import Chess
from game.piece import Piece
from game.exceptions import InvalidPosition, NotPieceToReplace

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()


    def test_init(self):
        self.assertEqual(self.chess.__turn__, "WHITE")


    def test_toggle_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")


    @patch('builtins.print')
    def test_move_piece_valid_move(self, patched_print):
        self.assertEqual(self.chess.__board__.piece_to_STR(7, 0), ({'ROOK'}, {'WHITE'}))
        self.chess.movement_fits(7, 0, 5, 0)
        self.assertEqual(self.chess.__board__.get_piece(7, 0), "No piece")
        self.assertEqual(self.chess.__turn__, "WHITE")


    @patch('builtins.print')
    def test_white_piece_color_check(self, patched_print):
        result = self.chess.right_color(7, 0)
        self.assertIsNone(result)
        result = self.chess.right_color(0, 0)
        self.assertEqual(result, "No podes mover una pieza que no es de tu color")


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["0"])
    def test_black_piece_promotion(self, patched_print, mock_input):
        self.chess.__board__.pieces_from_black = ["♕"]
        self.chess.__board__.pieces_from_black_piece = [Queen("BLACK")]
        self.chess.__board__.__positions__[7][0] = Pawn("BLACK")
        function = self.chess.define_new_piece(6, 0, 7, 0, self.chess.__board__.pieces_from_black_piece)
        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["0"])
    def test_white_piece_promotion(self, patched_print, mock_input):
        self.chess.__board__.pieces_from_white = ["♛"]
        self.chess.__board__.pieces_from_white_piece = [Queen("WHITE")]
        self.chess.__board__.__positions__[7][0] = Pawn("WHITE")
        function = self.chess.define_new_piece(6, 0, 7, 0, self.chess.__board__.pieces_from_white_piece)
        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1"])
    def test_piece_replacement(self, patched_print, mock_input):
        self.chess.__board__.__positions__[0][7] = None
        self.chess.__board__.__positions__[1][7] = Pawn("WHITE")
        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Queen("BLACK")]
        self.chess.__board__.pieces_from_black = ["♖", "♕"]
        self.chess.__board__.pieces_from_white_piece = [Rook("WHITE"), Queen("WHITE")]
        self.chess.__board__.pieces_from_white = ["♜", "♛"]
        self.chess.movement_fits(1, 7, 0, 7)
        self.assertEqual(self.chess.__board__.piece_to_STR(0, 7), ({'PAWN'}, {'WHITE'}))
        self.assertIsInstance(self.chess.__board__.get_piece(0, 7), Pawn)
        self.chess.change_pawn(1, 7, 0, 7)
        self.assertEqual(self.chess.__board__.piece_to_STR(0, 7), ({'QUEEN'}, {'WHITE'}))


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1"])
    def test_replace_black_pawn_with_queen(self, patched_print, mock_input):
        self.chess.__board__.__positions__[0][7] = None
        self.chess.__board__.__positions__[1][7] = Pawn("WHITE")
        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Queen("BLACK")]
        self.chess.__board__.pieces_from_black = ["♖", "♕"]
        self.chess.__board__.pieces_from_white_piece = [Rook("WHITE"), Queen("WHITE")]
        self.chess.__board__.pieces_from_white = ["♜", "♛"]
        self.chess.movement_fits(1, 7, 0, 7)
        self.assertEqual(self.chess.__board__.piece_to_STR(0, 7), ({'PAWN'}, {'WHITE'}))
        self.assertIsInstance(self.chess.__board__.get_piece(0, 7), Pawn)
        self.chess.change_pawn(1, 7, 0, 7)
        self.assertEqual(self.chess.__board__.piece_to_STR(0, 7), ({'QUEEN'}, {'WHITE'}))


    def test_white_victory_by_capturing_black_king(self):
        self.chess.__board__.pieces_from_black_piece = [King("BLACK")]
        self.assertEqual(self.chess.verify_winner(), "Equipo WHITE gana")


    def test_black_victory_by_capturing_white_king(self):
        self.chess.__board__.pieces_from_white_piece = [King("WHITE")]
        self.assertEqual(self.chess.verify_winner(), "Equipo BLACK gana")


    def test_display_captured_black_pieces_in_white_turn(self):
        self.chess.__turn__ = "WHITE"
        self.chess.__board__.pieces_from_black = [Rook("BLACK"), Knight("BLACK")]
        expected_output = ("Las piezas capturadas del BLACK son: ", self.chess.__board__.pieces_from_black)
        self.assertEqual(self.chess.STR_captured_pieces(), expected_output)


    def test_display_captured_white_pieces_in_black_turn(self):
        self.chess.__turn__ = "BLACK"
        self.chess.__board__.pieces_from_white = [Bishop("WHITE"), Queen("WHITE")]
        expected_output = ("Las piezas capturadas del WHITE son: ", self.chess.__board__.pieces_from_white)
        self.assertEqual(self.chess.STR_captured_pieces(), expected_output)


    def test_display_no_black_pieces_captured_in_white_turn(self):
        self.chess.__turn__ = "WHITE"
        self.chess.__board__.pieces_from_black = []
        expected_output = "El equipo esta completo"
        self.assertEqual(self.chess.STR_captured_pieces(), expected_output)


    def test_display_no_white_pieces_captured_in_black_turn(self):
        self.chess.__turn__ = "BLACK"
        self.chess.__board__.pieces_from_white = []
        expected_output = "El equipo esta completo"
        self.assertEqual(self.chess.STR_captured_pieces(), expected_output)


    def test_valid_position_no_error(self):
        try:
            self.chess.error_out_of_range(3, 4)
        except InvalidPosition:
            self.fail("error_out_of_range() raised InvalidPosition unexpectedly!")


    def test_invalid_row_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(8, 4)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_invalid_column_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(3, 8)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_invalid_row_and_column_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(8, 8)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_negative_row_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(-1, 4)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_negative_column_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(3, -1)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_negative_row_and_column_error(self):
        with self.assertRaises(InvalidPosition) as context:
            self.chess.error_out_of_range(-1, -1)
        self.assertEqual(str(context.exception), "Posicion invalida, tiene que estar entre los valores 0 a 7.")


    def test_check_right_color_no_piece(self):
        result = self.chess.right_color(2, 2)
        self.assertEqual(result, "La pieza no existe")


    def test_check_right_color_valid_piece(self):
        result = self.chess.right_color(0, 0)
        self.assertTrue(result)


    def test_check_right_color_invalid_piece(self):
        result = self.chess.right_color(1, 1)
        self.assertEqual(result, "No podes mover una pieza que no es de tu color")

    def test_verify_winner_returns_false(self):
        # Mockear el método king_captured para que devuelva False para ambos colores
        self.chess.king_captured = lambda color: False

        # Llamar a verify_winner y verificar que devuelve False
        result = self.chess.verify_winner()
        self.assertFalse(result)

        self.chess.__board__ = MockBoard()
        self.chess.__board__.get_piece = lambda row, col: MockPiece("PAWN", "WHITE") if row == 0 else MockPiece("PAWN", "BLACK")
        self.chess.__board__.pieces_from_white_piece = []
        self.chess.__board__.pieces_from_black_piece = []



class MockBoard:
    def get_piece(self, row, col):
        return None

class MockPiece:
    def __init__(self, piece_type, color):
        self.__type__ = piece_type
        self.__color__ = color


#COMPLETE