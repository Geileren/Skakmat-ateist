import tkinter
from tkinter import *
#from PIL import Image, ImageTk
import sys
class Felt():
    def __init__(self, root, bræt, billede, x, y, brikker):
        self.brikker = brikker
        self.bræt = bræt
        self.brik = billede
        self.x = x
        self.y = y
        self.button = Button(root, image=self.brik, command=self.tryk)


    def check_farve(self):
        if (self.x + self.y) % 2 == 0:
            if self.brikker.index(self.brik) % 2 != 0:
                self.skift(self.brikker[self.brikker.index(self.brik) - 1])

            else:
                pass
        else:
            if self.brikker.index(self.brik) % 2 != 1:
                self.skift(self.brikker[self.brikker.index(self.brik) + 1])
            else:
                pass


    def skift(self, billede):
        self.brik = billede
        self.button.config(image=self.brik)

    def grid(self, x, y):
        self.button.grid(column=x, row=y)

    def tryk(self):
        if self.bræt.flyt_brik == False:
            self.bræt.flyt_brik = True
            self.bræt.nuværende_brik = self.brik
            self.bræt.flyt_brik_pos = self.x, self.y
            self.bræt.eks_felt = self
            self.button.config(relief="sunken", bg="yellow")
        elif self.bræt.flyt_brik == True:
            if self.x == self.bræt.flyt_brik_pos[0] and self.y == self.bræt.flyt_brik_pos[1]:
                self.bræt.flyt_brik = False
                self.bræt.eks_felt = ""
                self.button.config(relief="raised", bg="white")
            else:
                #begynd flyt, skal snakke med logik

                self.skift(self.bræt.nuværende_brik)
                self.check_farve()
                self.bræt.tøm_felt()


    def tøm(self):
        self.bræt.flyt_brik = False
        self.skift(self.brikker[12])
        self.check_farve()
        self.button.config(relief="raised", bg="white")





class Bræt:

    def __init__(self, root, brækker):
        self.root = root
        self.brækker = brækker
        self.tildel_billeder(self.brækker)
        self.gen_start_lister()
        self.table_fields = []
        self.flyt_brik = False
        self.nuværende_brik = ""
        self.flyt_brik_pos = ""
        self.eks_felt = ""

    def tøm_felt(self):
        self.eks_felt.tøm()

    def gen_start_lister(self):
        self.sort_start = [self.sort_tårn_lys, self.sort_springer_mørk, self.sort_løber_lys, self.sort_dronning_mørk, self.sort_konge_lys, self.sort_løber_mørk, self.sort_springer_lys, self.sort_tårn_mørk]
        # liste svarrende til startpositionen for sorte brækker på række 8
        self.hvid_start = [self.hvid_tårn_mørk, self.hvid_springer_lys, self.hvid_løber_mørk, self.hvid_dronning_lys, self.hvid_konge_mørk, self.hvid_løber_lys, self.hvid_springer_mørk, self.hvid_tårn_lys]
        # liste svarrende til startpositionen for sorte brækker på række 1
        self.sort_start_bønder = self.sort_bonde_lys, self.sort_bonde_mørk

        self.hvid_start_bønder = self.hvid_bonde_mørk, self.hvid_bonde_lys

    def tildel_billeder(self, brikker):
        self.sort_bonde_mørk = brikker[0]
        self.sort_bonde_lys = brikker[1]

        self.sort_løber_mørk = brikker[2]
        self.sort_løber_lys = brikker[3]

        self.sort_springer_mørk = brikker[4]
        self.sort_springer_lys = brikker[5]

        self.sort_tårn_mørk = brikker[6]
        self.sort_tårn_lys = brikker[7]

        self.sort_konge_mørk = brikker[8]
        self.sort_konge_lys = brikker[9]

        self.sort_dronning_mørk = brikker[10]
        self.sort_dronning_lys = brikker[11]

        self.tom_mørk = brikker[12]
        self.tom_lys = brikker[13]

        self.hvid_bonde_mørk = brikker[14]
        self.hvid_bonde_lys = brikker[15]

        self.hvid_løber_mørk = brikker[16]
        self.hvid_løber_lys = brikker[17]

        self.hvid_springer_mørk = brikker[18]
        self.hvid_springer_lys = brikker[19]

        self.hvid_tårn_mørk = brikker[20]
        self.hvid_tårn_lys = brikker[21]

        self.hvid_konge_mørk = brikker[22]
        self.hvid_konge_lys = brikker[23]

        self.hvid_dronning_mørk = brikker[24]
        self.hvid_dronning_lys = brikker[25]

    def lav(self):
        for y in range(1,9):
            for x in range(1,9):
                if y == 1:# tegner alle startbrækkerne i række 1
                    self.table_fields.append(Felt(self.root, self, self.hvid_start[x-1], x, y, self.brækker))

                elif y == 2:
                    self.table_fields.append(Felt(self.root, self, self.hvid_start_bønder[x%2], x, y, self.brækker))

                elif y == 7:
                    self.table_fields.append(Felt(self.root, self, self.sort_start_bønder[x%2], x, y, self.brækker))

                elif y == 8:# tegner alle startbrækkerne i række 8
                    self.table_fields.append(Felt(self.root, self, self.sort_start[x - 1], x, y, self.brækker))

                elif (y + x) % 2 == 0: #tegner alle tomme mørke felter
                    self.table_fields.append(Felt(self.root, self, self.tom_mørk, x, y, self.brækker))

                else: # tegner de sidste felter, altså tomme lyse
                    self.table_fields.append(Felt(self.root, self, self.tom_lys, x, y, self.brækker))

                self.table_fields[len(self.table_fields) - 1].grid(x, y)
                # gridder knappen ud fra tilhørende koordinater






