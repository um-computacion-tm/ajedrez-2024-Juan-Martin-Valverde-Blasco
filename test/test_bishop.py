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

#class TestBishop(unittest.TestCase):
#
#    def setUp(self):
#        self.bishop = Bishop("BLACK")
#
#    def test_permited_move_bishop(self):
#        self.assertEqual(self.bishop.permited_move(3, 3, 4, 4), True)
#        self.assertEqual(self.bishop.permited_move(3, 3, 2, 4), True)
#        self.assertEqual(self.bishop.permited_move(3, 3, 2, 2), True)
#        self.assertEqual(self.bishop.permited_move(3, 3, 4, 2), True)
#        self.assertEqual(self.bishop.permited_move(3, 3, 5, 5), True)
#
#        self.assertEqual(self.bishop.permited_move(3, 3, 6, 5), False)
