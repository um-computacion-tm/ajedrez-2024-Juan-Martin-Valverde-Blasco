import unittest
from game.board import Board
from game.rook import Rook


class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rook = Rook("WHITE")  

    def test_valid_orthogonal_moves(self):
        board = None 
    def test_invalid_moves(self):
        board = None  
        self.assertFalse(self.rook.permited_move(0, 0, 5, 5, board))
        self.assertFalse(self.rook.permited_move(0, 0, 1, 2, board)) 
        
        
#COMPLETE