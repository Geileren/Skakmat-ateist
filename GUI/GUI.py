import tkinter
from tkinter import *
#from PIL import Image, ImageTk
import sys

class test:

    def __init__(self, root, brækker):
        self.root = root

        self.tildel_billeder(brækker)
        self.table_fields = []

    def tildel_billeder(self, brækker):
        self.sort_bonde_mørk = brækker[0]
        self.sort_bonde_lys = brækker[1]

        self.sort_løber_mørk = brækker[2]
        self.sort_løber_lys = brækker[3]

        self.sort_springer_mørk = brækker[4]
        self.sort_springer_lys = brækker[5]

        self.sort_tårn_mørk = brækker[6]
        self.sort_tårn_lys = brækker[7]

        self.sort_konge_mørk = brækker[8]
        self.sort_konge_lys = brækker[9]

        self.sort_dronning_mørk = brækker[10]
        self.sort_dronning_lys = brækker[11]

        self.tom_mørk = brækker[12]
        self.tom_lys = brækker[13]

        self.hvid_bonde_mørk = brækker[14]
        self.hvid_bonde_lys = brækker[15]

        self.hvid_løber_mørk = brækker[16]
        self.hvid_løber_lys = brækker[17]

        self.hvid_springer_mørk = brækker[18]
        self.hvid_springer_lys = brækker[19]

        self.hvid_tårn_mørk = brækker[20]
        self.hvid_tårn_lys = brækker[21]

        self.hvid_konge_mørk = brækker[22]
        self.hvid_konge_lys = brækker[23]

        self.hvid_dronning_mørk = brækker[24]
        self.hvid_dronning_lys = brækker[25]

    def lav(self):

        for y in range(1,9):
            print(y)
            for x in range(1,9):
                if y == 1:
                    if x == 1:
                        self.table_fields.append(Button(self.root, image=self.sort_tårn_lys))

                    elif x == 2:
                        self.table_fields.append(Button(self.root, image=self.sort_springer_mørk))

                    elif x == 3:
                        self.table_fields.append(Button(self.root, image=self.sort_løber_lys))

                    elif x == 4:
                        self.table_fields.append(Button(self.root, image=self.sort_dronning_mørk))

                    elif x == 5:
                        self.table_fields.append(Button(self.root, image=self.sort_konge_lys))

                    elif x == 6:
                        self.table_fields.append(Button(self.root, image=self.sort_løber_mørk))

                    elif x == 7:
                        self.table_fields.append(Button(self.root, image=self.sort_springer_lys))

                    elif x == 8:
                        self.table_fields.append(Button(self.root, image=self.sort_tårn_mørk))
                    self.table_fields[len(self.table_fields) - 1].grid(column=x, row=y)
                elif y == 8:
                    if x == 1:
                        self.table_fields.append(Button(self.root, image=self.hvid_tårn_mørk))

                    elif x == 2:
                        self.table_fields.append(Button(self.root, image=self.hvid_springer_lys))

                    elif x == 3:
                        self.table_fields.append(Button(self.root, image=self.hvid_løber_mørk))

                    elif x == 4:
                        self.table_fields.append(Button(self.root, image=self.hvid_dronning_lys))

                    elif x == 5:
                        self.table_fields.append(Button(self.root, image=self.hvid_konge_mørk))

                    elif x == 6:
                        self.table_fields.append(Button(self.root, image=self.hvid_løber_lys))

                    elif x == 7:
                        self.table_fields.append(Button(self.root, image=self.hvid_springer_mørk))

                    elif x == 8:
                        self.table_fields.append(Button(self.root, image=self.hvid_tårn_lys))

                    self.table_fields[len(self.table_fields) - 1].grid(column=x, row=y)

                elif (y % 2 + x) % 2 == 0:
                    self.table_fields.append(Button(self.root, image=self.tom_lys))
                    self.table_fields[len(self.table_fields)-1].grid(column=x, row=y)
                    if y == 2:
                        self.table_fields[len(self.table_fields)-1].config(image=self.sort_bonde_mørk)
                    elif y == 7:
                        self.table_fields[len(self.table_fields) - 1].config(image=self.hvid_bonde_mørk)

                else:
                    self.table_fields.append(Button(self.root, image=self.tom_mørk))
                    self.table_fields[len(self.table_fields) - 1].grid(column=x, row=y)
                    if y == 2:
                        self.table_fields[len(self.table_fields)-1].config(image=self.sort_bonde_lys)
                    elif y == 7:
                        self.table_fields[len(self.table_fields) - 1].config(image=self.hvid_bonde_lys)






