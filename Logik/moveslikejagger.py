import Data.Brikker as brikker


def fremhæv(Bræt):
    fremhævet = []
    for i range(len(Bræt)):
        for j in range(len(Bræt[0])):
            if Bræt[i][j] == "x":
                fremhøvet.append((i, j))
            else:
                try:
                    if Bræt[i][j].kandræbes
                        fremhævet.append((i, j))
                except:
                    pass
    return fremhævet



def tjek_hold(træk, indeks):
    row, col = indeks
    if træk%2 == 0:
        if Bræt[row][col].hold == "h":
            return True
        else:
            if Bræt[row][col].hold =="s":
                return True



def vælg_træk(brikker.Brik, indeks, træk):
    if tjek_hold(træk, indeks):
        if brikker.Brik.type == "b":
            if brikker.Brik.hold == "s":
                return fremhæv(bonde_træk_s(indeks))
            else:
                return fremhæv(bonde_træk_h(indeks))

        if brikker.Brik.type == "d"
            return fremhævet(dronning_træk(indeks))

        if brikker.Brik.type == "k"
            return fremhævet(konge_træk(indeks))

        if brikker.Brik.type == "s"
            return fremhævet(springer_træk(indeks))

        if brikker.Brik.type == "l"
            return fremhævet(løber_træk(indeks))
