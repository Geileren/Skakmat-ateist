import Data.Brikker as brikker


#Returnerer sandt hvis det træk der er regnet ud er indenfor brættets længde og bredde ved at opfylde kravene der hedder at det skal være større end -1 både længde og bredde
#og det skal være mindre end 8 både længde og bredde da python lister jo er 0 indekserede selvom brættet er 8x8 lang og bred
def på_bord(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True

#Funktion der laver en liste ud fra det specifikke træk sæt til den valgte brik og returnere en liste
#over mulige træk som et 2d array, altså i og j er vores x og y koordinat på brættet.
def fremhæv(Bræt):
    fremhævet = [] #Opretter en liste over potentielle træk
    for i range(len(Bræt)): #Kører et for loop på selve listen for at få en over bredden
        for j in range(len(Bræt[0])): #Kører derefter et for loop på den første i listen for at få en over længden
            if Bræt[i][j] == "x": #Hvis der er nogle af de felter den tjekker for som er markeret med et x så tilføj dem til listen
                fremhævet.append((i, j)) #Tilføjer dem til listen
            else: #Ellers
                try: #prøv at spørg
                    if Bræt[i][j].kandræbes #Hvis det er en brik om den kan dræbes hvis ja tilføj til liste
                        fremhævet.append((i, j))
                except:
                    pass #Altid have et except statement med et pass for safety
    return fremhævet #returner listen med potentielle træk for den enekelte brik


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
#Grunden til at vi tjekker hold ved bonden er fordi de kan gå i en retning og derfor vil det være nemmere at lave to forskellgie funktioner til dem efter hvilket hold de er på
def vælg_træk(brikker.Brik, indeks, træk):
    if tjek_hold(træk, indeks): #Kører tjek hold funktionen
        if brikker.Brik.type == "b": #Hvis brikken er af typen bonde
            if brikker.Brik.hold == "s": #Hvis brikken er af farven sort
                return fremhæv(bonde_træk_s(indeks))
            else: #Ellers må brikken være hvid
                return fremhæv(bonde_træk_h(indeks))

        if brikker.Brik.type == "d": #Hvis brikken er af typen Dronning
            return fremhæv(dronning_træk(indeks)) #Fremhæver dronningstræk ud fra fremhæv funktionen og dronningstræk funktion

        if brikker.Brik.type == "k": #Hvis brikken er af typen Konge
            return fremhæv(konge_træk(indeks)) #Fremhæver kongenstræk ud fra fremhæv funktionen og kongenstræk funktion

        if brikker.Brik.type == "s": #Hvis brikken er af typen Springer
            return fremhæv(springer_træk(indeks)) #Fremhæver springerenstræk ud fra fremhæv funktionen og springerenstræk funktion

        if brikker.Brik.type == "l": #hvis brikken er af typen Løber
            return fremhæv(løber_træk(indeks)) #Fremhæver løberenstræk ud fra fremhæv funktionen og Løberenstræk funktion

        if brikker.Brik.type == "t": #Hvis brikken er af typen tårn
            return fremhæv(tårn_træk(indeks)) #Fremhæver tårnetstræk ud fra fremhæv funktionen og tårnetstræk funktion