def gen_picts(path, size):
    brækker = []
    sort_bonde_mørk = PhotoImage(file=rf"{path}\Assets\sort_bonde_lys.png")
    brækker.append(sort_bonde_mørk.subsample(size, size))

    sort_bonde_lys = PhotoImage(file=rf"{path}\Assets\sort_bonde_mørk.png")
    brækker.append(sort_bonde_lys.subsample(size, size))

    sort_løber_mørk = PhotoImage(file=rf"{path}\Assets\sort_løber_mørk.png")
    brækker.append(sort_løber_mørk.subsample(size, size))

    sort_løber_lys = PhotoImage(file=rf"{path}\Assets\sort_løber_lys.png")
    brækker.append(sort_løber_lys.subsample(size, size))

    sort_springer_mørk = PhotoImage(file=rf"{path}\Assets\sort_springer_mørk.png")
    brækker.append(sort_springer_mørk.subsample(size, size))

    sort_springer_lys = PhotoImage(file=rf"{path}\Assets\sort_springer_lys.png")
    brækker.append(sort_springer_lys.subsample(size, size))

    sort_tårn_mørk = PhotoImage(file=rf"{path}\Assets\sort_tårn_mørk.png")
    brækker.append(sort_tårn_mørk.subsample(size, size))

    sort_tårn_lys = PhotoImage(file=rf"{path}\Assets\sort_tårn_lys.png")
    brækker.append(sort_tårn_lys.subsample(size, size))

    sort_konge_mørk = PhotoImage(file=rf"{path}\Assets\sort_konge_mørk.png")
    brækker.append(sort_konge_mørk.subsample(size, size))

    sort_konge_lys = PhotoImage(file=rf"{path}\Assets\sort_konge_lys.png")
    brækker.append(sort_konge_lys.subsample(size, size))

    sort_dronning_mørk = PhotoImage(file=rf"{path}\Assets\sort_dronning_mørk.png")
    brækker.append(sort_dronning_mørk.subsample(size, size))

    sort_dronning_lys = PhotoImage(file=rf"{path}\Assets\sort_dronning_lys.png")
    brækker.append(sort_dronning_lys.subsample(size, size))

    tom_mørk = PhotoImage(file=rf"{path}\Assets\tom_mørk.png")
    brækker.append(tom_mørk.subsample(size, size))

    tom_lys = PhotoImage(file=rf"{path}\Assets\tom_lys.png")
    brækker.append(tom_lys.subsample(size, size))

    hvid_bonde_mørk = PhotoImage(file=rf"{path}\Assets\hvid_bonde_lys.png")
    brækker.append(hvid_bonde_mørk.subsample(size, size))

    hvid_bonde_lys = PhotoImage(file=rf"{path}\Assets\hvid_bonde_mørk.png")
    brækker.append(hvid_bonde_lys.subsample(size, size))

    hvid_løber_mørk = PhotoImage(file=rf"{path}\Assets\hvid_løber_mørk.png")
    brækker.append(hvid_løber_mørk.subsample(size, size))

    hvid_løber_lys = PhotoImage(file=rf"{path}\Assets\hvid_løber_lys.png")
    brækker.append(hvid_løber_lys.subsample(size, size))

    hvid_springer_mørk = PhotoImage(file=rf"{path}\Assets\hvid_springer_mørk.png")
    brækker.append(hvid_springer_mørk.subsample(size, size))

    hvid_springer_lys = PhotoImage(file=rf"{path}\Assets\hvid_springer_lys.png")
    brækker.append(hvid_springer_lys.subsample(size, size))

    hvid_tårn_mørk = PhotoImage(file=rf"{path}\Assets\hvid_tårn_mørk.png")
    brækker.append(hvid_tårn_mørk.subsample(size, size))

    hvid_tårn_lys = PhotoImage(file=rf"{path}\Assets\hvid_tårn_lys.png")
    brækker.append(hvid_tårn_lys.subsample(size, size))

    hvid_konge_mørk = PhotoImage(file=rf"{path}\Assets\hvid_konge_mørk.png")
    brækker.append(hvid_konge_mørk.subsample(size, size))

    hvid_konge_lys = PhotoImage(file=rf"{path}\Assets\hvid_konge_lys.png")
    brækker.append(hvid_konge_lys.subsample(size, size))

    hvid_dronning_mørk = PhotoImage(file=rf"{path}\Assets\hvid_dronning_mørk.png")
    brækker.append(hvid_dronning_mørk.subsample(size, size))

    hvid_dronning_lys = PhotoImage(file=rf"{path}\Assets\hvid_dronning_lys.png")
    brækker.append(hvid_dronning_lys.subsample(size, size))


    return brækker

def main():
    root = Tk()
    path = sys.path[0]


    b = test(root, gen_picts(path, 3))
    b.lav()
    mainloop()

main()