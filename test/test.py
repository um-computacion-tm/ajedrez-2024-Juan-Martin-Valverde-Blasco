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


class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_chess_init(self):
        self.assertEqual(self.chess.__turn__, "WHITE")

    def test_turn_change(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")

    @patch('builtins.print')
    def test_move_piece(self, patched_print):

        self.assertEqual(self.chess.__board__.get_piece_for_show(7, 0), ({'ROOK'}, {'WHITE'}))

        self.chess.move(7, 0, 5, 0)

        self.assertEqual(self.chess.__board__.get_piece(7, 0), "No piece")

        self.assertEqual(self.chess.__turn__, "WHITE")

    # @patch('builtins.print')
    # def test_move_no_piece(self, patched_print):

    #     self.chess.__board__.get_piece(7, 0)

    #     self.assertEqual(self.chess.move(5,7,2,2), "You can't move a piece that doesn't exist")

    @patch('builtins.print')
    def test_move_correct_color_white_turn(self, patched_print):

        result = self.chess.move_correct_color(7, 0)
        self.assertIsNone(result)


        result = self.chess.move_correct_color(0, 0)
        self.assertEqual(result, "You can't move a piece that is not your color")

    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["0"])
    def test_define_new_piece_black(self, patched_print, mock_input):
        self.chess.__board__.pieces_from_black = ["♕"]
        self.chess.__board__.pieces_from_black_piece = [Queen("BLACK")]

        self.chess.__board__.__positions__[7][0] = Pawn("BLACK")

        function = self.chess.define_new_piece(6, 0, 7, 0, self.chess.__board__.pieces_from_black_piece)


        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["0"])
    def test_define_new_piece_white(self, patched_print, mock_input):
        self.chess.__board__.pieces_from_white = ["♛"]
        self.chess.__board__.pieces_from_white_piece = [Queen("WHITE")]

        self.chess.__board__.__positions__[7][0] = Pawn("WHITE")

        function = self.chess.define_new_piece(6, 0, 7, 0, self.chess.__board__.pieces_from_white_piece)


        self.assertEqual(self.chess.__board__.__positions__[7][0].__type__, "QUEEN")
        self.assertIsInstance(function, Queen)


    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["1"])
    def test_replace_piece(self, patched_print, mock_input):
        self.chess.__board__.__positions__[0][7] = None

        self.chess.__board__.__positions__[1][7] = Pawn("WHITE")

        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Queen("BLACK")]
        self.chess.__board__.pieces_from_black = ["♖", "♕"]

        self.chess.__board__.pieces_from_white_piece = [Rook("WHITE"), Queen("WHITE")]
        self.chess.__board__.pieces_from_white = ["♜", "♛"]

        self.chess.move(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece_for_show(0, 7), ({'PAWN'}, {'WHITE'}))
        self.assertIsInstance(self.chess.__board__.get_piece(0, 7), Pawn)

        self.chess.change_pawn_for_other(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece_for_show(0, 7), ({'QUEEN'}, {'WHITE'}))
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect = ["1"])
    def test_replace_piece_black(self, patched_print, mock_input):
        self.chess.__board__.__positions__[0][7] = None

        self.chess.__board__.__positions__[1][7] = Pawn("WHITE")

        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Queen("BLACK")]
        self.chess.__board__.pieces_from_black = ["♖", "♕"]

        self.chess.__board__.pieces_from_white_piece = [Rook("WHITE"), Queen("WHITE")]
        self.chess.__board__.pieces_from_white = ["♜", "♛"]

        self.chess.move(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece_for_show(0, 7), ({'PAWN'}, {'WHITE'}))
        self.assertIsInstance(self.chess.__board__.get_piece(0, 7), Pawn)

        self.chess.change_pawn_for_other(1, 7, 0, 7)

        self.assertEqual(self.chess.__board__.get_piece_for_show(0, 7), ({'QUEEN'}, {'WHITE'}))
        

    def test_verify_winner(self):
        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Rook("BLACK"), Knight("BLACK"), Knight("BLACK"), 
                                                        Bishop("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")]

        self.assertEqual(self.chess.verify_winner(), "WHITE WINS")


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()


    def test_init_board_rook(self):
        self.assertIsInstance(self.board.__positions__[0][0], Rook)
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")
        self.assertEqual(self.board.__positions__[0][0].__color__, "BLACK")


    def test_get_piece_empty(self):
        self.assertEqual(self.board.get_piece(3, 3), "No piece")

    @patch('builtins.print')
    def test_move_piece(self, patched_print):

        self.assertEqual(self.board.get_piece_for_show(0, 0), ({'ROOK'}, {'BLACK'}))

        self.board.move_piece(0, 0, 4, 0)

        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    # @patch('builtins.print')
    # def test_move_piece_no_piece_get(self, patched_print):

    #     self.assertEqual(self.board.move_piece(3, 3, 4, 4), "No piece to move")

    #     self.assertEqual(self.board.get_piece(3, 3), "No piece")
    #     self.assertEqual(self.board.get_piece(4, 4), "No piece")

    def test_permited_move_false_not_permited(self):
        self.assertEqual(self.board.permited_move(0, 0, 5, 5), False)

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

        self.board.eat_piece(3, 5, 4, 6)
        
        self.assertEqual(self.board.pieces_from_white[0], '♟') #Significa que la pieza comida fue la blanca
        self.assertEqual(len(self.board.pieces_from_black), 0)

    @patch('builtins.print')
    def test_eat_piece_black_eats_white(self, patched_print):
        self.board.__positions__[4][6] = Pawn("WHITE")
        self.board.__positions__[3][5] = Pawn("BLACK")

        self.board.eat_piece(4, 6, 3, 5)

        self.assertEqual(self.board.pieces_from_black[0], '♙')
        self.assertEqual(len(self.board.pieces_from_black), 1)

    def test_eat_no_piece(self):
        self.board.__positions__[4][6] = Pawn("WHITE")

        self.assertEqual(self.board.eat_piece(4, 6, 3, 5), False)



