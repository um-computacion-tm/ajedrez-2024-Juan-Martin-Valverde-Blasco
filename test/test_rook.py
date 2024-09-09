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

#class TestRook(unittest.TestCase):
#    
#    def test_permited_move_rook(self):
#
#        self.assertEqual(self.board.permited_move(0, 0, 3, 2), False)
