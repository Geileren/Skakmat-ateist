import Logik.moveslikejagger as mv
from tkinter import *

import sys
class Felt():
    def __init__(self, root, bræt, billede, x, y, brikker, type):
        self.brikker = brikker
        self.bræt = bræt
        self.billede = billede
        self.type = type
        self.fremhævet = False
        self.x = x
        self.y = y
        self.button = Button(root, image=self.billede, command=self.tryk)


    def fremhæv(self):
        self.button.config(bg="yellow")
        self.fremhævet = True

    def glem(self):
        self.button.config(bg="white")
        self.fremhævet = False

    def check_farve(self):
        if (self.x + self.y) % 2 == 0:# tjekker om feltet skal være mørkt
            if self.brikker.index(self.billede) % 2 != 0:# hvis feltet ikke er mørkt
                self.skift([self.brikker[self.brikker.index(self.billede) - 1], self.type])# skiftes til mørk version af samme brik
            else: # feltet har korrekt farve
                pass

        else:
            if self.brikker.index(self.billede) % 2 != 1: # hvis feltet ikke er lyst
                self.skift([self.brikker[self.brikker.index(self.billede) + 1], self.type]) # skiftes til lys version af samme brik
            else: # feltet har korrekt farve
                pass


    def skift(self, brik): #skifter et felt brik og type

        self.billede = brik[0]
        self.type = brik[1]
        self.button.config(image=self.billede, relief="raised", bg="white")


    def grid(self, x, y):
        self.button.grid(column=x, row=y)

    def tryk(self):

        if self.type == "tom" and self.bræt.flyt_brik == False:  # er der ikke valgt en brik kan man ikke vælge et tomt felt
            pass

        elif self.type != "tom" and self.bræt.flyt_brik == False and mv.tjek_hold(self.bræt.runde, [self.y, self.x]) == None: #hvis forkert farve brik vælges
            pass

        elif self.bræt.flyt_brik == False: #hvis der ikke er valgt en brik endnu
            self.bræt.flyt_brik = True
            self.bræt.nuværende_brik = [self.billede, self.type]
            self.bræt.flyt_brik_pos = [self.x, self.y]
            self.bræt.eks_felt = self
            self.button.config(relief="sunken", bg="Orange")
            #skal bede om fremhævet flytte steder fra logik
            self.bræt.fremhæver(mv.vaelg_traek(mv.Braet[self.y][self.x], [self.y, self.x], self.bræt.runde))



        elif self.bræt.flyt_brik == True: #hvis der allerede er valgt en brik
            if self.x == self.bræt.flyt_brik_pos[0] and self.y == self.bræt.flyt_brik_pos[1]: # er den samme brik valgt
                self.bræt.flyt_brik = False
                self.bræt.eks_felt = ""
                self.button.config(relief="raised", bg="white")
                self.bræt.glem_fremhævet()
                mv.reset_Braet(mv.Braet)
            elif self.fremhævet == True:
                #skal flytte til fremhævet ellers skal intet ske
                self.bræt.runde += 1
                self.bræt.flyt_brik = False
                self.skift(self.bræt.nuværende_brik)
                self.check_farve()
                self.bræt.tøm_felt()
                træk = mv.flyt_brik([self.x, self.y], [self.bræt.flyt_brik_pos[0], self.bræt.flyt_brik_pos[1]])
                if træk == "sort":
                    print("sort vandt")
                    self.popup("Sort")

                elif træk == "hvid":
                    print("hvid vandt")
                    self.popup("Hvid")

                self.bræt.glem_fremhævet()
            else:
                pass

    def popup(self, hold):
        slut = Toplevel()
        slut.title("Slut")

        tekst = Label(slut, text=f"{hold} hold vandt! \n tillykke!", font=("Times New Roman", 28, "bold"))
        tekst.grid(column=0, row=0)

        luk = Button(slut, text="Luk spil", font=("Times New Roman", 28, "bold"), command=sys.exit)
        luk.grid(column=0, row=1)

    def tøm(self): #ændres til
        self.skift([self.brikker[12], "tom"])
        self.check_farve()





