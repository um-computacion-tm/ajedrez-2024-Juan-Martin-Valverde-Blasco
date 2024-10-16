import unittest
from unittest.mock import patch
from io import StringIO
from game.piece import Piece
from game.rook import Rook
from game.pawn import Pawn
from game.board import Board, NotPieceToMove, NotPermitedMove
from game.exceptions import NotPieceToMove, NotPermitedMove

class TestBoard(unittest.TestCase):
   
   
    def setUp(self):
        self.board = Board()


    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")


    @patch('sys.stdout', new_callable=StringIO)
    def test_display_board_with_initial_setup(self, mock_stdout):
        self.board.show_board()
        expected_output = (
            "        0     1     2     3     4     5     6     7 \n"
            " 0 ║  ♖  ║  ♘  ║  ♗  ║  ♕  ║  ♔  ║  ♗  ║  ♘  ║  ♖  ║\n"
            "    ════════════════════════════════════════════════\n"
            " 1 ║  ♙  ║  ♙  ║  ♙  ║  ♙  ║  ♙  ║  ♙  ║  ♙  ║  ♙  ║\n"
            "    ════════════════════════════════════════════════\n"
            " 2 ║     ║     ║     ║     ║     ║     ║     ║     ║\n"
            "    ════════════════════════════════════════════════\n"
            " 3 ║     ║     ║     ║     ║     ║     ║     ║     ║\n"
            "    ════════════════════════════════════════════════\n"
            " 4 ║     ║     ║     ║     ║     ║     ║     ║     ║\n"
            "    ════════════════════════════════════════════════\n"
            " 5 ║     ║     ║     ║     ║     ║     ║     ║     ║\n"
            "    ════════════════════════════════════════════════\n"
            " 6 ║  ♟  ║  ♟  ║  ♟  ║  ♟  ║  ♟  ║  ♟  ║  ♟  ║  ♟  ║\n"
            "    ════════════════════════════════════════════════\n"
            " 7 ║  ♜  ║  ♞  ║  ♝  ║  ♛  ║  ♚  ║  ♝  ║  ♞  ║  ♜  ║\n"
            "    ════════════════════════════════════════════════\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_move_blocked_by_own_piece(self):
        self.board.__positions__[0][0] = Piece("WHITE")
        self.board.__positions__[1][1] = Piece("WHITE")
        with self.assertRaises(NotPermitedMove) as context:
            self.board.move_piece(0, 0, 1, 1)
        self.assertEqual(str(context.exception), "No se puede mover a esta posicion, esta ocupada por otra pieza del mismo equipo")


    def test_invalid_move_attempt(self):
        self.board.__positions__[0][0] = Piece("WHITE")
        self.board.permited_move = lambda from_row, from_col, to_row, to_col: False
        with self.assertRaises(NotPermitedMove) as context:
            self.board.move_piece(0, 0, 1, 1)
        self.assertEqual(str(context.exception), "No se puede mover a esta posicion")


    def test_initial_position_rook(self):
        self.assertIsInstance(self.board.__positions__[0][0], Rook)
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")
        self.assertEqual(self.board.__positions__[0][0].__color__, "BLACK")


    def test_empty_square_no_piece(self):
        self.assertEqual(self.board.get_piece(3, 3), "No piece")


    @patch('builtins.print')
    def test_piece_move_and_str_representation(self, patched_print):
        self.assertEqual(self.board.piece_to_STR(0, 0), ({'ROOK'}, {'BLACK'}))
        self.board.move_piece(0, 0, 4, 0)
        self.assertEqual(self.board.get_piece(0, 0), "No piece")


    @patch('builtins.print')
    def test_illegal_move_no_piece_on_board(self, patched_print):
        self.assertEqual(self.board.permited_move(5, 5, 6, 5), False)


    @patch('builtins.print')
    def test_exception_on_empty_source_square(self, patched_print):
        with self.assertRaises(NotPieceToMove) as exc:
            self.board.move_piece(5, 5, 1, 0)


    @patch('builtins.print')
    def test_illegal_move_destination_occupied_same_color(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[4][7] = Rook("WHITE")
        with self.assertRaises(NotPermitedMove) as exc:
            self.board.move_piece(4, 7, 4, 6)


    @patch('builtins.print')
    def test_illegal_move_to_non_permitted_position(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        with self.assertRaises(NotPermitedMove) as exc:
            self.board.move_piece(4, 6, 5, 5)


    @patch('builtins.print')
    def test_white_pawn_captures_black(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[3][5] = Pawn("BLACK")
        self.board.capture_piece(3, 5, 4, 6)
        self.assertEqual(self.board.pieces_from_white[0], '♟')
        self.assertEqual(len(self.board.pieces_from_black), 0)


    @patch('builtins.print')
    def test_black_pawn_captures_white(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[3][5] = Pawn("BLACK")
        self.board.capture_piece(4, 6, 3, 5)
        self.assertEqual(self.board.pieces_from_black[0], '♙')
        self.assertEqual(len(self.board.pieces_from_black), 1)


    def test_no_capture_when_no_piece(self):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.assertEqual(self.board.capture_piece(4, 6, 3, 5), False)


    def test_str_representation_of_empty_square(self):
        self.assertEqual(self.board.piece_to_STR(3, 3), "No piece")



class TestBoardMovePiece(unittest.TestCase):


    def setUp(self):
        self.board = Board()
        self.board.__positions__[0][0] = Rook("WHITE")
        self.board.__positions__[1][0] = Pawn("BLACK")


    @patch('builtins.print')
    def test_move_attempt_empty_square(self, mock_print):
        # Intentar mover una pieza desde una posición vacía
        with self.assertRaises(NotPieceToMove):
            self.board.move_piece(2, 2, 3, 3)


    @patch('builtins.print')
    def test_blocked_move_same_color_piece(self, mock_print):
        # Intentar mover una pieza a una posición ocupada por una pieza del mismo color
        self.board.__positions__[0][1] = Pawn("WHITE")
        with self.assertRaises(NotPermitedMove):
            self.board.move_piece(0, 0, 0, 1)


#COMPLETE