def gen_picts(path, size): #importere og subsampler alle billederne
    brikker = []
    sort_bonde_mørk = PhotoImage(file=rf"{path}\Assets\sort_bonde_mørk.png")
    brikker.append(sort_bonde_mørk.subsample(size, size))

    sort_bonde_lys = PhotoImage(file=rf"{path}\Assets\sort_bonde_lys.png")
    brikker.append(sort_bonde_lys.subsample(size, size))

    sort_løber_mørk = PhotoImage(file=rf"{path}\Assets\sort_løber_mørk.png")
    brikker.append(sort_løber_mørk.subsample(size, size))

    sort_løber_lys = PhotoImage(file=rf"{path}\Assets\sort_løber_lys.png")
    brikker.append(sort_løber_lys.subsample(size, size))

    sort_springer_mørk = PhotoImage(file=rf"{path}\Assets\sort_springer_mørk.png")
    brikker.append(sort_springer_mørk.subsample(size, size))

    sort_springer_lys = PhotoImage(file=rf"{path}\Assets\sort_springer_lys.png")
    brikker.append(sort_springer_lys.subsample(size, size))

    sort_tårn_mørk = PhotoImage(file=rf"{path}\Assets\sort_tårn_mørk.png")
    brikker.append(sort_tårn_mørk.subsample(size, size))

    sort_tårn_lys = PhotoImage(file=rf"{path}\Assets\sort_tårn_lys.png")
    brikker.append(sort_tårn_lys.subsample(size, size))

    sort_konge_mørk = PhotoImage(file=rf"{path}\Assets\sort_konge_mørk.png")
    brikker.append(sort_konge_mørk.subsample(size, size))

    sort_konge_lys = PhotoImage(file=rf"{path}\Assets\sort_konge_lys.png")
    brikker.append(sort_konge_lys.subsample(size, size))

    sort_dronning_mørk = PhotoImage(file=rf"{path}\Assets\sort_dronning_mørk.png")
    brikker.append(sort_dronning_mørk.subsample(size, size))

    sort_dronning_lys = PhotoImage(file=rf"{path}\Assets\sort_dronning_lys.png")
    brikker.append(sort_dronning_lys.subsample(size, size))

    tom_mørk = PhotoImage(file=rf"{path}\Assets\tom_mørk.png")
    brikker.append(tom_mørk.subsample(size, size))

    tom_lys = PhotoImage(file=rf"{path}\Assets\tom_lys.png")
    brikker.append(tom_lys.subsample(size, size))

    hvid_bonde_mørk = PhotoImage(file=rf"{path}\Assets\hvid_bonde_mørk.png")
    brikker.append(hvid_bonde_mørk.subsample(size, size))

    hvid_bonde_lys = PhotoImage(file=rf"{path}\Assets\hvid_bonde_lys.png")
    brikker.append(hvid_bonde_lys.subsample(size, size))

    hvid_løber_mørk = PhotoImage(file=rf"{path}\Assets\hvid_løber_mørk.png")
    brikker.append(hvid_løber_mørk.subsample(size, size))

    hvid_løber_lys = PhotoImage(file=rf"{path}\Assets\hvid_løber_lys.png")
    brikker.append(hvid_løber_lys.subsample(size, size))

    hvid_springer_mørk = PhotoImage(file=rf"{path}\Assets\hvid_springer_mørk.png")
    brikker.append(hvid_springer_mørk.subsample(size, size))

    hvid_springer_lys = PhotoImage(file=rf"{path}\Assets\hvid_springer_lys.png")
    brikker.append(hvid_springer_lys.subsample(size, size))

    hvid_tårn_mørk = PhotoImage(file=rf"{path}\Assets\hvid_tårn_mørk.png")
    brikker.append(hvid_tårn_mørk.subsample(size, size))

    hvid_tårn_lys = PhotoImage(file=rf"{path}\Assets\hvid_tårn_lys.png")
    brikker.append(hvid_tårn_lys.subsample(size, size))

    hvid_konge_mørk = PhotoImage(file=rf"{path}\Assets\hvid_konge_mørk.png")
    brikker.append(hvid_konge_mørk.subsample(size, size))

    hvid_konge_lys = PhotoImage(file=rf"{path}\Assets\hvid_konge_lys.png")
    brikker.append(hvid_konge_lys.subsample(size, size))

    hvid_dronning_mørk = PhotoImage(file=rf"{path}\Assets\hvid_dronning_mørk.png")
    brikker.append(hvid_dronning_mørk.subsample(size, size))

    hvid_dronning_lys = PhotoImage(file=rf"{path}\Assets\hvid_dronning_lys.png")
    brikker.append(hvid_dronning_lys.subsample(size, size))


    return brikker

def main():
    root = Tk()
    path = sys.path[0]


    b = Bræt(root, gen_picts(path, 3))
    b.lav()
    mainloop()

main()

