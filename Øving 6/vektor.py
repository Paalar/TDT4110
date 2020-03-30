from math import sqrt
lol = [1.5, 3.7, 4.5]
eksempel1 = [3, 7, 1]
eksempel2 =[2, -4, 8]
eksempelc = 2
xyzlist = []
 
def xyzvar(x, y, z):
    xyzlist.append(x)
    xyzlist.append(y)
    xyzlist.append(z)
    return xyzlist

def printvektor(vec1):
    print("Vektor 1 =",vec1)

def skalar(vektor, c):
    skalar = 0
    for i in vektor:
        skalar += i*c
        xyzlist.append(i*c)
    return xyzlist

def vektorlengde(vektor):
    print(vektor)
    lengde = 0
    skalengde = 0
    skalar(lol, 2)

    for i in vektor:
        lengde += i**2
    lengde = sqrt(lengde)
    print("Lengden til vektoren er {0} før skalering".format("%.4f" % lengde))
    for i in xyzlist:
        skalengde += i**2
    skalengde = sqrt(skalengde)
    print("Lengden til vektoren etter skalaringen er {0}".format("%.4f" % skalengde))

def dotvektor(vektor1, vektor2):
    dotlist = []
    dot = 0
    print("Vektor 1 er {0}\nVektor 2 er {1}".format(vektor1, vektor2))
    for i in range(len(vektor1)):
        dot += vektor1[i]*vektor2[i]
        vektor3 = vektor1[i]*vektor2[i]
        dotlist.append(float("%.2f" % vektor3))
    print ("Dotproduktet for disse vektorene er {0}.\nSummen er {1}".format(dotlist, dot))
    return dotlist, dot
#    for i in vekotr1:
#        for j in vektor2:
#            print(dot)

#skalar(lol, 2)
#vektorlengde(lol)
#dotvektor(lol, skalar(lol, 2))
dotvektor(eksempel1, eksempel2)
