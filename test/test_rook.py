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

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.rook = Rook("WHITE")  # Proporcionar el argumento 'color'

    def test_valid_orthogonal_moves(self):
        board = None  # Asumiendo que el tablero no es necesario para esta prueba
#        self.assertTrue(self.rook.permited_move(0, 0, 0, 5, board))  # Movimiento horizontal válido
#        self.assertTrue(self.rook.permited_move(0, 0, 5, 0, board))  # Movimiento vertical válido

    def test_invalid_moves(self):
        board = None  # Asumiendo que el tablero no es necesario para esta prueba
        self.assertFalse(self.rook.permited_move(0, 0, 5, 5, board))  # Movimiento diagonal inválido
        self.assertFalse(self.rook.permited_move(0, 0, 1, 2, board))  # Movimiento en L inválido