import unittest

from calculator import Calculator


class TestsCalculator(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta siempre antes de cada test
        """
        self.calculator = Calculator()

    def tearDown(self):
        """
        Se ejecuta siempre después de cada test
        """
        self.calculator = None

    def test_add_1_2(self):
        result = self.calculator.add(1, 2)  # 1 + 2 =  3
        self.assertEqual(result, 3)

    def test_add_5_5(self):
        result = self.calculator.add(5, 5)  # 5 + 5 = 10
        self.assertEqual(result, 10)

    def test_add_commutative_property(self):
        result_a = self.calculator.add(3, 4)
        result_b = self.calculator.add(4, 3)
        self.assertEqual(result_a, result_b)

    def test_subtract_1_6(self):
        result = self.calculator.subtract(1, 6)  # 1 - 6 = -5
        self.assertEqual(result, -5)


# comprueba si se está ejecutando directamente este archivo con el comando: python tests.py y de ser así, arranca los test
if __name__ == "__main__":
    unittest.main()
