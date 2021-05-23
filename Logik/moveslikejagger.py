from Data.Brikker import *


#print(Braet)


# Returnerer sandt hvis det træk der er regnet ud er indenfor brættets længde og bredde ved at opfylde kravene der hedder at det skal være større end -1 både længde og bredde
# og det skal være mindre end 8 både længde og bredde da python lister jo er 0 indekserede selvom brættet er 8x8 lang og bred
def paa_bord(placering):
    if placering[0] > -1 and placering[1] > -1 and placering[0] < 8 and placering[1] < 8:
        return True

# Funktion der laver en liste ud fra det specifikke træk sæt til den valgte brik og returnere en liste
# over mulige træk som et 2d array, altså i og j er vores x og y koordinat på brættet.
def fremhaev(Braet):
    fremhaevet = [] # Opretter en liste over potentielle træk
    for i in range(8): # Kører et for loop på selve listen for at få en over bredden
        for j in range(8): # Kører derefter et for loop på den første i listen for at få en over længden
            if Braet[i][j] == 'x ': # Hvis der er nogle af de felter den tjekker for som er markeret med et x så tilføj dem til listen
                fremhaevet.append((i, j)) # Tilføjer dem til listen
            else:
                try: # prøv at spørg
                    if Braet[i][j].kandræbes: # Hvis det er en brik om den kan dræbes hvis ja tilføj til liste
                        fremhaevet.append((i, j))
                except:
                    pass # Altid have et except statement med et pass for safety
    return fremhaevet # returner listen med potentielle træk for den enekelte brik

def reset_Braet(Braet):
    for i in range(8):
        for j in range(8):
            if Braet[i][j] == 'x ':
                Braet[i][j] = ' '
            else:
                try:
                    Braet[i][j].kandræbes = False
                except:
                    pass
    return Braet

# Tjekker Hvilket hold der er valgt, dette gør den ved at finde ud af hvilken runde det er først.
# Da hvis det er en lige runde så vil %2 returnere 0 som rest da den går op fordi hvid er lige runder
def tjek_hold(traek, position):
    row, col = position
    if traek % 2 == 0:
        if Braet[row][col].hold == 'h':
            return True
    else:
        if Braet[row][col].hold == 's':
            return True

# Funktion der henter træksættet til den valgte brik, dette gør den ud fra nogle simple if funktioner
# Som egentlig bare spørger efter hvilken brik der er tale om ud fra det objekt vi har lavet til brikken
# Grunden til at vi tjekker hold ved bonden er fordi de kan gå i en retning og derfor vil det være nemmere at lave to forskellgie funktioner til dem efter hvilket hold de er på
def vaelg_traek(brik, position, traek):
    if tjek_hold(traek, position): # Kører tjek hold funktionen
        if brik.type == 'b': # Hvis brikken er af typen bonde
            if brik.hold == 's': # Hvis brikken er af farven sort
                return fremhaev(bonde_traek_s(position))
            else: # Ellers må brikken være hvid
                return fremhaev(bonde_traek_h(position))

        elif brik.type == 'd': # Hvis brikken er af typen Dronning
            return fremhaev(dronning_traek(position)) # Fremhæver dronningstræk ud fra fremhæv funktionen og dronningstræk funktion

        elif brik.type == 'k': # Hvis brikken er af typen Konge
            return fremhaev(konge_traek(position)) # Fremhæver kongenstræk ud fra fremhæv funktionen og kongenstræk funktion

        elif brik.type == 's': # Hvis brikken er af typen Springer
            return fremhaev(springer_traek(position)) # Fremhæver springerenstræk ud fra fremhæv funktionen og springerenstræk funktion

        elif brik.type == 'l': # hvis brikken er af typen Løber
            return fremhaev(lober_traek(position)) # Fremhæver løberenstræk ud fra fremhæv funktionen og Løberenstræk funktion

        elif brik.type == 't': # Hvis brikken er af typen tårn
            return fremhaev(taarn_traek(position)) # Fremhæver tårnetstræk ud fra fremhæv funktionen og tårnetstræk funktion


