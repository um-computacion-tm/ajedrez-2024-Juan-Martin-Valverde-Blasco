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

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        
    def test_permited_move(self):

        self.assertEqual(self.board.permited_move(0, 1, 2, 2), True)
        self.assertEqual(self.board.permited_move(0, 1, 2, 0), True)

        self.board.__positions__[4][4] = Knight("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 2, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 2, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 5), False)      

#    def test_permited_move_line_77(self): 
#        self.board.__positions__[2][2] = Knight("BLACK")
#        self.assertEqual(self.board.__positions__[2][2].__type__, "KNIGHT")
#        
#        self.assertEqual(self.board.get_piece(2, 2), ({'KNIGHT'}, {'BLACK'}))
#        self.assertEqual(self.board.permited_move(2, 2, 4, 3), True)  
#   