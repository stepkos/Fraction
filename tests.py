import unittest
from functions import *
from fraction import *


class FunctionsTests(unittest.TestCase):
    def test_nwd1(self):
        self.assertEqual(NWD(12, 18), 6)

    def test_nwd2(self):
        self.assertEqual(NWD(0, 321), 321)

    def test_nww1(self):
        self.assertEqual(NWW(3, 6), 6)

    def test_nww2(self):
        self.assertEqual(NWW(12, 18), 36)


class FractionTests(unittest.TestCase):
    def test_init1(self):
        f1 = Fraction()
        self.assertEqual(str(f1), '1/1')

    def test_inti2(self):
        f1 = Fraction(2, 5)
        self.assertEqual(str(f1), '2/5')

    def test_properties(self):
        f1 = Fraction()
        f1.num = 21
        f1.den = 85
        self.assertEqual(f1.num, 21)
        self.assertEqual(f1.den, 85)

    def test_den_setter_0_dev(self):
        self.assertRaises(ZeroDivisionError, Fraction, 5, 0)


if __name__ == '__main__':
    unittest.main()
