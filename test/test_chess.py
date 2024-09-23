import unittest
from game.chess import Chess
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace
from game.rook import Rook
from unittest.mock import patch
from game.rook import Rook
from game.pawn import Pawn
from game.queen import Queen



class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()


    def test_chess_init(self):
        self.assertEqual(self.chess.__turn__, "WHITE")


    def test_turn_change(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")

#    @patch('builtins.print')
#    def test_move_piece(self, patched_print):
#
#        self.assertEqual(self.chess.__board__.get_piece(7, 0), ({'ROOK'}, {'WHITE'}))
#
#        self.chess.move(7, 0, 5, 0)
#
#        self.assertEqual(self.chess.__board__.get_piece(7, 0), "No piece")
#
#        self.assertEqual(self.chess.__turn__, "WHITE")
       
        
    @patch('builtins.print')
    def test_move_correct_color_white_turn(self, patched_print):

        result = self.chess.move_correct_color(7, 0)
        self.assertIsNone(result)


        result = self.chess.move_correct_color(0, 0)
        self.assertEqual(result, "You can't move a piece that is not your color")


#    @patch('builtins.print')
#    @patch('builtins.input', side_effect = ["0"])
#    def test_define_new_piece_black(self, patched_print, mock_input):
#        self.chess.__board__.pieces_from_black = ["♕"]
#        self.chess.__board__.pieces_from_black_piece = [("BLACK")]
#
#        self.chess.__board__.__positions__[7][0] = Pawn("BLACK")
#
#        function = self.chess.define_new_piece_black(6, 0, 7, 0)
#
#
#        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
#        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["0"])
    def test_define_new_piece_white(self, patched_print, mock_input):
        self.chess.__board__.pieces_from_white = ["♛"]
        self.chess.__board__.pieces_from_white_piece = [Queen("WHITE")]

        self.chess.__board__.__positions__[7][0] = Pawn("WHITE")

        function = self.chess.define_new_piece_white(6, 0, 7, 0)


        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["1"])
    def test_replace_piece(self, patched_print, mock_input):
        self.chess.__board__.__positions__[0][7] = None

        self.chess.__board__.__positions__[1][7] = Pawn("WHITE")

        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Queen("BLACK")]
        self.chess.__board__.pieces_from_black = ["♖", "♕"]

        self.chess.__board__.pieces_from_white_piece = [Rook("WHITE"), Queen("WHITE")]
        self.chess.__board__.pieces_from_white = ["♜", "♛"]

        self.chess.move(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece(0, 7), ({'PAWN'}, {'WHITE'}))

        self.chess.change_pawn_for_other(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece(0, 7), ({'QUEEN'}, {'WHITE'}))
        

    @patch('builtins.input', return_value='0')
    def test_change_pawn_for_other_white(self, mock_input):
        self.chess.__board__.pieces_from_black_piece.append("ROOK")
        self.chess.change_pawn_for_other(0, 0, 0, 0)
        # Aquí deberías verificar que la pieza se ha cambiado correctamente

#    def test_change_pawn_for_other_white_no_pieces(self):
#        with self.assertRaises(NotPieceToReplace):
#            self.chess.change_pawn_for_other(0, 0, 0, 0)
#
    @patch('builtins.input', return_value='0')
    def test_change_pawn_for_other_black(self, mock_input):
        self.chess.__board__.pieces_from_white_piece.append("ROOK")
        self.chess.change_pawn_for_other(7, 0, 7, 0)
        # Aquí deberías verificar que la pieza se ha cambiado correctamente
#
 #   def test_change_pawn_for_other_black_no_pieces(self):
 #       with self.assertRaises(NotPieceToReplace):
 #           self.chess.change_pawn_for_other(7, 0, 7, 0)
