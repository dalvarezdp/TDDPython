import unittest

from calculator import Calculator, CalculatorSyntaxError


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

    def test_subtract_no_commutative_property(self):
        result_a = self.calculator.subtract(1, 6)
        result_b = self.calculator.subtract(6, 1)
        self.assertNotEqual(result_a, result_b)

    def test_eval_add_4_6(self):
        result = self.calculator.eval("4 + 6")
        self.assertEqual(result, 10)

    def test_eval_add_6_6(self):
        result = self.calculator.eval("6 + 6")
        self.assertEqual(result, 12)

    def test_eval_multiple_operations(self):
        result = self.calculator.eval("6 + 5 - 3 - 10 + 20")
        self.assertEqual(result, 18)

    def test_parse_add_4_6(self):
        result = self.calculator.parse("4 + 6")
        self.assertEqual(result, [4, "+", 6])

    def test_parse_add_6_6(self):
        result = self.calculator.parse("6 + 6")
        self.assertEqual(result, [6, "+", 6])

    def test_parse_add_1_2_3(self):
        result = self.calculator.parse("1 + 2 + 3")
        self.assertEqual(result, [1, "+", 2, "+", 3])

    def test_parse_subtract_1_6(self):
        result = self.calculator.parse("1 - 6")
        self.assertEqual(result, [1, "-", 6])

    def test_bad_expression_syntax_with_two_operators_raises_exception(self):
        with self.assertRaises(CalculatorSyntaxError):
            self.calculator.parse("1 + + 5")

    def test_bad_expression_syntax_with_unknown_item_raises_exception(self):
        with self.assertRaises(CalculatorSyntaxError):
            self.calculator.parse("1 + alberto")

    def test_bad_expression_syntax_with_two_numbers_without_operator_between(self):
        with self.assertRaises(CalculatorSyntaxError):
            self.calculator.parse("1 + 2 3")

    def test_bad_expression_syntax_with_unknown_operator(self):
        with self.assertRaises(CalculatorSyntaxError):
            self.calculator.parse("1 menos 2")


# comprueba si se está ejecutando directamente este archivo con el comando: python tests.py y de ser así, arranca los test
if __name__ == "__main__":
    unittest.main()
