print("Nå vil jeg at du skal skrive navnene dine inn her!")

AlderX = int(input("Hvor gammel er du?\n"))

NavnF = input("Hva er fornavnet ditt? \n")

NavnM = input("Har du mellom navn? Hvis ja, skriv de/n inn her. Hvis ikke bare trykk Enter \n")

NavnE = input("Hva er etternavnet ditt?\n")

if len(NavnM) == 0:
    print ("Ditt navn er", NavnF, NavnE, "og du er", AlderX, "gammel.")
    # print ("Ditt navn er {0} {1} og du er {2} gammel".format(NavnF, NavnE, AlderX))
else:
    print ("Ditt navn er",  NavnF, NavnM, NavnE, "og du er", AlderX, "gammel.")
