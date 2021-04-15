import tkinter
from tkinter import *
#from PIL import Image, ImageTk

class test:

    def __init__(self, root, pawn):
        self.root = root
        self.pawn = pawn
        self.table_fields = []

    def lav(self):

        for y in range(8):
            for x in range(8):
                if (y % 2 + x) % 2 == 0:
                    self.table_fields.append(Button(self.root, bg="dark blue"))
                    self.table_fields[len(self.table_fields)-1].grid(column=x, row=y)
                    if y == 1:
                        self.table_fields[len(self.table_fields)-1].config(image=self.pawn)
                else:
                    self.table_fields.append(Button(self.root, bg="white"))
                    self.table_fields[len(self.table_fields) - 1].grid(column=x, row=y)
                    if y == 1:
                        self.table_fields[len(self.table_fields)-1].config(image=self.pawn)




        #a = Button(self.root)
        #a.grid(column=1, row=1)
        #a.config(image=self.pawn)

def gen_picts():
    pawn = PhotoImage(file=r"C:\Users\jakob\Skakmat-ateist\GUI\Img\Pawn.png")
    return pawn.subsample(10, 10)

def main():
    root = Tk()


    b = test(root, gen_picts())
    b.lav()
    mainloop()

main()