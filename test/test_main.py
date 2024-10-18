import unittest
from unittest.mock import patch, MagicMock
from game.chess import Chess
from game.main import Cli
import io
import sys
from game.board import Board
from game.exceptions import InvalidPosition, NotPermitedMove, NotPieceToMove, NotPieceToReplace
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
            "----------------------Bienvenido a mi Ajedrez por Juan Martin Valverde----------------------\n"
            "----------------------------Consultor Tecnico: Copilot and GPT-4----------------------------\n"
            "------------------------Proyecto Para ComputacionI Ing informaticaUM------------------------\n"
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
        
    @patch('builtins.print')
    def test_main_menu2(self, mock_print):
        self.cli.main_menu2()
        mock_print.assert_any_call("------------------------------------------Opciones---------------------------------------------")
        mock_print.assert_any_call("Presiona 1 para continuar jugando")
        mock_print.assert_any_call("Presiona 2 para ver un tutorial")
        mock_print.assert_any_call("Presiona 3 dos veces(por separado) para terminar para salir")
        mock_print.assert_any_call("-----------------------------------------------------------------------------------------------")


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
        
class TestClientFunctions(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()  # Instancia de la clase Cli

    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    @patch.object(Cli, 'play_game')
    def test_client_play_game(self, mock_play_game, mock_main_menu1, mock_welcome_message, mock_input):
        self.cli.client()
        mock_welcome_message.assert_called_once()
        mock_main_menu1.assert_called_once()
        mock_play_game.assert_called_once()

    @patch('builtins.input', side_effect=['2', '3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    @patch.object(Cli, 'show_tutorial')
    def test_client_show_tutorial(self, mock_show_tutorial, mock_main_menu1, mock_welcome_message, mock_input):
        self.cli.client()
        mock_welcome_message.assert_called_once()
        self.assertEqual(mock_main_menu1.call_count, 2)
        mock_show_tutorial.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    def test_client_exit(self, mock_main_menu1, mock_welcome_message, mock_input):
        self.cli.client()
        mock_welcome_message.assert_called_once()
        mock_main_menu1.assert_called_once()


    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Cli, 'verify_move', return_value=(0, 0))
    @patch.object(Cli, 'validate_range', return_value=(1, 1))
    @patch.object(Cli, 'execute_move')
    @patch.object(Cli, 'main_menu2')
    @patch.object(Cli, 'handle_secondary_menu', return_value='3')
    @patch.object(Board, 'show_board')
    @patch.object(Chess, 'verify_winner', return_value=False)
    def test_play_game(self, mock_verify_winner, mock_show_board, mock_handle_secondary_menu, mock_main_menu2, mock_execute_move, mock_validate_range, mock_verify_move, mock_input):
        self.cli.play_game()
        mock_show_board.assert_called()
        mock_verify_move.assert_called_once_with(self.cli.chess)
        mock_validate_range.assert_called_once()
        mock_execute_move.assert_called_once_with(0, 0, 1, 1)
        mock_main_menu2.assert_called_once()
        mock_handle_secondary_menu.assert_called_once()


    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Board, 'capture_piece', return_value="Captured")
    @patch.object(Chess, 'movement_fits')
    @patch.object(Chess, 'change_pawn')
    @patch.object(Board, 'show_board')
    @patch.object(Chess, 'STR_captured_pieces', return_value="Captured pieces")
    def test_execute_move(self, mock_STR_captured_pieces, mock_show_board, mock_change_pawn, mock_movement_fits, mock_capture_piece, mock_input):
        self.cli.execute_move(0, 0, 1, 1)
        mock_capture_piece.assert_called_once_with(0, 0, 1, 1)
        mock_movement_fits.assert_called_once_with(0, 0, 1, 1)
        mock_change_pawn.assert_called_once_with(0, 0, 1, 1)
        mock_show_board.assert_called_once()
        mock_STR_captured_pieces.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Chess, 'change_turn')
    def test_handle_secondary_menu(self, mock_change_turn, mock_input):
        self.cli.handle_secondary_menu()
        mock_change_turn.assert_called_once()
        self.assertEqual(mock_input.call_count, 1)



    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    @patch.object(Cli, 'play_game')
    def test_client_play_game(self, mock_play_game, mock_main_menu1, mock_welcome_message, mock_input):
        self.cli.client()
        mock_welcome_message.assert_called_once()
        mock_main_menu1.assert_called_once()
        mock_play_game.assert_called_once()

    @patch('builtins.input', side_effect=['2', '3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    @patch.object(Cli, 'show_tutorial')
    def test_client_show_tutorial(self, mock_show_tutorial, mock_main_menu1, mock_welcome_message, mock_input):
        self.cli.client()
        mock_welcome_message.assert_called_once()
        self.assertEqual(mock_main_menu1.call_count, 2)
        mock_show_tutorial.assert_called_once()

    @patch('builtins.input', side_effect=['3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    def test_client_exit(self, mock_main_menu1, mock_welcome_message, mock_input):
        with patch('builtins.print') as mock_print:
            self.cli.client()
            mock_welcome_message.assert_called_once()
            mock_main_menu1.assert_called_once()
            mock_print.assert_any_call("Fin del juego")

    @patch('builtins.input', side_effect=['4', '3'])
    @patch.object(Cli, 'welcome_message')
    @patch.object(Cli, 'main_menu1')
    def test_client_invalid_option(self, mock_main_menu1, mock_welcome_message, mock_input):
        with patch('builtins.print') as mock_print:
            self.cli.client()
            mock_welcome_message.assert_called_once()
            mock_main_menu1.assert_called_once()
            mock_print.assert_any_call("Opcion invalida")
            mock_print.assert_any_call("Fin del juego")

    @patch('builtins.input', side_effect=['1'])
    def test_handle_secondary_menu_change_turn(self, mock_input):
        with patch.object(self.cli.chess, 'change_turn') as mock_change_turn:
            with patch('builtins.print') as mock_print:
                result = self.cli.handle_secondary_menu()
                mock_change_turn.assert_called_once()
                mock_print.assert_any_call("Es turno de: ", self.cli.chess.__turn__)
                self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['2', '3'])
    @patch.object(Cli, 'show_tutorial')
    @patch.object(Cli, 'main_menu2')
    def test_handle_secondary_menu_show_tutorial(self, mock_main_menu2, mock_show_tutorial, mock_input):
        result = self.cli.handle_secondary_menu()
        mock_show_tutorial.assert_called_once()
        mock_main_menu2.assert_called_once()
        self.assertEqual(result, '3')

    @patch('builtins.input', side_effect=['3'])
    def test_handle_secondary_menu_exit(self, mock_input):
        result = self.cli.handle_secondary_menu()
        self.assertEqual(result, '3')

    @patch('builtins.input', side_effect=['4', '3'])
    def test_handle_secondary_menu_invalid_option(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = self.cli.handle_secondary_menu()
            mock_print.assert_any_call("Opcion invalida")
            self.assertEqual(result, '3')

#class TestVerifyMove(unittest.TestCase):
#    def setUp(self):
#        self.cli = Cli()
#        self.chess = Chess()
#        self.cli.chess = self.chess
#
#    @patch('builtins.input', side_effect=['1', '2'])
#    @patch.object(Cli, 'verify_color', return_value=True)
#    @patch.object(Board, 'piece_to_STR', return_value="Knight")
#    @patch.object(Chess, 'error_out_of_range')
#    def test_verify_move_valid(self, mock_error_out_of_range, mock_piece_to_STR, mock_verify_color, mock_input):
#        from_row, from_col = self.cli.verify_move(self.chess)
#        self.assertEqual((from_row, from_col), (1, 2))
#        mock_error_out_of_range.assert_called_once_with(1, 2)
#        mock_piece_to_STR.assert_called_once_with(1, 2)
#        mock_verify_color.assert_called_once_with(self.chess, 1, 2)
#
#    @patch('builtins.input', side_effect=['a', '1', '2'])
#    def test_verify_move_invalid_input(self, mock_input):
#        with patch('builtins.print') as mock_print:
#            self.cli.verify_move(self.chess)
#            mock_print.assert_any_call("Flasehaste, mete un numero")
#
#    @patch('builtins.input', side_effect=['1', '2', '1', '2'])
#    @patch.object(Chess, 'error_out_of_range', side_effect=InvalidPosition("Invalid position"))
#    def test_verify_move_invalid_position(self, mock_error_out_of_range, mock_input):
#        with patch('builtins.print') as mock_print:
#            self.cli.verify_move(self.chess)
#            mock_print.assert_any_call("Invalid position")
#
#    @patch('builtins.input', side_effect=['1', '2', '1', '2'])
#    @patch.object(Cli, 'verify_color', return_value=False)
#    @patch.object(Board, 'piece_to_STR', return_value="Knight")
#    def test_verify_move_invalid_color(self, mock_piece_to_STR, mock_verify_color, mock_input):
#        with patch('builtins.print') as mock_print:
#            self.cli.verify_move(self.chess)
#            mock_verify_color.assert_called_once_with(self.chess, 1, 2)
#            mock_print.assert_any_call("Invalid option")
#
class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.chess = Chess()
        self.cli.chess.__board__ = MagicMock()

    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Cli, 'verify_move', return_value=(0, 0))
    @patch.object(Cli, 'validate_range', return_value=(1, 1))
    @patch.object(Cli, 'execute_move')
    @patch.object(Cli, 'main_menu2')
    @patch.object(Cli, 'handle_secondary_menu', return_value='3')
    def test_play_game_normal_flow(self, mock_handle_secondary_menu, mock_main_menu2, mock_execute_move, mock_validate_range, mock_verify_move, mock_input):
        self.cli.chess.__board__.show_board = MagicMock()
        self.cli.chess.verify_winner = MagicMock(return_value=False)
        self.cli.play_game()
        self.cli.chess.__board__.show_board.assert_called()
        mock_verify_move.assert_called_once_with(self.cli.chess)
        mock_validate_range.assert_called_once()
        mock_execute_move.assert_called_once_with(0, 0, 1, 1)
        mock_main_menu2.assert_called_once()
        mock_handle_secondary_menu.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3'])
    @patch.object(Cli, 'verify_move', return_value=(0, 0))
    @patch.object(Cli, 'validate_range', return_value=(1, 1))
    @patch.object(Cli, 'execute_move')
    @patch.object(Cli, 'main_menu2')
    @patch.object(Cli, 'handle_secondary_menu', return_value='3')
    def test_play_game_with_winner(self, mock_handle_secondary_menu, mock_main_menu2, mock_execute_move, mock_validate_range, mock_verify_move, mock_input):
        self.cli.chess.__board__.show_board = MagicMock()
        self.cli.chess.verify_winner = MagicMock(return_value="Winner")
        with patch('builtins.print') as mock_print:
            self.cli.play_game()
            self.cli.chess.__board__.show_board.assert_called()
            mock_verify_move.assert_called_once_with(self.cli.chess)
            mock_validate_range.assert_called_once()
            mock_execute_move.assert_called_once_with(0, 0, 1, 1)
            mock_print.assert_any_call("Winner")
            mock_print.assert_any_call("Fin del juego")

class TestValidateRange(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.chess = MagicMock(spec=Chess)

    @patch('builtins.input', side_effect=['3', '4'])
    def test_validate_range_valid(self, mock_input):
        to_row, to_col = self.cli.validate_range()
        self.assertEqual((to_row, to_col), (3, 4))
        self.cli.chess.error_out_of_range.assert_called_once_with(3, 4)

    @patch('builtins.input', side_effect=['a', '3', '4'])
    def test_validate_range_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            to_row, to_col = self.cli.validate_range()
            mock_print.assert_any_call("Flasheaste, mete un numero.")
            self.assertEqual((to_row, to_col), (3, 4))
            self.cli.chess.error_out_of_range.assert_called_once_with(3, 4)


