import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from game.board import Board
from game.piece import Piece
from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn

class TestQueen(unittest.TestCase):

    def test_str_white_queen(self):
        queen = Queen("WHITE")
        self.assertEqual(str(queen), " ♛")

    def test_str_black_queen(self):
        queen = Queen("BLACK")
        self.assertEqual(str(queen), " ♕")

    def setUp(self):
        self.board = Board()
        
    def test_permited_move_queen(self):

        self.assertEqual(self.board.permited_move(0, 3, 3, 3), True)
        self.assertEqual(self.board.permited_move(0, 3, 2, 5), True)
        self.assertEqual(self.board.permited_move(0, 3, 2, 1), True)

        self.board.__positions__[4][4] = Queen("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 4, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 4, 4), True)

        self.assertEqual(self.board.permited_move(0, 3, 2, 4), False)