class TestPiece(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board()
        return super().setUp()

    def test_piece_init(self):
        piece = Piece("BLACK")
        self.assertEqual(piece.__color__, "BLACK")
        self.assertEqual(piece.__type__, None)

    def test_rook_init(self):
        rook = Rook("BLACK")
        self.assertEqual(rook.__color__, "BLACK")
        self.assertEqual(rook.__type__, "ROOK")

    def test_pawn_init(self):
        pawn = Pawn("WHITE")
        self.assertEqual(pawn.__color__, "WHITE")
        self.assertEqual(pawn.__type__, "PAWN")

    def test_knight_init(self):
        knight = Knight("WHITE")
        self.assertEqual(knight.__color__, "WHITE")
        self.assertEqual(knight.__type__, "KNIGHT")

    def test_bishop_init(self):
        bishop = Bishop("WHITE")
        self.assertEqual(bishop.__color__, "WHITE")
        self.assertEqual(bishop.__type__, "BISHOP")

    def test_queen_init(self):
        queen = Queen("WHITE")
        self.assertEqual(queen.__color__, "WHITE")
        self.assertEqual(queen.__type__, "QUEEN")

    def test_king_init(self):
        king = King("WHITE")
        self.assertEqual(king.__color__, "WHITE")
        self.assertEqual(king.__type__, "KING")


    def test_permited_move_pawn(self):
        self.assertEqual(self.board.permited_move(1, 0, 3, 0), True)
        self.assertEqual(self.board.permited_move(1, 0, 2, 0), True)
        self.assertEqual(self.board.permited_move(1, 0, 5, 0), False)
        self.assertEqual(self.board.permited_move(6, 0, 5, 0), True)
        self.assertEqual(self.board.permited_move(6, 0, 4, 0), True)

        self.board.__positions__[4][1] = Pawn("WHITE")
        self.board.__positions__[3][2] = Pawn("BLACK")

        self.assertEqual(self.board.permited_move(4, 1, 3, 2), True)


    def test_permited_move_knight(self):

        self.assertEqual(self.board.permited_move(0, 1, 2, 2), True)
        self.assertEqual(self.board.permited_move(0, 1, 2, 0), True)

        self.board.__positions__[4][4] = Knight("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 2, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 2, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 5), True)
        self.assertEqual(self.board.permited_move(4, 4, 6, 3), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 6), True)
        self.assertEqual(self.board.permited_move(4, 4, 3, 2), True)
        self.assertEqual(self.board.permited_move(4, 4, 5, 6), True)
        self.assertEqual(self.board.permited_move(4, 4, 5, 2), True)


        self.assertEqual(self.board.permited_move(4, 4, 3, 5), False)

    def test_permited_move_line_77(self):
        self.board.__positions__[2][2] = Knight("BLACK")
        self.assertEqual(self.board.__positions__[2][2].__type__, "KNIGHT")

        self.assertEqual(self.board.get_piece_for_show(2, 2), ({'KNIGHT'}, {'BLACK'}))
        self.assertIsInstance(self.board.get_piece(2, 2), Knight)

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

        self.board.__positions__[4][4] = Rook("BLACK")

        self.assertEqual(self.board.permited_move(4, 4, 4, 2), True)
        self.assertEqual(self.board.permited_move(4, 4, 2, 4), True)

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


class TestMain(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()
        self.chess = Chess()

        
    @patch('builtins.print')
    @patch ('builtins.input', side_effect = ["e"])
    def test_play_error(self,patched_print, mock_input):
        self.cli.play()

        self.assertEqual(self.cli.play(), "error")


    @patch('builtins.print')
    def test_verify_color(self, patched_print):

        result = self.chess.move_correct_color(7, 0)
        self.assertIsNone(result)

        self.assertEqual(self.cli.verify_color(self.chess, 7, 0), True)

    @patch('builtins.print')
    def test_verify_color_no_piece(self, patched_print):

        self.chess.move_correct_color(5, 5)

        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)
        
    @patch('builtins.print')
    def test_verify_color_no_piece(self, patched_print):

        self.chess.move_correct_color(5, 5)

        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)
        

    # #Como testeo que levante invalidposition 1 vez si lo tengo en bucle
    # @patch('builtins.print', side_effect= [9, 9])
    # def test_verify_move_invalid_position(self, patched_print):

    #     with self.assertRaises(InvalidPosition) as exc:
    #         self.cli.verify_move(self.chess)


    #Como testeo que se termine el juego cuando ya no hay piezas de un color
    @patch('builtins.print')
    @patch('builtins.input', side_effect= ["6", "6", "4", "6"])
    def test_verify_winner(self, mock_input, patched_print):
        self.cli.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Rook("BLACK"), Knight("BLACK"), Knight("BLACK"), 
                                                        Bishop("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")]

        self.cli.play()

        patched_print.assert_any_call(
            "WHITE WINS",
            )
        patched_print.assert_any_call(
            "Game ended",
            )

    def test_verify_end_game_called(self):

        self.chess.__board__.__positions__[5][5] = Queen("BLACK") #"RookBlack"
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None #"PawnBlack"
            self.chess.__board__.__positions__[0][col] = None 
        print(self.chess.__board__.get_piece(5, 5))
        self.cli.play()

    @patch('builtins.print')
    @patch ('builtins.input', side_effect = [6,6,4,6])
    def test_verify_end_game_called(self, patched_print, mock_input):
        # Modificar el tablero directamente
        self.chess.__board__.__positions__[5][5] = Queen("BLACK")
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None  # Eliminar todas las piezas negras de la fila 1
            self.chess.__board__.__positions__[0][col] = None  # Eliminar todas las piezas negras de la fila 0

        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Rook("BLACK"), Knight("BLACK"), Knight("BLACK"), 
                                                        Bishop("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")]


        # Asegurarse de que `self.cli` use el mismo tablero que acabamos de modificar
        self.cli.chess = self.chess

        self.assertEqual(self.chess.__board__.get_piece_for_show(5, 5), ({'QUEEN'}, {'BLACK'}))

        self.assertIsInstance(self.chess.__board__.get_piece(5, 5), Queen)

        self.assertIsNone(self.cli.play())

    @patch('builtins.print')
    @patch('builtins.input', side_effect = [6, 6, 4, 6, "y"])
    def test_answer_yes(self, patched_print, mock_input):
        self.cli.play()

        self.assertEqual(self.cli.chess.__turn__, "BLACK")


if __name__ == '__main__':
    unittest.main()
