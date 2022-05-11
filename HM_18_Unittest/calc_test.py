import unittest
from calculator import Calculator


class Test_Calc(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_sum_int(self):
        self.assertEqual(self.calculator.sum(7, 10), 17)

    def test_positive_sum_float(self):
        self.assertEqual(self.calculator.sum(2.11, 1.89), 4)

    def test_positive_diff(self):
        self.assertEqual(self.calculator.diff(73, 13), 60)

    def test_positive_mult(self):
        self.assertEqual(self.calculator.mult(11, 3), 33)

    def test_positive_div(self):
        self.assertEqual(self.calculator.div(114, 3), 38)

    def test_negative_sum_int(self):
        self.assertNotEqual(self.calculator.sum(7, 10), 2)

    def test_negative_diff(self):
        self.assertNotEqual(self.calculator.diff(73, 13), 59)

    def test_negative_mult(self):
        self.assertNotEqual(self.calculator.mult(11, 3), 3)

    def test_negative_div(self):
        self.assertNotEqual(self.calculator.div(114, 3), 0)

    def test_error_mult_first(self):
        self.assertRaises(TypeError, self.calculator.mult(100, 'ffffffff'), 'aaa')

    def test_error_mult_second(self):
        self.assertRaises(TypeError, self.calculator.mult('abcabcabc', 100), 100)

    def test_error_div(self):
        self.assertRaises(ZeroDivisionError, self.calculator.div, 3, 0)


if __name__ == '__main__':
    unittest.main()
