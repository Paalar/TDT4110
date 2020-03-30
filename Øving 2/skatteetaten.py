boligtype = input("Du må fortelle meg hva slags type bolig dette er. Er det:\n"
                    "en sekeundærbolig, egenbolig eller fritidsbolig?\n")


if boligtype.lower() == "sekundærbolig" or boligtype.lower() == "sekundær":
    print ("Hei, skatteetaten her. Jeg skal beregne hvor stor del av inntekten din er skattbar.\n"
            "Først må jeg vite hvor stor del av boligen du har leid ut i prosent.\n"
            "Eksempel: hvis du leier ut 20% av leiligheten skriver du bare inn 20")
    andelleid = float(input("Skriv her: "))

    while andelleid>100 or andelleid<0:
        print ("Dette tallet er ikke et gyldig prosenttall")
        andelleid = float(input("Skriv inn et gyldig tall: "))

    andelinntekt = float(input("Skriv inn hva du har hatt i leieinntekt i året: "))
    print ("Sorry, Mac. Fordi dette er en sekundærbolig så må du skatte alt uansett")

if boligtype.lower() == "egenbolig" or boligtype.lower() == "egen":
    print ("Hei, skatteetaten her. Jeg skal beregne hvor stor del av inntekten din er skattbar.\n"
            "Først må jeg vite hvor stor del av boligen du har leid ut i prosent.\n"
            "Eksempel: hvis du leier ut 20% av leiligheten skriver du bare inn 20")
    andelleid = float(input("Skriv her: "))

    while andelleid>100 or andelleid<0:
        print ("Dette tallet er ikke et gyldig prosenttall")
        andelleid = float(input("Skriv inn et gyldig tall: "))

    andelinntekt = float(input("Skriv inn hva du har hatt i leieinntekt i året: "))

    if andelleid <= 50:
        print ("Siden du bruker ihvertfall halvparten selv så er alt du tjener skattefritt, grattis!")
    elif andelleid > 50 and andelinntekt < 20000:
        print ("Du bruker kanskje litt mye av leiligheten selv, men du tjener ikke så mye i året så det går bra.")
    elif andelleid > 50 and andelinntekt > 20000:
        print ("Du bruker for mye av boligen og du tjener for mye penger. Dette må du skatte.", andelinntekt)
    else:
        print ("Noe gikk galt.")


if boligtype.lower() == "fritidsbolig" or boligtype.lower() == "fritid":
    hytte = input("Er denne fritidsboligen en utleiehytte eller ikke? Svar ja/nei\n")
    if hytte.lower() == "ja":
        hytter = int(input("Hvor mange hytter leier du ut?\n"))
        if hytter == 1:
            andelinntekt = float(input("Skriv inn hva du har hatt i leieinntekt i året:\n"))
            print ("Sorry, Mac. Fordi dette er en fritidsbolig så må du skatte alt uansett")
        elif hytter > 1:
            hytterplis = int(input("Hvor mange hytter har du som du tjener mer enn kr 10 000 på?\n"))
            hytter = hytter - hytterplis
            if hytter > 0:
                andelinntekt = float(input("Skriv inn hva du har hatt i leieinntekt i året på de andre hyttene som overgår kr 10 000:\n"))
                print(andelinntekt*0.85)
            else:
                pass
        else:
                print("Dette tallet er ikke gyldig.")
    elif hytte.lower() == "nei":
        andelfri = int(input("Hvor mange fritidsboliger eier du?"))
        if andelfri == 1:
            andelinntekt = float(input("Hva var inntekten til fritidsboligen din?"))
            if andelinntekt < 10000:
                print ("Slapp av dude, dette er skattefritt.")
            elif andelinntekt >= 10000:
                andelinntekt = andelinntekt - 10000
                print(andelinntekt*0.85, "Er summen du må skatte")
        elif andelfri > 1:
            boligfri = float(input("Hvor mange fritidsboliger tjener du mer enn kr 10 000 på?:\n"))
            if boligfri == 0:
                print ("Slapp av dude, dette er skattefritt.")
            elif boligfri > 0:
                andelinntekt = float(input("Hva var inntekten til fritidsboligene dine som oversteg kr 10 000?\n"))
                if andelinntekt < 10000:
                    print ("Slapp av dude, dette er skattefritt.")
                elif andelinntekt >= 10000:
                    andelinntekt = andelinntekt - 10000
                    print(andelinntekt*0.85, "Er summen du må skatte")
        else:
            pass
    else:
        pass







#print ("Hei, skatteetaten her. Jeg skal beregne hvor stor del av inntekten din er skattbar.\n"
#        "Først må jeg vite hvor stor del av boligen du har leid ut i prosent.\n"
#        "Eksempel: hvis du leier ut 20% av leiligheten skriver du bare inn 20")

#andelleid = float(input("Skriv her: "))

#while andelleid>100 or andelleid<0:
#    print ("Dette tallet er ikke et gyldig prosenttall")
#    andelleid = float(input("Skriv inn et gyldig tall: "))

#andelinntekt = float(input("Skriv inn hva du har hatt i leieinntekt i året: "))

#if andelleid <= 50:
#    print ("Siden du bruker ihvertfall halvparten selv så er alt du tjener skattefritt, grattis!")
#elif andelleid > 50 and andelinntekt < 20000:
#    print ("Du bruker kanskje litt mye av leiligheten selv, men du tjener ikke så mye i året så det går bra.")
#elif andelleid > 50 and andelinntekt > 20000:
#    print ("Du bruker for mye av boligen og du tjener for mye penger. Dette må du skatte.")
#else:
#    print ("Noe gikk galt.")
