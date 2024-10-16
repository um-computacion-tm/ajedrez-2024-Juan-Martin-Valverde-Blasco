import unittest
from game.pawn import Pawn
from game.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board()
    
    def test_permited_move_pawn(self):
        self.assertEqual(self.board.permited_move(1, 0, 3, 0), True)
        self.assertEqual(self.board.permited_move(1, 0, 2, 0), True)
        self.assertEqual(self.board.permited_move(1, 0, 5, 0), False)
        self.assertEqual(self.board.permited_move(6, 0, 5, 0), True)
        self.assertEqual(self.board.permited_move(6, 0, 4, 0), True)

        self.board.__positions__[4][1] = Pawn("WHITE")
        self.board.__positions__[3][2] = Pawn("BLACK")

        self.assertEqual(self.board.permited_move(4, 1, 3, 2), True)

