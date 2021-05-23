from Logik.moveslikejagger import *
import unittest

class testaflogiklag(unittest.TestCase):

    def test1(self):
        reset_Braet(Braet)
        x = 1
        y = 4
        pos = x,y
        bonde_traek_s(pos)
        self.assertEqual(len(fremhaev(Braet)), 2)

    def test2(self):
        reset_Braet(Braet)
        x = 6
        y = 4
        pos = x,y
        bonde_traek_h(pos)
        self.assertEqual(len(fremhaev(Braet)), 2)

    def test3(self):
        reset_Braet(Braet)
        x = 4
        y = 4
        pos = x,y
        taarn_traek(pos)
        self.assertEqual(len(fremhaev(Braet)), 14)

    def test4(self):
        reset_Braet(Braet)
        x = 4
        y = 4
        pos = x,y
        lober_traek(pos)
        self.assertEqual(len(fremhaev(Braet)), 13)

    def test5(self):
        reset_Braet(Braet)
        x = 4
        y = 4
        pos = x,y
        konge_traek(pos)
        self.assertEqual(len(fremhaev(Braet)), 9)

    def test6(self):
        reset_Braet(Braet)
        x = 4
        y = 4
        pos = x, y
        dronning_traek(pos)
        self.assertEqual(len(fremhaev(Braet)), 27)

    def test7(self):
        reset_Braet(Braet)
        x = 4
        y = 4
        pos = x, y
        springer_traek(pos)
        self.assertEqual(len(fremhaev(Braet)), 8)



if __name__ == "__main__":
    unittest.main()