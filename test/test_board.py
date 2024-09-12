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


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")

#    @patch('builtins.print')
#    def test_move_piece(self, patched_print):
#        self.board.move_piece(0, 0, 0, 1)
#        self.assertEqual(self.board.get_piece(0, 1), ({'ROOK'}, {'BLACK'}))
#        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    @patch('builtins.print')
    def test_move_piece_no_piece(self, patched_print):

        self.assertEqual(self.board.move_piece(3, 3, 4, 4), "No piece to move")

        self.assertEqual(self.board.get_piece(3, 3), "No piece")
        self.assertEqual(self.board.get_piece(4, 4), "No piece")

#
#    def test_get_piece_empty(self):
#        self.assertEqual(self.board.get_piece(3, 3), "No piece")
#
#    @patch('builtins.print')
#    def test_move_piece(self, patched_print):
#        self.board.move_piece(0, 0, 0, 1)
#        
#
#        self.assertEqual(self.board.get_piece(0, 1), ({'ROOK'}, {'BLACK'}))
#
#        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    @patch('builtins.print')
    def test_move_piece_no_piece(self, patched_print):

        self.assertEqual(self.board.move_piece(3, 3, 4, 4), "No piece to move")

        self.assertEqual(self.board.get_piece(3, 3), "No piece")
        self.assertEqual(self.board.get_piece(4, 4), "No piece")
        
#    def test_move_piece_valid(self):
#        self.board.__positions__[0][0] = Rook("WHITE")
#        result = self.board.move_piece(0, 0, 0, 1)
#        self.assertIsNone(result)
#        self.assertIsNone(self.board.__positions__[0][0])
#        self.assertIsInstance(self.board.__positions__[0][1], Rook)
#
    def test_move_piece_no_piece(self):
        result = self.board.move_piece(3, 3, 4, 4)
        self.assertEqual(result, "No piece to move")

#    def test_move_piece_invalid_move(self):
#        self.board.__positions__[0][0] = Rook("WHITE")
#        result = self.board.move_piece(0, 0, 1, 1)  # Movimiento inválido para una torre
#        self.assertEqual(result, "The piece cannot be moved in this position")
#
    @patch('builtins.print')
    def test_move_piece_no_piece(self, mock_print):
        board = Board()
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        result = board.move_piece(0, 0, 1, 0)
        
        self.assertEqual(result, "No piece to move")
        mock_print.assert_called_with("No piece to move")

#    @patch('builtins.print')
#    def test_move_piece_invalid_move(self, mock_print):
#        board = Board()
#        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
#        board.__positions__[0][0] = Rook("white")
#        
#        Rook.permited_move = MagicMock(return_value=False)
#        
#        result = board.move_piece(0, 0, 1, 0)
#        
#        self.assertEqual(result, "The piece cannot be moved in this position")
#        mock_print.assert_called_with("The piece cannot be moved in this position")
#
#    @patch('builtins.print')
#    def test_move_piece_success(self, mock_print):
#        board = Board()
#        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
#        board.__positions__[0][0] = Rook("white")
#        
#        self.permited_move = MagicMock(return_value=True)
#        board.show_board = MagicMock()
#        
#        result = board.move_piece(0, 0, 1, 0)
#        
#        self.assertIsNone(result)
#        self.assertIsNone(board.__positions__[0][0])
#        self.assertIsInstance(board.__positions__[1][0], Rook)
#        mock_print.assert_any_call(f"Moved piece from: ", {0}, {0}, "to: ", {1}, {0})
#        board.show_board.assert_called_once()

#   @patch('sys.stdout', new_callable=StringIO)
#   def test_show_board(self, mock_stdout):
#       board = Board()
#       board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
#       
#       # Colocar algunas piezas en el tablero para la prueba
#       board.__positions__[0][0] = Rook("black")
#       board.__positions__[0][1] = Knight("black")
#       board.__positions__[0][2] = Bishop("black")
#       board.__positions__[0][3] = Queen("black")
#       board.__positions__[0][4] = King("black")
#       board.__positions__[0][5] = Bishop("black")
#       board.__positions__[0][6] = Knight("black")
#       board.__positions__[0][7] = Rook("black")
#       for i in range(8):
#           board.__positions__[1][i] = Pawn("black")
#           board.__positions__[6][i] = Pawn("white")
#       board.__positions__[7][0] = Rook("white")
#       board.__positions__[7][1] = Knight("white")
#       board.__positions__[7][2] = Bishop("white")
#       board.__positions__[7][3] = Queen("white")
#       board.__positions__[7][4] = King("white")
#       board.__positions__[7][5] = Bishop("white")
#       board.__positions__[7][6] = Knight("white")
#       board.__positions__[7][7] = Rook("white")
##       board.show_board()
##       expected_output = (
#           "╔══╤══╤══╤══╤══╤══╤══╤══╗\n"
#           "║ ♜│ ♞│ ♝│ ♛│ ♚│ ♝│ ♞│ ♜║8\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║ ♟│ ♟│ ♟│ ♟│ ♟│ ♟│ ♟│ ♟║7\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║  │░░│  │░░│  │░░│  │░░║6\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║░░│  │░░│  │░░│  │░░│  ║5\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║  │░░│  │░░│  │░░│  │░░║4\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║░░│  │░░│  │░░│  │░░│  ║3\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║ ♙│ ♙│ ♙│ ♙│ ♙│ ♙│ ♙│ ♙║2\n"
#           "╟──┼──┼──┼──┼──┼──┼──┼──╢\n"
#           "║ ♖│ ♘│ ♗│ ♕│ ♔│ ♗│ ♘│ ♖║1\n"
#           "╚══╧══╧══╧══╧══╧══╧══╧══╝\n"
#           "╰a─┈b─┈c─┈d─┈e─┈f─┈g─┈h─┈╯\n"
#       )
##       self.assertEqual(mock_stdout.getvalue(), expected_output)#