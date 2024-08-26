import unittest
from game.chess import Chess
from unittest.mock import patch, call, Mock

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

    @patch('builtins.print')
    def test_move_piece(self, patched_print):
        self.chess.move(7, 0, 6, 0)
        
        self.assertEqual(self.chess.__board__.get_piece(7, 0), "No piece")

        self.assertEqual(self.chess.__turn__, "WHITE")

    @patch('builtins.print')
    def test_move_no_piece(self, patched_print):

        self.chess.__board__.get_piece(7, 0)

        self.assertEqual(self.chess.move(5,7,2,2), "You can't move a piece that doesn't exist")

    @patch('builtins.print')
    def test_move_correct_color_white_turn(self, patched_print):

        result = self.chess.move_correct_color(7, 0) 
        self.assertIsNone(result, "Debería permitir mover la pieza blanca en el turno de blancas")


        result = self.chess.move_correct_color(0, 0)
        self.assertEqual(result, "You can't move a piece that is not your color")


if __name__ == '__main__':
    unittest.main()