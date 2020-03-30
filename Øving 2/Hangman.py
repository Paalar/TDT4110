print("Nå skal vi spille Hangman!\n")
ordet = input("Hva skal ordet været?\n").lower()
liv = int(input("Hvor mange forsøk skal spilleren ha?\n"))

print("\nOrdet har ", len(ordet), "bokstaver")
print("Du har", liv, "liv")
lengde = len(ordet)

#bokstav = input("Skriv inn en bokstav til ordet")
def Bokstaver():
    global liv
    global lengde
    while liv > 0:
        bokstav = input("Skriv inn en bokstav til ordet\n").lower()
        if bokstav in ordet:
            print("Riktig svar.")
            lengde = lengde-1
        else:
            print("Feil svar.")
            liv = liv-1

#def lol(lengde, bokstav):
#    while liv > 0:
#        bokstav = input("Skriv inn en bokstav til ordet\n").lower()
#        if bokstav in ordet:
#            print("Riktig svar.")
#            lengde = lengde-1
#            return lol()
#        else:
#            print("Feil svar.")
#            liv = liv-1


Bokstaver()

if liv == 0:
    print("Du har ingen liv igjen. Du har tapt")
else:
    pass

if lengde == 0:
    print("Du har vunnet! Ordet var", bokstav)
else:
    pass
