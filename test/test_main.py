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


    @patch('builtins.input', side_effect=['invalid input', 'n'])
    @patch('builtins.print')
    def test_play_invalid_input_error(self, mock_print, mock_input):
        self.assertEqual(self.cli.play(), "Error")


    @patch('builtins.print')
    def test_verify_color_valid_piece(self, patched_print):
        result = self.chess.right_color(7, 0)
        self.assertIsNone(result)
        self.assertEqual(self.cli.verify_color(self.chess, 7, 0), True)


    @patch('builtins.print')
    def test_verify_color_no_piece_on_position(self, patched_print):
        self.chess.right_color(5, 5)
        self.assertEqual(self.cli.verify_color(self.chess, 5, 5), False)




#    @patch('builtins.input', side_effect=['1 1 2 2', 'n'])
#    @patch('builtins.print')
#    def test_end_game_called_when_black_queen_left(self, mock_print, mock_input):
#        self.cli.chess.verify_winner = MagicMock(return_value="Equipo WHITE gana")
#        self.assertIsNone(self.cli.play())

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
        self.main.play = MagicMock()
        self.main.handle_pawn_moves_and_attacks = MagicMock()
        self.main.handle_rook_moves_and_attacks = MagicMock()
        self.main.handle_knight_moves_and_attacks = MagicMock()
        self.main.handle_bishop_moves_and_attacks = MagicMock()
        self.main.handle_queen_moves_and_attacks = MagicMock()
        self.main.handle_king_moves_and_attacks = MagicMock()

    def test_handle_option_2(self):
        self.main.handle_option_2()
        self.main.handle_pawn_moves_and_attacks.assert_called_once()
        self.main.handle_rook_moves_and_attacks.assert_called_once()
        self.main.handle_knight_moves_and_attacks.assert_called_once()
        self.main.handle_bishop_moves_and_attacks.assert_called_once()
        self.main.handle_queen_moves_and_attacks.assert_called_once()
        self.main.handle_king_moves_and_attacks.assert_called_once()

    @patch('builtins.input', return_value='1')
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu')
    @patch.object(Cli, 'handle_user_input')
    def test_client(self, mock_handle_user_input, mock_main_menu, mock_welcome_message, mock_input):
        game = Cli()
        game.client()
        
        # Verificar que se haya llamado a welcome_message
        mock_welcome_message.assert_called_once()
        
        # Verificar que se haya llamado a main_menu
        mock_main_menu.assert_called_once()
        
        # Verificar que se haya llamado a handle_user_input con el valor 1
        mock_handle_user_input.assert_called_once_with(1)

    @patch('builtins.input', return_value='1')
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu')
    @patch.object(Cli, 'handle_user_input')
    def test_client(self, mock_handle_user_input, mock_main_menu, mock_welcome_message, mock_input):
        game = Cli()
        game.client()
        
        # Verificar que se haya llamado a welcome_message
        mock_welcome_message.assert_called_once()
        
        # Verificar que se haya llamado a main_menu
        mock_main_menu.assert_called_once()
        
        # Verificar que se haya llamado a handle_user_input con el valor 1
        mock_handle_user_input.assert_called_once_with(1)


class TestClientFunction(unittest.TestCase):
    def setUp(self):
        self.main = Cli()
        self.main.play = MagicMock()
        self.main.handle_option_2 = MagicMock()
        self.main.handle_option_3 = MagicMock()

    @patch('builtins.input', return_value='1')
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu')
    @patch.object(Cli, 'handle_user_input')
    def test_client(self, mock_handle_user_input, mock_main_menu, mock_welcome_message, mock_input):
        game = Cli()
        game.client()
        
        # Verificar que se haya llamado a welcome_message
        mock_welcome_message.assert_called_once()
        
        # Verificar que se haya llamado a main_menu
        mock_main_menu.assert_called_once()
        
        # Verificar que se haya llamado a handle_user_input con el valor 1
        mock_handle_user_input.assert_called_once_with(1)

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

    @patch('builtins.print')
    def test_handle_user_input_invalid_option(self, mock_print):
        self.main.handle_user_input(99)
        mock_print.assert_called_once_with("Opcion invalida")
        self.main.play.assert_not_called()
        self.main.handle_option_2.assert_not_called()
        self.main.handle_option_3.assert_not_called()


