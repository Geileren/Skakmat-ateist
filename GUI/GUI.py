from PIL import Image, ImageTk
from tkinter import *

class Bræt():
    def __init__(self, root):
        self.root = root
        self.table_fields = []
        self.pawn = PhotoImage(file = r"C:\Users\jakob\Skakmat-ateist\GUI\Img\Pawn.png")
        self.pawnimage = self.pawn.subsample(1, 1)
        self.draw_gui()
        

    def draw_gui(self):

        for y in range(8):
            for x in range(8):
                if (y % 2 + x) % 2 == 0:
                    self.table_fields.append(Button(self.root, width=5, height=2, bg="white"))
                    self.table_fields[len(self.table_fields)-1].grid(column=x, row=y)
                    if y == 1:
                        self.table_fields[len(self.table_fields)-1].config(image=self.pawnimage)
                else:
                    self.table_fields.append(Button(self.root, width=5, height=2, bg="black").grid(column=x, row=y))
# width=5, height=2, bg="white"
def main():
    root = Tk()
    Bræt(root)
    root.mainloop()

main()