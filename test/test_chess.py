import unittest
from game.chess import ChessClass1, ChessClass2  

class TestChessClass1(unittest.TestCase):
    def setUp(self):
        self.instance = ChessClass1()

    def test_initial_state(self):
        # Verifica el estado inicial
        self.assertEqual(self.instance.some_attribute, expected_value)  # Reemplaza con atributos y valores reales

    def test_some_method(self):
        # Verifica el comportamiento de algún método
        result = self.instance.some_method()
        self.assertEqual(result, expected_result)  

class TestChessClass2(unittest.TestCase):
    def setUp(self):
        self.instance = ChessClass2()

    def test_initial_state(self):
        # Verifica el estado inicial
        self.assertEqual(self.instance.some_attribute, expected_value)  

    def test_some_method(self):
        # Verifica el comportamiento de algún método
        result = self.instance.some_method()
        self.assertEqual(result, expected_result)  

    

if __name__ == '__main__':
    unittest.main()