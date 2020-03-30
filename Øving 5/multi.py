def multiplikasjon(tol):
    endring = 1
    produkt = 1
    n = 0
    print("Toleranse verdien er ", tol)
    while endring > tol:
        n +=1
        iterasjoner = (1 + (1/n**2))
        nesteiterasjon, produkt = produkt, produkt*iterasjoner
        endring = produkt-nesteiterasjon
    print("Produktet ble %a etter %a iterasjoner. Endringen er %a" )
    print ("Produktet ble {0:.3f} etter {1} iterasjoner. Endringen er {2:.4f}".format(produkt , n, endring))
    return produkt



multiplikasjon(float(input("Hvor stor skal toleransen være?     ")))
