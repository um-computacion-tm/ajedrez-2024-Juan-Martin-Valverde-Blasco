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
from game.exceptions import NotPieceToMove, NotPermitedMove

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")

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

class TestBoardMovePiece(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.__positions__[0][0] = Rook("WHITE")
        self.board.__positions__[1][0] = Pawn("BLACK")

    @patch('builtins.print')
    def test_move_piece_valid(self, mock_print):
        # Mockear permited_move para permitir el movimiento
        with patch.object(Board, 'permited_move', return_value=True):
            self.board.move_piece(0, 0, 0, 1)
            self.assertIsInstance(self.board.__positions__[0][1], Rook)
            self.assertIsNone(self.board.__positions__[0][0])
            mock_print.assert_called_with("Moved piece from: 0, 0 to: 0, 1")

    def test_move_piece_no_piece(self):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(NotPieceToMove):
            self.board.move_piece(2, 2, 3, 3)

    @patch('builtins.print')
    def test_move_piece_same_color(self, mock_print):
        # Intentar mover una pieza a una posición ocupada por una pieza del mismo color
        self.board.__positions__[0][1] = Pawn("WHITE")
        with self.assertRaises(NotPermitedMove):
            self.board.move_piece(0, 0, 0, 1)

    @patch('builtins.print')
    def test_move_piece_invalid_move(self, mock_print):
        # Intentar mover una pieza a una posición inválida
        Rook.permited_move = MagicMock(return_value=False)
        with self.assertRaises(NotPermitedMove):
            self.board.move_piece(0, 0, 3, 3)

