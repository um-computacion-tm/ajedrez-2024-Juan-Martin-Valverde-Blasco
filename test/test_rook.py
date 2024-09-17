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

class TestRook(unittest.TestCase):

    def test_str_white_rook(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), " ♜")

    def test_str_black_rook(self):
        rook = Rook("BLACK")
        self.assertEqual(str(rook), " ♖")

    def setUp(self):
        self.board = Board()

    def test_permited_move_rook(self):

        self.assertEqual(self.board.permited_move(0, 0, 3, 2), False)
        self.board.__positions__[4][4] = Rook("BLACK")
        self.assertEqual(self.board.permited_move(4, 4, 4, 2), True)
        self.assertEqual(self.board.permited_move(4, 4, 2, 4), True)

