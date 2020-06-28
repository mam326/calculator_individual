import unittest

from Calculator import Calculator
from CsvReader import getFileData

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
        print("starting addition test")
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = getFileData("/src/addition.csv")
        for row in test_data:
            print(row)
            value1 = int(row[0])
            value2 = int(row[1])
            result = int(row[2])
            self.assertEqual(self.calculator.add(value1, value2), result)
            self.assertEqual(self.calculator.result, result)



    def test_subtract_method_calculator(self):
        print("starting subtraction test")
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)
        test_data = getFileData("/src/subtraction.csv")
        for row in test_data:
            value1 = int(row[0])
            value2 = int(row[1])
            result = int(row[2])
            self.assertEqual(self.calculator.subtract(value2, value1), result)
            self.assertEqual(self.calculator.result, result)


    def test_multiply_method_calculator(self):
        print("starting multiplication test")
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = getFileData("/src/multiplication.csv")
        for row in test_data:
            value1 = int(row[0])
            value2 = int(row[1])
            result = int(row[2])
            self.assertEqual(self.calculator.multiply(value2, value1), result)
            self.assertEqual(self.calculator.result, result)


    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = getFileData("/src/division.csv")
        for row in test_data:
            value1 = float(row[0])
            value2 = float(row[1])
            result = float(row[2])
            self.assertEqual(self.calculator.divide(value2, value1), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(8), 64)
        self.assertEqual(self.calculator.result, 64)
        test_data = getFileData("/src/square.csv")
        for row in test_data:
            value1 = int(row[0])
            result = int(row[1])
            self.assertEqual(self.calculator.square(value1), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(64), 8)
        self.assertEqual(self.calculator.result, 8)

if __name__ == '__main__':
    unittest.main()
