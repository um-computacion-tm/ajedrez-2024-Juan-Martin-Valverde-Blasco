import unittest
from game.pawn import Peon  

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.peon = Peon()

    def test_initial_state(self):
        # Verifica el estado inicial del peon
        self.assertEqual(self.peon.some_attribute, expected_value)  

    def test_some_method(self):
        # Verifica el comportamiento de algún método
        result = self.peon.some_method()
        self.assertEqual(result, expected_result)  

    

if __name__ == '__main__':
    unittest.main()