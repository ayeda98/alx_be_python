import unittest
from simple_calculator import SimpleCalculator

class test(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, 1), -3)
        self.assertEqual(self.calc.add(9, 3), 12)
        # Add more assertions to thoroughly test the add method.
def test_substract(self):
        """Test the substract method."""
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(3, 8), -5)
        self.assertEqual(self.calc.subtract(1, 1), 0)
def test_multiply(self):
        """Test the substract method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(5, -3), -15)
def test_divide(self):
        """Test the substract method.""" 
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(5, 2), 2,5)
        self.assertEqual(self.calc.divide(5, 0), "ErrorZeroDivision")
        

# Remember to write additional test methods for subtract, multiply, and divide.