def bonde_traek_s(position):
    if position[0] == 1: # Da en bonde må flytte sig 2 på dens første træk spørger vi først efter om den står på den første flade
        if Braet[position[0]+2][position[1]] == ' ' and Braet[position[0]+1][position[1]] == ' ': # Derefter tjekker vi om de to pladser foran den er ledige ved at tjekke for x markeringer
            Braet[position[0]+2][position[1]] = 'x '
    # Før laver vi en liste med de 3 positioner foran bonden for at se om der er noget den kan dræbe, dette gør vi
    # ved at oprette tre forskellige sæt koordinator som er lige foran brikken og -1 til den ene side og 2 til den anden side.
    pladserforans = [[position[0]+1, position[1]+i] for i in range(-1,2)]

    for placering in pladserforans: # Tjekker for alle tre positioner fra listen vi lavede oven over
        if paa_bord(placering): # Tjekker om placeringerne er på brættet
            if pladserforans.index(placering) % 2 == 0: # Vi vil kun have de to placeringer der er diagonalt for brikken derfor ikke den i midten så vi
                                                        # Benytter os af .index som giver tilbage deres placering i listen og den første er 0 og nr 3 er 2
                                                        # Disse to tal går op i 2 og giver 0 rest tilbage derfor vil de blive sendt videre mens den position
                                                        # lige over for vil returnere en rest af 1 og ikke sendt videre
                try:
                    if Braet[placering[0]][placering[1]].hold != Braet[position[0]][position[1]].hold: # Tjekker om brikken er modstander holdet
                        Braet[placering[0]][placering[1]].kandræbes = True # Hvis ikke sætter vi brikken som den kan dræbes
                except:
                    pass # Altid godt at have et except statement med et pass så koden ikke sidder fast, jeg har lært noget jørn
            else: # Ellers skal man jo kunne flytte brikken op der hvor den ikke kan dræbe så den bliver sendt herned pga else statementet
                if Braet[placering[0]][placering[1]] == ' ': # tjekker om der er fri plads på feltet foran og her ligger vi jo ikke en til da vi allerede har gjort det oven over
                    Braet[placering[0]][placering[1]] = 'x ' # Hvis der er frit markeres dette med et x for at signalere seneere hen at det er et muligt træk
    return Braet # Returnere listen bræt som den ser ud nu

# Samme funktion som oven over udover at de hvide starter et andet sted altså i bund så de arbejder sig op af listen
def bonde_traek_h(position):
    if position[0] == 6:
        if Braet[position[0]-2][position[1]] == ' ' and Braet[position[0]-1][position[1]] == ' ':
            Braet[position[0]-2][position[1]] = 'x '

    pladserforanh = [[position[0]-1, position[1]-i] for i in range(-1,2)]

    for placering in pladserforanh:
        if paa_bord(placering):
            if pladserforanh.index(placering) % 2 == 0:
                try:
                    if Braet[placering[0]][placering[1]].hold != Braet[position[0]][position[1]].hold:
                        Braet[placering[0]][placering[1]].kandræbes = True
                except:
                    pass
            else:
                if Braet[placering[0]][placering[1]] == ' ':
                    Braet[placering[0]][placering[1]] = 'x '

    return Braet

def taarn_traek(position):
    # Laver fire lister som sættes sammen til en liste for at lave tårnets kryds som den kan flytte sig i
    plus = [[[position[0]+i, position[1]] for i in range(1,8)],  # Den første liste er ud til højre derfor tjekker vi fra 1 til 8 minus der hvor den står da vi så ikke tjekker ud over brættets kant
            [[position[0]-i, position[1]] for i in range(1,8)],  # Den anden liste er ud til venstre for den som tjekker fra 1 til dens position 0 ved at trække fra og vi lægger så 1 til da listerne er 0 indekserede
            [[position[0], position[1]+i] for i in range(1,8)],  # Den tredje liste tjekker op af brættet og her gør vi det samme som i lsite udover at det er emd andet koordinatet
            [[position[0], position[1]-i] for i in range(1,8)]] # Den fjerde liste tjekker ned af brættet og her gør vi det samme som i liste 2 udover med anden koordinatet

    for retning in plus: # Deler den store liste op i de forskellige retninger
        for placering in retning: # Tjekker for alle individuelle placeringer i de her retninger
            if paa_bord(placering): # Tjekker om de er på bordet for en sikkerhedsskyld
                if Braet[placering[0]][placering[1]] == ' ':# Hvis der ikke står noget
                    Braet[placering[0]][placering[1]] = 'x ' # Så placerer vi et x
                else:
                    if Braet[placering[0]][placering[1]].hold != Braet[position[0]][position[1]].hold:
                        Braet[placering[0]][placering[1]].kandræbes = True


                    break

    return Braet # returnere brættet


