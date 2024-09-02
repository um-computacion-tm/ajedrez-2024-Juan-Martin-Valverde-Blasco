import unittest
from unittest.mock import patch, call, MagicMock
from io import StringIO
from game.main import Cli, Chess


class TestMain(unittest.TestCase):  

    def test_main(self):
        instance = Cli()
        instance.play = MagicMock()
        instance.main()
        instance.play.assert_called_once()

    @patch('builtins.print')
    @patch ('builtins.input', side_effect = ["e"])

    def test_play_error(self,patched_print, mock_input):
        cli = Cli()
        cli.play()

        self.assertEqual(cli.play(), "error")
    @patch('builtins.input', side_effect=["1", "2"])
    @patch('builtins.print')
    def test_verify_move_correct(self, mock_print, mock_input):
        cli = Cli()
        chess_mock = MagicMock()
        chess_mock.__board__ = MagicMock()
        chess_mock.__board__.get_piece.return_value = "Knight"
        chess_mock.move_correct_color.return_value = None

        from_row, from_col = cli.verify_move(chess_mock)

        self.assertEqual(from_row, 1)
        self.assertEqual(from_col, 2)
        chess_mock.__board__.get_piece.assert_called_once_with(1, 2)
        chess_mock.move_correct_color.assert_called_once_with(1, 2)
        mock_print.assert_any_call("La pieza que elegiste es: ", "Knight")

    @patch('builtins.input', side_effect=["1", "2", "3", "4"])
    @patch('builtins.print')
    def test_verify_move_incorrect_then_correct(self, mock_print, mock_input):
        cli = Cli()
        chess_mock = MagicMock()
        chess_mock.__board__ = MagicMock()
        chess_mock.__board__.get_piece.side_effect = ["Knight", "Bishop"]
        chess_mock.move_correct_color.side_effect = ["Wrong color", None]

        from_row, from_col = cli.verify_move(chess_mock)

        self.assertEqual(from_row, 3)
        self.assertEqual(from_col, 4)
        self.assertEqual(chess_mock.__board__.get_piece.call_count, 2)
        self.assertEqual(chess_mock.move_correct_color.call_count, 2)
        mock_print.assert_any_call("La pieza que elegiste es: ", "Knight")
        mock_print.assert_any_call("Wrong color")
        mock_print.assert_any_call("La pieza que elegiste es: ", "Bishop")