import unittest
import calculator
class TestCalculator(unittest.TestCase):

    def test_add(self):
        '''Test case function for addition'''
        result = calculator.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_substract(self):
        '''Test case function for subtraction'''

        result = calculator.substract(10, 5)
        expected = 5
        self.assertEqual(result, expected)


    def test_mul(self):
        '''Test case function for multiplication'''
        result = calculator.multiply(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        result =calculator.divide(10, 2)
        expected = 5
        self.assertEqual(result, expected)

    def test_max(self):
        '''Test case function for max'''
        result = calculator.max(10, 2,7)
        expected = 10
        self.assertEqual(result, expected)
        result = calculator.max(2,10,7)
        expected = 10
        self.assertEqual(result, expected)
        result = calculator.max(2,7,10)
        expected = 10
        self.assertEqual(result, expected)