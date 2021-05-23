from Data.Brikker import *
import unittest

class Testafdatalag(unittest.TestCase):

    def test1(self):
        a = Braet
        b = lav_braet(Braet)
        self.assertEqual(len(a), len(b))

    def test2(self):
        a = Braet[0]
        b = Braet
        self.assertIn(a, b)

    def test3(self):
        lav_braet(Braet)
        self.assertIsNotNone(Braet[1][6])

    def test4(self):
        a = Brik('s', 't')
        self.assertIs(a.hold, 's')
        self.assertIsNot(a.type, 'k')
        self.assertFalse(a.kandræbes)


if __name__ == "__main__":
    unittest.main()


