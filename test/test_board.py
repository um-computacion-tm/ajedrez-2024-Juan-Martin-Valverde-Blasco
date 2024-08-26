import unittest
from unittest.mock import patch

from game.board import Board
from game.piece import Piece, Rook, Pawn, Knight, Bishop, Queen, King


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")
        

    def test_get_piece_empty(self):
        self.assertEqual(self.board.get_piece(3, 3), "No piece")

    @patch('builtins.print')
    def test_move_piece(self, patched_print):
        self.board.move_piece(0, 0, 0, 1)
        

        self.assertEqual(self.board.get_piece(0, 1), ({'ROOK'}, {'BLACK'}))

        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    @patch('builtins.print')
    def test_move_piece_no_piece(self, patched_print):

        self.assertEqual(self.board.move_piece(3, 3, 4, 4), "No piece to move")

        self.assertEqual(self.board.get_piece(3, 3), "No piece")
        self.assertEqual(self.board.get_piece(4, 4), "No piece")

    def test_permited_move_knight(self):

        self.assertEqual(self.board.permited_move(0, 1, 2, 2), True)
        self.assertEqual(self.board.permited_move(0, 1, 2, 0), True)

        self.board.__positions__[4][4] = Knight("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 2, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 2, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 3), True)
        #self.assertEqual(self.board.permited_move(4, 4, 3, 6), True)
        #self.assertEqual(self.board.permited_move(4, 4, 3, 2), True)


        self.assertEqual(self.board.permited_move(4, 4, 3, 5), False)      

    def test_permited_move_line_77(self): 
        self.board.__positions__[2][2] = Knight("BLACK")
        self.assertEqual(self.board.__positions__[2][2].__type__, "KNIGHT")
        
        self.assertEqual(self.board.get_piece(2, 2), ({'KNIGHT'}, {'BLACK'}))
        self.assertEqual(self.board.permited_move(2, 2, 4, 3), True)

    def test_permited_move_queen(self):

        self.assertEqual(self.board.permited_move(0, 3, 3, 3), True)
        self.assertEqual(self.board.permited_move(0, 3, 2, 5), True)
        self.assertEqual(self.board.permited_move(0, 3, 2, 1), True)

        self.board.__positions__[4][4] = Queen("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 4, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 4, 4), True)

        self.assertEqual(self.board.permited_move(0, 3, 2, 4), False)

    def test_permited_move_rook(self):

        self.assertEqual(self.board.permited_move(0, 0, 3, 2), False)

    def test_permited_move_bishop(self):
        self.board.__positions__[3][3] = Bishop("BLACK")

        self.assertEqual(self.board.permited_move(3, 3, 4, 4), True)
        self.assertEqual(self.board.permited_move(3, 3, 2, 4), True)
        self.assertEqual(self.board.permited_move(3, 3, 2, 2), True)
        self.assertEqual(self.board.permited_move(3, 3, 4, 2), True)
        self.assertEqual(self.board.permited_move(3, 3, 5, 5), True)

        self.assertEqual(self.board.permited_move(3, 3, 6, 5), False)

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