#class TestPlayFunction(unittest.TestCase):
#    def setUp(self):
#        self.main = Cli()
#        self.main.chess = MagicMock()
#        self.main.chess.__board__ = MagicMock()
#        self.main.chess.__board__.show_board = MagicMock()
#        self.main.chess.__board__.capture_piece = MagicMock(return_value="Pieza capturada")
#        self.main.chess.movement_fits = MagicMock()
#        self.main.chess.change_pawn = MagicMock()
#        self.main.chess.STR_captured_pieces = MagicMock(return_value="Piezas capturadas")
#        self.main.chess.verify_winner = MagicMock(return_value=False)
#        self.main.chess.change_turn = MagicMock()
#        self.main.chess.__turn__ = "WHITE"
#        self.main.verify_move = MagicMock(return_value=(1, 1))
#        self.main.validate_range_to = MagicMock(return_value=(2, 2))
#
#    @patch('builtins.input', side_effect=['s', 'n'])
#    @patch('builtins.print')
#    def test_play_game_continues_and_ends(self, mock_print, mock_input):
#        self.main.play()
#        
#        # Verificar que se haya mostrado el tablero dos veces
#        self.assertEqual(self.main.chess.__board__.show_board.call_count, 2)
#        
#        # Verificar que se haya capturado una pieza
#        self.main.chess.__board__.capture_piece.assert_called_once_with(1, 1, 2, 2)
#        
#        # Verificar que se haya llamado a movement_fits y change_pawn
#        self.main.chess.movement_fits.assert_called_once_with(1, 1, 2, 2)
#        self.main.chess.change_pawn.assert_called_once_with(1, 1, 2, 2)
#        
#        # Verificar que se haya mostrado las piezas capturadas
#        mock_print.assert_any_call("Piezas capturadas")
#        
#        # Verificar que se haya cambiado el turno
#        self.main.chess.change_turn.assert_called_once()
#        
#        # Verificar que se haya preguntado si se quiere seguir jugando
#        mock_input.assert_any_call("Quieres seguir jugando? (s/n): ")
#        
#        # Verificar que se haya terminado el juego por decisión del jugador
#        mock_print.assert_any_call("Fin del juego")
#
#
#
#    @patch('builtins.input', side_effect=['s'])
#    @patch('builtins.print')
#    def test_play_game_winner(self, mock_print, mock_input):
#        self.main.chess.verify_winner = MagicMock(return_value="Jugador 1 gana")
#        
#        self.main.play()
#        
#        # Verificar que se haya mostrado el tablero una vez
#        self.main.chess.__board__.show_board.assert_called_once()
#        
#        # Verificar que se haya capturado una pieza
#        self.main.chess.__board__.capture_piece.assert_called_once_with(1, 1, 2, 2)
#        
#        # Verificar que se haya llamado a movement_fits y change_pawn
#        self.main.chess.movement_fits.assert_called_once_with(1, 1, 2, 2)
#        self.main.chess.change_pawn.assert_called_once_with(1, 1, 2, 2)
#        
#        # Verificar que se haya mostrado las piezas capturadas
#        mock_print.assert_any_call("Piezas capturadas")
#        
#        # Verificar que se haya mostrado el ganador
#        mock_print.assert_any_call("Jugador 1 gana")
#        mock_print.assert_any_call("Fin del juego")

#    @patch('builtins.input', side_effect=['s', 'n'])
#    @patch('builtins.print')
#    def test_play_game_exception(self, mock_print, mock_input):
#        self.main.chess.__board__.capture_piece.side_effect = NotPieceToMove("No hay pieza para mover")
#        
#        self.main.play()
#        
#        # Verificar que se haya mostrado el tablero una vez
#        self.main.chess.__board__.show_board.assert_called_once()
#        
#        # Verificar que se haya capturado una pieza y haya lanzado una excepción
#        self.main.chess.__board__.capture_piece.assert_called_once_with(1, 1, 2, 2)
#        
#        # Verificar que se haya mostrado el mensaje de error
#        mock_print.assert_any_call("Error:", "No hay pieza para mover")
#        mock_print.assert_any_call("Proba de nuevo", "sigue siendo el turno de ", self.main.chess.__turn__)




