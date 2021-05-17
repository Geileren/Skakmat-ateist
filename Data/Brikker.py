Braet = [[' ' for i in range(8)]for i in range(8)]

#Laver en klasse til brikkerne som viser hvilket hold, type og om den kan dræbes eller ej
class Brik:
    def __init__(self, hold, type, kandræbes=False):
        self.hold = hold
        self.type = type
        self.kandræbes = kandræbes


sb = Brik("s", "b")
hb = Brik("h", "b")
sk = Brik("s", "k")
hk = Brik("h", "k")
st = Brik("s", "t")
ht = Brik("h", "t")
ss = Brik("s", "s")
hs = Brik("h", "s")
sd = Brik("s", "d")
hd = Brik("h", "d")
sl = Brik("s", "l")
hl = Brik("h", "l")

def lav_braet(braet):
    braet[0] = [Brik("s", "t"), Brik("s", "s"), Brik("s", "l"), Brik("s", "d"), Brik("s", "k"), Brik("s", "l"), Brik("s", "s"), Brik("s", "t")]
    braet[7] = [Brik("h", "t"), Brik("h", "s"), Brik("h", "l"), Brik("h", "d"), Brik("h", "k"), Brik("h", "l"), Brik("h", "s"), Brik("h", "t")]

    for i in range(8):
        braet[1][i] = Brik("s", "b")
        braet[6][i] = Brik("h", "b")
    return braet

