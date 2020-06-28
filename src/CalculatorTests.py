import unittest

from Calculator import Calculator
from CsvReader import CsvReader

## TESTING CALCUATOR CLASS
# Verifying constructor, add, subtract, divide, multiply, square, square root operations.
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader("Tests/Data/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)



    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(8), 64)
        self.assertEqual(self.calculator.result, 64)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(64), 8)
        self.assertEqual(self.calculator.result, 8)

if __name__ == '__main__':
    unittest.main()
