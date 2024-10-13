import unittest

from unittest.mock import patch
from io import StringIO


from game.piece import Piece
from game.king import King
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen

from game.board import Board, NotPieceToMove, NotPermitedMove
from game.chess import Chess
from game.main import Cli

from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")


#    def test_show_board_empty(self):
#        expected_output = (
#            "      a    b    c    d    e    f    g    h\n"
#            "   ╔════╤════╤════╤════╤════╤════╤════╤════╗\n"
#            " 8 ║    │    │    │    │    │    │    │    ║ 8\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 7 ║    │    │    │    │    │    │    │    ║ 7\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 6 ║    │    │    │    │    │    │    │    ║ 6\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 5 ║    │    │    │    │    │    │    │    ║ 5\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 4 ║    │    │    │    │    │    │    │    ║ 4\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 3 ║    │    │    │    │    │    │    │    ║ 3\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 2 ║    │    │    │    │    │    │    │    ║ 2\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 1 ║    │    │    │    │    │    │    │    ║ 1\n"
#            "   ╚════╧════╧════╧════╧════╧════╧════╧════╝\n"
#            "      a    b    c    d    e    f    g    h\n"
#        )
#
#        captured_output = io.StringIO()
#        sys.stdout = captured_output
#        self.board.show_board()
#        sys.stdout = sys.__stdout__
#
#        self.maxDiff = None
#        self.assertEqual(captured_output.getvalue(), expected_output)
#
#    def test_show_board_with_pieces(self):
#        self.board.__positions__[0][0] = Pawn("WHITE", "♟", "♟")
#        self.board.__positions__[7][7] = Pawn("BLACK", "♙", "♙")
#
#        expected_output = (
#            "      a    b    c    d    e    f    g    h\n"
#            "   ╔════╤════╤════╤════╤════╤════╤════╤════╗\n"
#            " 8 ║ ♖  │    │    │    │    │    │    │    ║ 8\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 7 ║    │    │    │    │    │    │    │    ║ 7\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 6 ║    │    │    │    │    │    │    │    ║ 6\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 5 ║    │    │    │    │    │    │    │    ║ 5\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 4 ║    │    │    │    │    │    │    │    ║ 4\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 3 ║    │    │    │    │    │    │    │    ║ 3\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 2 ║    │    │    │    │    │    │    │    ║ 2\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 1 ║    │    │    │    │    │    │    │ ♜  ║ 1\n"
#            "   ╚════╧════╧════╧════╧════╧════╧════╧════╝\n"
#            "      a    b    c    d    e    f    g    h\n"
#        )
#
#        captured_output = io.StringIO()
#        sys.stdout = captured_output
#        self.board.show_board()
#        sys.stdout = sys.__stdout__
#
#        self.maxDiff = None
#        self.assertEqual(captured_output.getvalue(), expected_output)
 

#    def test_show_board_initial(self):
#        expected_output = (
#            "      a    b    c    d    e    f    g    h\n"
#            "   ╔════╤════╤════╤════╤════╤════╤════╤════╗\n"
#            " 8 ║ ♖  │ ♘  │ ♗  │ ♕  │ ♔  │ ♗  │ ♘  │ ♖  ║ 8\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 7 ║ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  ║ 7\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 6 ║    │    │    │    │    │    │    │    ║ 6\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 5 ║    │    │    │    │    │    │    │    ║ 5\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 4 ║    │    │    │    │    │    │    │    ║ 4\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 3 ║    │    │    │    │    │    │    │    ║ 3\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 2 ║ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  ║ 2\n"
#            "   ╟────┼────┼────┼────┼────┼────┼────┼────╢\n"
#            " 1 ║ ♜  │ ♞  │ ♝  │ ♛  │ ♚  │ ♝  │ ♞  │ ♜  ║ 1\n"
#            "   ╚════╧════╧════╧════╧════╧════╧════╧════╝\n"
#            "      a    b    c    d    e    f    g    h\n"
#        )
#
#        captured_output = io.StringIO()
#        sys.stdout = captured_output
#        self.board.show_board()
#        sys.stdout = sys.__stdout__
#
#        self.maxDiff = None
#        self.assertEqual(captured_output.getvalue(), expected_output)


        
        
    def test_move_piece_destination_occupied_by_same_color(self):
        self.board.__positions__[0][0] = Piece("WHITE")
        self.board.__positions__[1][1] = Piece("WHITE")
        with self.assertRaises(NotPermitedMove) as context:
            self.board.move_piece(0, 0, 1, 1)
        self.assertEqual(str(context.exception), "Cannot move to a position occupied by a piece with the same color")

    def test_move_piece_not_permitted_move(self):
        self.board.__positions__[0][0] = Piece("WHITE")
        self.board.permited_move = lambda from_row, from_col, to_row, to_col: False
        with self.assertRaises(NotPermitedMove) as context:
            self.board.move_piece(0, 0, 1, 1)
        self.assertEqual(str(context.exception), "The piece cannot be moved in this position")

    def test_init_board_rook(self):
        self.assertIsInstance(self.board.__positions__[0][0], Rook)
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")
        self.assertEqual(self.board.__positions__[0][0].__color__, "BLACK")


    def test_get_piece_empty(self):
        self.assertEqual(self.board.get_piece(3, 3), "No piece")

    @patch('builtins.print')
    def test_move_piece(self, patched_print):

        self.assertEqual(self.board.piece_to_STR(0, 0), ({'ROOK'}, {'BLACK'}))

        self.board.move_piece(0, 0, 4, 0)

        self.assertEqual(self.board.get_piece(0, 0), "No piece")

