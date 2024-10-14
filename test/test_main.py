import unittest
from unittest.mock import patch
from game.king import King
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.chess import Chess
from game.main import Cli


class TestMain(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()
        self.chess = Chess()

        
    @patch('builtins.print')
    @patch ('builtins.input', side_effect = ["e"])
    def test_play_error(self,patched_print, mock_input):
        self.cli.play()

        self.assertEqual(self.cli.play(), "error")


    @patch('builtins.print')
    def test_verify_color(self, patched_print):

        result = self.chess.right_color(7, 0)
        self.assertIsNone(result)

        self.assertEqual(self.cli.verify_color(self.chess, 7, 0), True)

    @patch('builtins.print')
    def test_verify_color_no_piece(self, patched_print):

        self.chess.right_color(5, 5)

        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)
        
    @patch('builtins.print')
    def test_verify_color_no_piece(self, patched_print):

        self.chess.right_color(5, 5)

        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)
        

    def test_verify_end_game_called(self):

        self.chess.__board__.__positions__[5][5] = Queen("BLACK") 
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None 
            self.chess.__board__.__positions__[0][col] = None 
        print(self.chess.__board__.get_piece(5, 5))
        self.cli.play()

    @patch('builtins.print')
    @patch ('builtins.input', side_effect = [6,6,4,6])
    def test_verify_end_game_called(self, patched_print, mock_input):
        self.chess.__board__.__positions__[5][5] = Queen("BLACK")
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None  
            self.chess.__board__.__positions__[0][col] = None  

        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Rook("BLACK"), Knight("BLACK"), Knight("BLACK"), 
                                                        Bishop("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")]


        # Asegurarse de que `self.cli` use el mismo tablero que acabamos de modificar
        self.cli.chess = self.chess

        self.assertEqual(self.chess.__board__.piece_to_STR(5, 5), ({'QUEEN'}, {'BLACK'}))

        self.assertIsInstance(self.chess.__board__.get_piece(5, 5), Queen)

        self.assertIsNone(self.cli.play())

#    @patch('builtins.print')
#    @patch('builtins.input', side_effect = [6, 6, 4, 6, "y"])
#    def test_answer_yes(self, patched_print, mock_input):
#        self.cli.play()
#
#        self.assertEqual(self.cli.chess.__turn__, "BLACK")
