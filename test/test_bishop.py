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

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.bishop = Bishop("WHITE")
        self.board.__positions__[3][3] = self.bishop

    def test_str_white_bishop(self):
        bishop = Bishop("WHITE")
        self.assertEqual(str(bishop), " ♝")

    def test_str_black_bishop(self):
        bishop = Bishop("BLACK")
        self.assertEqual(str(bishop), " ♗")

    def test_permited_move_valid(self):
        # Movimientos válidos para el alfil
        self.assertTrue(self.bishop.permited_move(self.board, 3, 3, 5, 5))
        self.assertTrue(self.bishop.permited_move(self.board, 3, 3, 1, 1))
        self.assertTrue(self.bishop.permited_move(self.board, 3, 3, 5, 1))
        self.assertTrue(self.bishop.permited_move(self.board, 3, 3, 1, 5))

    def test_permited_move_invalid(self):
        # Movimientos inválidos para el alfil
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 4, 5))
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 2, 4))
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 3, 5))
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 5, 3))

    def test_permited_move_blocked(self):
        # Movimientos bloqueados por otras piezas
        self.board.__positions__[4][4] = Bishop("BLACK")
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 5, 5))
        self.board.__positions__[4][4] = None
        self.board.__positions__[2][2] = Bishop("BLACK")
        self.assertFalse(self.bishop.permited_move(self.board, 3, 3, 1, 1))
