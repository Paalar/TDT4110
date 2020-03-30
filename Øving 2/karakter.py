while True:
    try:
        karakter = eval(input("Hva er poengsummen?\n"))
    except (NameError, SyntaxError):
        print("Dette går ikke.")

while type(karakter) == float:
    print("dette går ikke!")
    karakter = eval(input("Jeg trenger en gyldig poengsum!\n"))

while karakter<0 or karakter>100:
        print("Dette tallet kan du ikke få på eksamen, prøver du å jukse?")
        karakter = eval(input("Jeg trenger en gyldig poengsum!\n"))

if type(karakter) ==int and 0<=karakter<=40:
    print("Din karakter er: F        Du stryker!")
elif type(karakter) ==int and 41<=karakter<=52:
    print("Din karakter er: E        Det var like før du strøyk, er du stolt?")
elif type(karakter) ==int and 53<=karakter<=64:
    print("Din karakter er: D        Du kunne prøvd litt hardere da.")
elif type(karakter) ==int and 65<=karakter<=76:
    print("Din karakter er: C        Du er helt gjennomsnittlig.")
elif type(karakter) ==int and 77<=karakter<=88:
    print("Din karakter er: B        Bra jobbet, dette var ingen dårlig karakter!")
elif type(karakter) ==int and 89<=karakter<=100:
    print("Din karakter er: A        Sikker på at du ikke jukset?")
else:
    print("Nei dette her var dårlig saker as")
