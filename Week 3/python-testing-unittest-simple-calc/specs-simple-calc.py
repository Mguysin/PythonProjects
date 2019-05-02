from simple_calc import SimpleCalc
import unittest


class Calc_test(unittest.TestCase):

    #Initiating a calculator object so we can test its behavior
    calc=SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6, 'You failed to get 6, adding 2+4')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2, 4))

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_calculator_initiated(self):
        self.assertIsInstance(self.calc, SimpleCalc, msg='Is it a calculator object')

