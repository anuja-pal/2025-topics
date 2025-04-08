import unittest
from calculator_package import add_multiple_numbers, multiply_multiple_numbers

class TestCalculatorPackage(unittest.TestCase):
    def test_add_multiple_numbers(self):
        self.assertEqual(add_multiple_numbers(1,1),2)
        self.assertEqual(add_multiple_numbers(1,-1),0)
        self.assertEqual(add_multiple_numbers(-1,-1),-2)

    def test_multiply_multiple_numbers(self):
        self.assertEqual(multiply_multiple_numbers(1,1),1)
        self.assertEqual(multiply_multiple_numbers(1,-1),-1)
        self.assertEqual(multiply_multiple_numbers(-1,-1),1)


if __name__ == '__main__':
    unittest.main()