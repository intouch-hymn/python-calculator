import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 23), 33)
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(2, 2), 4)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 9), -7)
        self.assertEqual(self.calc.subtract(30, 85), -55)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,4), 12)
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(7, 7), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)
        self.assertEqual(self.calc.modulo(7, 1), 0)
if __name__ == '__main__':
    unittest.main()