# Stortset den samme funktion som tårn_træk men her skal den være diagonal
# så vi lægger bare vores for loop til begge også filtrere vi dem der er uden for brættet fra senere hen
def lober_traek(position):

    # List comprehension er lidt mere avanceret her da vi skal lægge til og trække fra efter hvilken retning vi vil have
    # Bare se det som et koordinatsystem og brikken er origo så giver det god mening
    kryds = [[[position[0]+i, position[1]+i] for i in range(1, 8)],
             [[position[0]-i, position[1]-i] for i in range(1, 8)],
             [[position[0]-i, position[1]+i] for i in range(1, 8)],
             [[position[0]+i, position[1]-i] for i in range(1, 8)]]

    for retning in kryds: # Splitter den store liste op i de 4 små lister
        for placering in retning: # Tager hver psotion i de fire små lister
            if paa_bord(placering): # Spørger om position er på bordet
                if Braet[placering[0]][placering[1]] == ' ': # Hvis der er ikke er noget allerede
                    Braet[placering[0]][placering[1]] = 'x ' # Så marker med et x
                else:
                    if Braet[placering[0]][placering[1]].hold != Braet[position[0]][position[1]].hold: # Her spørger vi om de ikke er det samme hold
                        Braet[placering[0]][placering[1]].kandræbes = True # Hvis de ikke er det samme hold så sæt brikken til at kunne dræbes

                    break
    return Braet

# En dronning er bare et tårn og en løber i en så vi importerer bare deres to funktioner herind i også er den lavet
def dronning_traek(position):
    Braet = taarn_traek(position)
    Braet = lober_traek(position)
    return Braet

# En konge kan flytte i et 3x3 grid rundt om sig så derfor kører vi 2 for loops af 3 for den position han står ved
# Hvor vi trækker en fra fordi det jo er rundt om ham og ikke foran ham ellers ser python ham ikke som origo
def konge_traek(position):
    for i in range(3): # første for loop af 3
        for j in range(3): # Andet for loop af 3
            if paa_bord((position[0] - 1 + i, position[1] - 1 + j)): # Her lægger vi for loopsne til og trækker 1 fra for netop at gøre konge til origo
                if Braet[position[0] - 1 + i][position[1] - 1 + j] == ' ': # Tjekker om der er noget på den position
                    Braet[position[0] - 1 + i][position[1] - 1 + j] = 'x ' # hvis ikke så marker med et x
                else:
                    if Braet[position[0] - 1 + i][position[1] - 1 + j].hold != Braet[position[0]][position[1]].hold: # Hvis der er noget så tjekker vi om det er samme hold
                        Braet[position[0]][position[1]].kandræbes = True # Hvis ikke så sætter vi brikken der står der til at den kan dræbes
    return Braet

# funktion tjekker et 5x5 grid rundt omkring springeren ligesom ved kongen udover at her tjekker vi valide moves ved at bruge pythagoras
# Så alt hvor i og j i anden giver 5 er altså et valid træk for springeren
def springer_traek(position):
    for i in range(5):
        for j in range(5):
            if (i-2)**2 + (j-2)**2 == 5: # Pythagoras tjekket sker her. Der trækkes 2 fra fordi ligesom ved kongen skal springeren være i midten
                if paa_bord((position[0]+i-2,position[1]+j-2)): # tjekker om positionen overhovedet er på brættet
                    if Braet[position[0]+i-2][position[1]+j-2] == ' ': # Som altid hvis der ikke er noget
                        Braet[position[0]+i-2][position[1]+j-2] = 'x ' # så tilføjer vi et x
                    else:
                        if Braet[position[0]+(i-2)][position[1]+(j-2)].hold != Braet[position[0]][position[1]].hold: # Hvis der er noget så tjekker vi om det er samme hold
                            Braet[position[0]][position[1]].kandræbes = True # Hivs det ikke er samme hold så sætter vi brikken der er i vejen som kandræbes
    return Braet



ginga = 1
gunga = 4

gingagunga = ginga,gunga
#print(Braet)
#lav_braet(Braet)
#print(Braet)
#springer_traek(gingagunga)
#print(Braet)
#print(fremhaev(Braet))
#reset_Braet(Braet)
#print(Braet)

lav_braet(Braet)


print(vaelg_traek((Braet[ginga][gunga]), gingagunga, 1))