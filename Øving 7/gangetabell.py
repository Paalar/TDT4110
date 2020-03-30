tlist1 = []
for i in range(0, 15):
    tlist1.append(i)
y = 8
mindreenn = []
størreenn = []



def seperate(numbers, treshold):    #funksjon som tar in to argumenter
    for i in numbers:               #sjekker alle elementene i listen numbers
        if i < treshold:            #hvis elementene er mindre enn argumentet treshold
            mindreenn.append(i)     #legger de elementene inn i en liste som heter mindreenn
        if i >= treshold:           #hivs elementene er større enn eller lik argumentet treshold
            størreenn.append(i)     #legger de elementene inn i en lise som heter størreenn
    return mindreenn, størreenn     #returnerer de to listene

def multiplication_table(n):                                #funksjon som tar inn ett argument
    gtabell = [[0 for x in range(n)] for y in range(n)]     #lager en liste med tallene n nuller i seg., og så multipliserer den med antall n
    gtall = 1                                               #tallet man må gange med
    for x in range(n):                                      # for hver x verdi i range (0, n):
        for y in range(n):                                  # for hver y verdi i range (0, n):
            gtabell[x][y] = (y+1)*gtall                     # andre iterasjon: i listen gtabell [1][2] = 1+1 * 1 = 2. Niende iterasjon: i listen gtabell[3][3] når n = 3. = 2+1 * 3 = 9.
        gtall += 1                                          #når man er ferdig med første liste, så legger man til 1 i gtall for å gå til andre ganger (tredje, ferdje gangen osv.)
    return gtabell



print(seperate(tlist1, y))          #printer 2 lister mindreenn og størreenn

for i in multiplication_table(10):  #
    print (i)                       # printer listene på en pen måte.
