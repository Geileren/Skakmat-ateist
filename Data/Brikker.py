


class Brik:
    def __init__(self, hold, type, billede, kandræbes=False):
        self.hold = hold
        self.type = type
        self.kandræbes = kandræbes
        self.billede = billede


sb = Brik("s", "b", "sort_bonde.noget")
hb = Brik("h", "b", "hvid_bonde.noget")
sk = Brik("s", "k", "sort_konge.noget")
hk = Brik("h", "k", "hvid_konge.noget")
st = Brik("s", "t", "sort_tårn.noget")
ht = Brik("h", "t", "hvid_tårn.noget")
ss = Brik("s", "s", "sort_springer.noget")
hs = Brik("h", "s", "hvid_springer.noget")
sd = Brik("s", "d", "Sort_dronning.noget")
hd = Brik("h", "d", "Hvid_dronning.noget")
sl = Brik("s", "l", "Sort_løber.noget")
hl = Brik("h", "l", "Hvid_løber.noget")