#    def test_permited_move_false_not_permited(self):
#        self.assertEqual(self.board.permited_move(0, 0, 5, 5), False)

    @patch('builtins.print')
    def test_permited_move_false_no_piece(self, patched_print):
        self.assertEqual(self.board.permited_move(5, 5, 6, 5), False)

    @patch('builtins.print')
    def test_no_piece_to_move_exception_move(self, patched_print):

        with self.assertRaises(NotPieceToMove) as exc:
            self.board.move_piece(5, 5, 1, 0)

    @patch('builtins.print')
    def test_destination_same_color(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[4][7] = Rook("WHITE")

        with self.assertRaises(NotPermitedMove) as exc:
            self.board.move_piece(4, 7, 4, 6)


    @patch('builtins.print')
    def test_not_permited_move_position(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")

        with self.assertRaises(NotPermitedMove) as exc:
            self.board.move_piece(4, 6, 5, 5)

    @patch('builtins.print')
    def test_eat_piece_white_eats_black(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[3][5] = Pawn("BLACK")

        self.board.capture_piece(3, 5, 4, 6)
        
        self.assertEqual(self.board.pieces_from_white[0], '♟') #Significa que la pieza comida fue la blanca
        self.assertEqual(len(self.board.pieces_from_black), 0)

    @patch('builtins.print')
    def test_eat_piece_black_eats_white(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[3][5] = Pawn("BLACK")

        self.board.capture_piece(4, 6, 3, 5)

        self.assertEqual(self.board.pieces_from_black[0], '♙')
        self.assertEqual(len(self.board.pieces_from_black), 1)

    def test_eat_no_piece(self):
        self.board.__positions__[4][6] = Pawn("WHITE")

        self.assertEqual(self.board.capture_piece(4, 6, 3, 5), False)

    def test_piece_to_STR_no_piece(self):
        # Verificar que devuelve "No piece" cuando no hay pieza en la posición
        self.assertEqual(self.board.piece_to_STR(3, 3), "No piece")

#    def test_piece_to_STR_with_piece(self):
#        # Verificar que devuelve el tipo y color de la pieza correctamente
#        self.board.__positions__[0][0] = Rook("BLACK")
#        self.assertEqual(self.board.piece_to_STR(0, 0), ("ROOK", "BLACK"))
#
#        self.board.__positions__[7][7] = Queen("WHITE")
#        self.assertEqual(self.board.piece_to_STR(7, 7), ("QUEEN", "WHITE"))

#    def test_piece_to_STR_with_different_pieces(self):
#        # Verificar que devuelve el tipo y color de diferentes piezas correctamente
#        self.board.__positions__[1][1] = Knight("BLACK")
#        self.assertEqual(self.board.piece_to_STR(1, 1), ("KNIGHT", "BLACK"))
#
#        self.board.__positions__[6][6] = Bishop("WHITE")
#        self.assertEqual(self.board.piece_to_STR(6, 6), ("BISHOP", "WHITE"))




class TestBoardMovePiece(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.__positions__[0][0] = Rook("WHITE")
        self.board.__positions__[1][0] = Pawn("BLACK")


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



