import Data.Brikker as brikker


#Returnerer sandt hvis det træk der er regnet ud er indenfor brættets længde og bredde ved at opfylde kravene der hedder at det skal være større end -1 både længde og bredde
#og det skal være mindre end 8 både længde og bredde da python lister jo er 0 indekserede selvom brættet er 8x8 lang og bred
def på_bord(placering):
    if placering[0] > -1 and placering[1] > -1 and placering[0] < 8 and placering[1] < 8:
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
def tjek_hold(træk, position):
    row, col = position
    if træk%2 == 0:
        if Bræt[row][col].hold == "h":
            return True
    else:
        if Bræt[row][col].hold =="s":
            return True


#Funktion der henter træksættet til den valgte brik, dette gør den ud fra nogle simple if funktioner
#Som egentlig bare spørger efter hvilken brik der er tale om ud fra det objekt vi har lavet til brikken
#Grunden til at vi tjekker hold ved bonden er fordi de kan gå i en retning og derfor vil det være nemmere at lave to forskellgie funktioner til dem efter hvilket hold de er på
def vælg_træk(brikker.Brik, position, træk):
    if tjek_hold(træk, indeks): #Kører tjek hold funktionen
        if brikker.Brik.type == "b": #Hvis brikken er af typen bonde
            if brikker.Brik.hold == "s": #Hvis brikken er af farven sort
                return fremhæv(bonde_træk_s(position))
            else: #Ellers må brikken være hvid
                return fremhæv(bonde_træk_h(position))

        if brikker.Brik.type == "d": #Hvis brikken er af typen Dronning
            return fremhæv(dronning_træk(position)) #Fremhæver dronningstræk ud fra fremhæv funktionen og dronningstræk funktion

        if brikker.Brik.type == "k": #Hvis brikken er af typen Konge
            return fremhæv(konge_træk(position)) #Fremhæver kongenstræk ud fra fremhæv funktionen og kongenstræk funktion

        if brikker.Brik.type == "s": #Hvis brikken er af typen Springer
            return fremhæv(springer_træk(position)) #Fremhæver springerenstræk ud fra fremhæv funktionen og springerenstræk funktion

        if brikker.Brik.type == "l": #hvis brikken er af typen Løber
            return fremhæv(løber_træk(position)) #Fremhæver løberenstræk ud fra fremhæv funktionen og Løberenstræk funktion

        if brikker.Brik.type == "t": #Hvis brikken er af typen tårn
            return fremhæv(tårn_træk(position)) #Fremhæver tårnetstræk ud fra fremhæv funktionen og tårnetstræk funktion


def bonde_træk_s(position):
    if position[0] == 1: #Da en bonde må flytte sig 2 på dens første træk spørger vi først efter om den står på den første flade
        if Bræt[position[0]+2][position[1]] == ' ' and Bræt[position[0]+1][position[1]] == '  ': #Derefter tjekker vi om de to pladser foran den er ledige ved at tjekke for x markeringer
            Bræt[position[0]+2][position[1]] = 'x '
    #Før laver vi en liste med de 3 positioner foran bonden for at se om der er noget den kan dræbe, dette gør vi
    #ved at oprette tre forskellige sæt koordinator som er lige foran brikken og -1 til den ene side og 2 til den anden side.
    pladserforans = [[position[0]+1, position[1] + i] for i in range(-1,2)]

    for placering in pladserforans: #Tjekker for alle tre positioner fra listen vi lavede oven over
        if på_bord(placering): #Tjekker om placeringerne er på brættet
            if pladserforans.index(placering) % 2 == 0: #Vi vil kun have de to placeringer der er diagonalt for brikken derfor ikke den i midten så vi
                                                        #Benytter os af .index som giver tilbage deres placering i listen og den første er 0 og nr 3 er 2
                                                        #Disse to tal går op i 2 og giver 0 rest tilbage derfor vil de blive sendt videre mens den position
                                                        #lige over for vil returnere en rest af 1 og ikke sendt videre
                try:
                    if Bræt[position[0]][position[1]].hold == "h": #Tjekker om brikken er modstander holdet
                        Bræt[position[0]][position[1]].kandræbes = True #Hvis ikke sætter vi brikken som den kan dræbes
                except:
                    pass #Altid godt at have et except statement med et pass så koden ikke sidder fast, jeg har lært noget jørn
            else: #Ellers skal man jo kunne flytte brikken op der hvor den ikke kan dræbe så den bliver sendt herned pga else statementet
                if Bræt[position[0]][position[1]] == '': #tjekker om der er fri plads på feltet foran og her ligger vi jo ikke en til da vi allerede har gjort det oven over
                    Bræt[position[0]][position[1]] = 'x' #Hvis der er frit markeres dette med et x for at signalere seneere hen at det er et muligt træk
        return Bræt #Returnere listen bræt som den ser ud nu

#Samme funktion som oven over udover at de hvide starter et andet sted altså i bund så de arbejder sig op af listen
def bonde_træk_h(position):
    if position[0] == 6:
        if Bræt[position[0]-2][position[1]] == ' ' and Bræt[position[0]-1][position[1]] == ' ':
            Bræt[position[0]-2][position[1]] = 'x'

        pladserforanh = [[position[0]-1, position[1]-i] for i in range(-1,2)]

        for placering in pladserforanh:
            if på_bord(placering):
                if pladserforanh.index(placering) % 2 == 0:
                    try:
                        if Bræt[position[0]][position[1]].hold == "s":
                            Bræt[position[0]][position[1]].kandræbes = True
                    except:
                        pass
                else:
                    if Bræt[position[0]][position[1]] == '':
                        Bræt[position[0]][position[1]] == 'x'

    return brikker.Bræt

def tårn_træk(position):
    #Laver fire lister som sættes sammen til en liste for at lave tårnets kryds som den kan flytte sig i
    kryds = [[[position[0] + i, position[1]] for i in range(1,8 - position[0])],  #Den første liste er ud til højre derfor tjekker vi fra 1 til 8 minus der hvor den står da vi så ikke tjekker ud over brættets kant
             [[position[0] - i, position[1]] for i in range(1,position[0] + 1)],  #Den anden liste er ud til venstre for den som tjekker fra 1 til dens position 0 ved at trække fra og vi lægger så 1 til da listerne er 0 indekserede
             [[position[0], position[1] + i] for i in range(1,8 - position[1])],  #Den tredje liste tjekker op af brættet og her gør vi det samme som i lsite udover at det er emd andet koordinatet
             [[position[0], position[1] - i] for i in range(1, position[1] + 1)]] #Den fjerde liste tjekker ned af brættet og her gør vi det samme som i liste 2 udover med anden koordinatet

    for retning in kryds: #Deler den store liste op i de forskellige retninger
        for placering in retning: #Tjekker for alle individuelle placeringer i de her retninger
            if på_bord(placering): #Tjekker om de er på bordet for en sikkerhedsskyld
                if Bræt[placering[0]][placering[1]] == ' ': #Hvis der ikke står noget
                    Bræt[placering[0]][placering[1]] = 'x ' #Så placerer vi et x
                else:
                    if Bræt[placering[0]][placering[1]].brikker.Brik.hold != Bræt[position[0]][position[1]].brikker.Brik.hold: #Hvis tårnets hold ikke er det samme som den brik der står på feltet
                        Bræt[placering[0]][placering[1]].brikker.Brik.kandræbes = True #Ændre den briks attribute kandræbes til at være sand

                    break #Altid godt at have et break statement
            return brikker.Bræt #returnere brættet 