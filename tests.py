import unittest

from calculator import Calculator


class TestsCalculator(unittest.TestCase):

    """
    Se ejecuta siempre antes de cada test
    """
    def setUp(self):
        self.calculator = Calculator()


    """
    Se ejecuta siempre despues de cada test
    """
    def test_add_1_2(self):
        result = self.calculator.add(1, 2)   # 1 + 2
        self.assertEquals(result, 3)

    def test_add_5_5(self):
        result = self.calculator.add(5, 5)   # 5 + 5
        self.assertEquals(result, 10)

# comprueba si se está ejecutando directamente este archivo con el comando: python tests.py y de ser así, arranca los test
if __name__ == "__main__":
    unittest.main()
