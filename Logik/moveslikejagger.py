import Data.Brikker as brikker


#Returnerer sandt hvis det træk der er regnet ud er indenfor brættets længde og bredde ved at opfylde kravene der hedder at det skal være større end -1 både længde og bredde
#og det skal være mindre end 8 både længde og bredde da python lister jo er 0 indekserede selvom brættet er 8x8 lang og bred
def på_bord(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True

#Funktion der laver en liste ud fra det specifikke træk sæt til den valgte brik og returnere en liste
#over mulige træk som et 2d array, altså i og j er vores x og y koordinat på brættet.
def fremhæv(Bræt):
    fremhævet = []
    for i range(len(Bræt)):
        for j in range(len(Bræt[0])):
            if Bræt[i][j] == "x":
                fremhævet.append((i, j))
            else:
                try:
                    if Bræt[i][j].kandræbes
                        fremhævet.append((i, j))
                except:
                    pass
    return fremhævet


#Tjekker Hvilket hold der er valgt, dette gør den ved at finde ud af hvilken runde det er først.
#Da hvis det er en lige runde så vil %2 returnere 0 som rest da den går op fordi hvid er lige runder
def tjek_hold(træk, indeks):
    row, col = indeks
    if træk%2 == 0:
        if Bræt[row][col].hold == "h":
            return True
    else:
        if Bræt[row][col].hold =="s":
            return True


#Funktion der henter træksættet til den valgte brik, dette gør den ud fra nogle simple if funktioner
#Som egentlig bare spørger efter hvilken brik der er tale om ud fra det objekt vi har lavet til brikken
def vælg_træk(brikker.Brik, indeks, træk):
    if tjek_hold(træk, indeks):
        if brikker.Brik.type == "b":
            if brikker.Brik.hold == "s":
                return fremhæv(bonde_træk_s(indeks))
            else:
                return fremhæv(bonde_træk_h(indeks))

        if brikker.Brik.type == "d"
            return fremhæv(dronning_træk(indeks))

        if brikker.Brik.type == "k"
            return fremhæv(konge_træk(indeks))

        if brikker.Brik.type == "s"
            return fremhæv(springer_træk(indeks))

        if brikker.Brik.type == "l"
            return fremhæv(løber_træk(indeks))


