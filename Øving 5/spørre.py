antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_itgk = 0
antall_timer_lekser = 0

kjønn = 0
age = 0
fag = 0
#hvis noen sier hade så vil while løkken avsluttes.

def whilekjonn():
    kjønn = input("Er du mann eller kvinne?\n").lower()
    if kjønn == "m" or kjønn == "mann" or kjønn == "k" or kjønn == "kvinne" or kjønn == "hade":
        return kjønn
    else:
        print ("Ugyldig kjønn")
        whilekjonn()

def alder():
    age = int(input("Hvor gammel er du?\n"))
    return age

def fager():
        fag = input("Tar du ett fag?\n").lower()
        if fag == "ja" or fag == "j" or fag == "nei" or fag == "n":
            return fag
        else:
            print("Ugyldig svar")
            fager()

def itgk(age):
    global antall_itgk
    antall_itgk += 1
    if age <= 22:
        print ("Tar du ITGK?")
    else:
        print ("Tar du særr ITGK?")


while True:
    kjønn = whilekjonn()
    if kjønn == "m" or kjønn == "mann":
        print ("Du er en mann")
        antall_menn += 1
    elif kjønn == "k" or kjønn == "kvinne":
        print ("Du er en kvinne")
        antall_kvinner += 1
    elif kjønn == "hade":
        break

    age = alder()
    if 16 <= age <= 25:
        print("Du passer perf.")
        fag = fager()
        if fag == "ja" or fag == "j":
            itgk(age)
            antall_fag += 1
            timer_lekser = float(input("Hvor mange timer i uka bruker du i uka på lekser da?\n"))
            antall_timer_lekser += timer_lekser

        elif fag == "hade":
            break
        else:
            print("Du burde ta ITGK.")
    else:
        print("Du er ikke innenfor aldersgruppen vi søker, beklager")

print("Kvinner {}, Menn {}, fag {}, itgk {}, timer lekser {}".format(antall_kvinner, antall_menn, antall_fag, antall_itgk, antall_timer_lekser))
