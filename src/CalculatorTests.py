import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

## Part 1 - Subtraction
    def test_subtraction_calulator(self):
        print("Start Subtraction test")
        self.assertEqual(self.calculator.subtract(2, 4), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

## Part 2 - Addition
    def test_addition_calulator(self):
        print("Start addition test")
        self.assertEqual(self.calculator.add(4, 4), 8)
        self.assertEqual(self.calculator.result, 8)
        test_data = CsvReader('/src/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

## Part 3 - Multiplcation
    def test_multiplication_calulator(self):
        print("Start Multiplication test")
        self.assertEqual(self.calculator.multiply(4, 4), 16)
        self.assertEqual(self.calculator.result, 16)
        test_data = CsvReader('/src/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

## Part 4 - Divide
    def test_division_calulator(self):
        print("Start Divide test")
        self.assertEqual(self.calculator.divide(4, 4), 1)
        self.assertEqual(self.calculator.result, 1)
        test_data = CsvReader('/src/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

## Part 5 - Square
    def test_square_calulator(self):
        print("Start Square test")
        self.assertEqual(self.calculator.square(4), 16)
        self.assertEqual(self.calculator.result, 16)
        test_data = CsvReader('/src/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

## Part 6 - Square Root
    def test_sqrt_calulator(self):
        print("Start Square Root test")
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('/src/sqrt2.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()