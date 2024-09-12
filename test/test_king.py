import unittest
from game.king import King
from game.board import Board
class TestKing(unittest.TestCase):

    def test_str_white_king(self):
        king = King("WHITE")
        self.assertEqual(str(king), " ♚")

    def test_str_black_king(self):
        king = King("BLACK")
        self.assertEqual(str(king), " ♔")

    def setUp(self):
        self.board = Board()    

    def test_permited_move_king(self):
        self.board.__positions__[4][4] = King("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 4, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 4, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 4), True)
        self.assertEqual(self.board.permited_move(4, 4, 5, 4), True)
        self.assertEqual(self.board.permited_move(4, 4, 5, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 5, 3), True)
               

        self.assertEqual(self.board.permited_move(4, 4, 2, 4), False)

