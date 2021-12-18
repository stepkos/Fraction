import unittest
from fraction import Fraction


class FractionTests(unittest.TestCase):
    def test_gcd1(self):
        self.assertEqual(Fraction.gcd(12, 18), 6)

    def test_gcd2(self):
        self.assertEqual(Fraction.gcd(0, 321), 321)

    def test_lcm1(self):
        self.assertEqual(Fraction.lcm(3, 6), 6)

    def test_lcm2(self):
        self.assertEqual(Fraction.lcm(12, 18), 36)

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
