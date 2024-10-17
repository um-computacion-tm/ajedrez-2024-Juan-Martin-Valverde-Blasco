import unittest
from unittest.mock import patch, MagicMock
from game.king import King
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.chess import Chess
from game.main import Cli
from game.exceptions import NotPieceToMove
import io
import sys
from io import StringIO

class TestMain(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()
        self.chess = Chess()


#    @patch('builtins.input', side_effect=['invalid input', 'n'])
#    @patch('builtins.print')
#    def test_play_invalid_input_error(self, mock_print, mock_input):
#        self.assertEqual(self.cli.client(), "Error")


    @patch('builtins.print')
    def test_verify_color_valid_piece(self, patched_print):
        result = self.chess.right_color(7, 0)
        self.assertIsNone(result)
        self.assertEqual(self.cli.verify_color(self.chess, 7, 0), True)


    @patch('builtins.print')
    def test_verify_color_no_piece_on_position(self, patched_print):
        self.chess.right_color(5, 5)
        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)


    def test_welcome_message(self):
        # Capturar la salida de la función welcome_message
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cli.welcome_message()
        sys.stdout = sys.__stdout__

        # Salida esperada
        expected_output = (
            "--------------------------------------------------------------------------------------------\n"
            "-------------------------Welcome to Ajedrez By Juan Martin Valverde-------------------------\n"
            "----------------------------Tecnical consultor Copilot and GPT-4----------------------------\n"
            "-------------------------Proyect For ComputacionI Ing informaticaUM-------------------------\n"
            "--------------------------------------------------------------------------------------------\n"
        )

        # Comparar la salida capturada con la salida esperada
        self.assertEqual(captured_output.getvalue(), expected_output)
        
    def test_main_menu(self):
        # Capturar la salida de la función main_menu
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cli.main_menu1()
        sys.stdout = sys.__stdout__

        # Salida esperada
        expected_output = (
            "------------------------------------------Opciones---------------------------------------------\n"
            "Presiona 1 para comenzar a jugar\n"
            "Presiona 2 para ver un tutorial\n"
            "Presiona 3 para salir\n"
            "-----------------------------------------------------------------------------------------------\n"
        )

        # Comparar la salida capturada con la salida esperada
        self.assertEqual(captured_output.getvalue(), expected_output)
        

class TestClient(unittest.TestCase):
    def setUp(self):
        self.main = Cli()
        self.main.welcome_message = MagicMock()
        self.main.client = MagicMock()
        self.main.tutorial_pawn_moves_and_attacks = MagicMock()
        self.main.tutorial_rook_moves_and_attacks = MagicMock()
        self.main.tutorial_knight_moves_and_attacks = MagicMock()
        self.main.tutorial_bishop_moves_and_attacks = MagicMock()
        self.main.tutorial_queen_moves_and_attacks = MagicMock()
        self.main.tutorial_king_moves_and_attacks = MagicMock()

    def test_handle_option_2(self):
        self.main.show_tutorial()
        self.main.tutorial_pawn_moves_and_attacks.assert_called_once()
        self.main.tutorial_rook_moves_and_attacks.assert_called_once()
        self.main.tutorial_knight_moves_and_attacks.assert_called_once()
        self.main.tutorial_bishop_moves_and_attacks.assert_called_once()
        self.main.tutorial_queen_moves_and_attacks.assert_called_once()
        self.main.tutorial_king_moves_and_attacks.assert_called_once()


