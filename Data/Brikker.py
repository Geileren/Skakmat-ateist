Braet = [[' ' for i in range(8)] for i in range(8)]

#Laver en klasse til brikkerne som viser hvilket hold, type og om den kan dræbes eller ej
class Brik:
    def __init__(self, hold, type, kandræbes=False):
        self.hold = hold
        self.type = type
        self.kandræbes = kandræbes


def lav_braet(Braet):
    Braet[0] = [Brik("s", "t"), Brik("s", "s"), Brik("s", "l"), Brik("s", "d"), Brik("s", "k"), Brik("s", "l"), Brik("s", "s"), Brik("s", "t")]
    Braet[7] = [Brik("h", "t"), Brik("h", "s"), Brik("h", "l"), Brik("h", "d"), Brik("h", "k"), Brik("h", "l"), Brik("h", "s"), Brik("h", "t")]

    for i in range(8):
        Braet[1][i] = Brik("s", "b")
        Braet[6][i] = Brik("h", "b")
    return Braet

