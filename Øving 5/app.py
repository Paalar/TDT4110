def billettpris(alder):
    if alder < 0:
        print ("Ugyldig alder")
    elif alder < 5:
        print ("Billetten er gratis")
    elif alder <= 20:
        print ("Billettpris kr 20")
    elif alder <= 25:
        print ("Billettpris kr 50")
    elif alder <= 60:
        print ("Billettpris kr 80")
    elif alder < 150:
        print ("Billetten er gratis")
    else:
        print ("Ugyldig alder")

billettpris(int(input("Hvor gammel er du?\n")))
