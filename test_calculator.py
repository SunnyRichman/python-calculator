import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(4, 8), 12)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 4), 2)
        self.assertEqual(self.calc.subtract(4, 8), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(4, 8), 32)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(8, 4), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(18, 8), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()