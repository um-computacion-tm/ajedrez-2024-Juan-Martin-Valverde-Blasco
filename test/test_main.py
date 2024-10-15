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
import io
import sys


class TestMain(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()
        self.chess = Chess()


    @patch('builtins.print')
    @patch('builtins.input', side_effect=["e"])
    def test_play_invalid_input_error(self, patched_print, mock_input):
        self.cli.play()
        self.assertEqual(self.cli.play(), "error")


    @patch('builtins.print')
    def test_verify_color_valid_piece(self, patched_print):
        result = self.chess.right_color(7, 0)
        self.assertIsNone(result)
        self.assertEqual(self.cli.verify_color(self.chess, 7, 0), True)


    @patch('builtins.print')
    def test_verify_color_no_piece_on_position(self, patched_print):
        self.chess.right_color(5, 5)
        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)


    def test_play_with_empty_board_except_black_queen(self):
        self.chess.__board__.__positions__[5][5] = Queen("BLACK")
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None
            self.chess.__board__.__positions__[0][col] = None
        print(self.chess.__board__.get_piece(5, 5))
        self.cli.play()


    @patch('builtins.print')
    @patch('builtins.input', side_effect=[6, 6, 4, 6])
    def test_end_game_called_when_black_queen_left(self, patched_print, mock_input):
        self.chess.__board__.__positions__[5][5] = Queen("BLACK")
        for col in range(8):
            self.chess.__board__.__positions__[1][col] = None
            self.chess.__board__.__positions__[0][col] = None
        self.chess.__board__.pieces_from_black_piece = [Rook("BLACK"), Rook("BLACK"), Knight("BLACK"), Knight("BLACK"), 
                                                        Bishop("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), 
                                                        Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK")]
        self.cli.chess = self.chess
        self.assertEqual(self.chess.__board__.piece_to_STR(5, 5), ({'QUEEN'}, {'BLACK'}))
        self.assertIsInstance(self.chess.__board__.get_piece(5, 5), Queen)
        self.assertIsNone(self.cli.play())


#    @patch('builtins.print')
#    @patch('builtins.input', side_effect = [6, 6, 4, 6, "y"])
#    def test_answer_yes(self, patched_print, mock_input):
#        self.cli.play()
#
#        self.assertEqual(self.cli.chess.__turn__, "BLACK")

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
            "-------------------------Proyect For computacionI Ing informaticaUM-------------------------\n"
            "--------------------------------------------------------------------------------------------\n"
        )

        # Comparar la salida capturada con la salida esperada
        self.assertEqual(captured_output.getvalue(), expected_output)
        
    def test_main_menu(self):
        # Capturar la salida de la función main_menu
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cli.main_menu()
        sys.stdout = sys.__stdout__

        # Salida esperada
        expected_output = (
            "------------------------------------------Opciones---------------------------------------------\n"
            "Presiona 1 para empezar a jugar\n"
            "Presiona 2 para ver un tutorial\n"
            "Presiona 3 para salir\n"
            "-----------------------------------------------------------------------------------------------\n"
        )

        # Comparar la salida capturada con la salida esperada
        self.assertEqual(captured_output.getvalue(), expected_output)


    @patch('builtins.exit')
    def test_handle_option_3(self, mock_exit):
        # Capturar la salida de la función handle_option_3
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cli.handle_option_3()
        sys.stdout = sys.__stdout__

        # Salida esperada
        expected_output = "Hasta luego\n"

        # Comparar la salida capturada con la salida esperada
        self.assertEqual(captured_output.getvalue(), expected_output)
        # Verificar que exit() fue llamado
        mock_exit.assert_called_once()


class TestHandleInputs(unittest.TestCase):
    
    def setUp(self):
        self.main = Cli()
        self.main.play = MagicMock()
        self.main.handle_option_2 = MagicMock()
        self.main.handle_option_3 = MagicMock()

    def test_handle_user_input_option_1(self):
        self.main.handle_user_input(1)
        self.main.play.assert_called_once()
        self.main.handle_option_2.assert_not_called()
        self.main.handle_option_3.assert_not_called()

    def test_handle_user_input_option_2(self):
        self.main.handle_user_input(2)
        self.main.handle_option_2.assert_called_once()
        self.main.play.assert_not_called()
        self.main.handle_option_3.assert_not_called()

    def test_handle_user_input_option_3(self):
        self.main.handle_user_input(3)
        self.main.handle_option_3.assert_called_once()
        self.main.play.assert_not_called()
        self.main.handle_option_2.assert_not_called()
        

class TestClient(unittest.TestCase):
    def setUp(self):
        self.main = Cli()
        self.main.welcome_message = MagicMock()
        self.main.main_menu = MagicMock()
        self.main.handle_user_input = MagicMock()
        self.main.handle_option_2 = MagicMock()

    @patch('builtins.input', side_effect=['1', '2', '4', '3'])
    @patch('builtins.print')
    def test_client(self, mock_print, mock_input):
        # Capturar la salida de la función client
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Ejecutar la función client
        self.main.client()

        sys.stdout = sys.__stdout__

        # Verificar que welcome_message y main_menu fueron llamados
        self.main.welcome_message.assert_called_once()
        self.assertEqual(self.main.main_menu.call_count, 4)

        # Verificar que handle_user_input y handle_option_2 fueron llamados
        self.main.handle_user_input.assert_called_once_with(1)
        self.main.handle_option_2.assert_called_once()

        # Verificar que se imprimió "Opcion invalida" para la opción 4
        mock_print.assert_any_call("Opcion invalida")
        # Verificar que se imprimió "Hasta luego" para la opción 3
        mock_print.assert_any_call("Hasta luego")

