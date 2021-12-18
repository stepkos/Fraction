import unittest
import functions as fn


class FunctionsTests(unittest.TestCase):
    def test_nwd1(self):
        self.assertEqual(fn.NWD(12, 18), 6)

    def test_nwd2(self):
        self.assertEqual(fn.NWD(0, 321), 321)

    def test_nww1(self):
        self.assertEqual(fn.NWW(3, 6), 6)

    def test_nww2(self):
        self.assertEqual(fn.NWW(12, 18), 36)


class FractionTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
