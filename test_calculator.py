import unittest
from calculator import parse_input, calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(parse_input("3+4")), 7)

    def test_subtraction(self):
        self.assertEqual(calculate(parse_input("10-2")), 8)

    def test_multiplication(self):
        self.assertEqual(calculate(parse_input("6*3")), 18)

    def test_division(self):
        self.assertEqual(calculate(parse_input("8/2")), 4)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate(parse_input("3&4"))

if __name__ == '__main__':
    unittest.main()