class Bræt:

    def __init__(self, root, brækker, frame):
        self.root = root
        self.brækker = brækker
        self.tildel_billeder(self.brækker)
        self.gen_start_lister()
        self.table_fields = []
        self.flyt_brik = False
        self.nuværende_brik = ""
        self.flyt_brik_pos = ""
        self.eks_felt = ""
        self.runde = 1
        self.fremhævet = []
        self.frame = frame



    def fremhæver(self, muligheder):
        for i in muligheder:
            for felt in self.table_fields:
                if i[1] == felt.x and i[0] == felt.y:
                    felt.fremhæv()
                    self.fremhævet.append(felt)


    def glem_fremhævet(self):
        for felt in self.fremhævet:
            felt.glem()
        self.fremhævet = []





    def tøm_felt(self):
        self.eks_felt.tøm()
        self.nuværende_brik = ""

    def gen_start_lister(self):
        self.sort_start = [self.sort_tårn_lys, self.sort_springer_mørk, self.sort_løber_lys, self.sort_dronning_mørk, self.sort_konge_lys, self.sort_løber_mørk, self.sort_springer_lys, self.sort_tårn_mørk]
        # liste svarrende til startpositionen for sorte brækker på række 8
        self.hvid_start = [self.hvid_tårn_mørk, self.hvid_springer_lys, self.hvid_løber_mørk, self.hvid_dronning_lys, self.hvid_konge_mørk, self.hvid_løber_lys, self.hvid_springer_mørk, self.hvid_tårn_lys]
        # liste svarrende til startpositionen for hvide brækker på række 1

        self.sort_start_bønder = self.sort_bonde_lys, self.sort_bonde_mørk

        self.hvid_start_bønder = self.hvid_bonde_mørk, self.hvid_bonde_lys

        self.type_liste = ["tårn", "springer", "løber", "dronning", "konge", "løber", "springer", "tårn"]

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
        self.frame.destroy()
        for y in range(1,9):
            for x in range(1,9):
                if y == 1:# tegner alle startbrækkerne i række 1
                    self.table_fields.append(Felt(self.root, self, self.hvid_start[x-1], x-1, y-1, self.brækker, self.type_liste[x-1]))

                elif y == 2:
                    self.table_fields.append(Felt(self.root, self, self.hvid_start_bønder[x%2], x-1, y-1, self.brækker, "bonde"))

                elif y == 7:
                    self.table_fields.append(Felt(self.root, self, self.sort_start_bønder[x%2], x-1, y-1, self.brækker, "bonde"))

                elif y == 8:# tegner alle startbrækkerne i række 8
                    self.table_fields.append(Felt(self.root, self, self.sort_start[x - 1], x-1, y-1, self.brækker, self.type_liste[x-1]))

                elif (y + x) % 2 == 0: #tegner alle tomme mørke felter
                    self.table_fields.append(Felt(self.root, self, self.tom_mørk, x-1, y-1, self.brækker, "tom"))

                else: # tegner de sidste felter, altså tomme lyse
                    self.table_fields.append(Felt(self.root, self, self.tom_lys, x-1, y-1, self.brækker, "tom"))

                self.table_fields[len(self.table_fields) - 1].grid(x-1, y-1)
                # gridder knappen ud fra tilhørende koordinater
                # dermed tegnes alle felter






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
    root.title("Skak")

    path = sys.path[0] #angiver pathen til GUI mappen
    mv.lav_braet(mv.Braet)




    frame = Frame(root)
    frame.grid(column=1, row=1, padx=120, pady=20)

    b = Bræt(root, gen_picts(path, 3), frame)  # initialisere brættet

    Label(frame, text="Skak", font=("Times New Roman", 28, "bold")).grid(column=1, row=1)
    Button(frame, text="Start spil mod anden spiller", width=20, command=b.lav).grid(column=1, row=2)
    Button(frame, text="Start spil mod computer", width=20, state="disabled").grid(column=1, row=3)

    mainloop()

main()