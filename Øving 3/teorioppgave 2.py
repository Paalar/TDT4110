Oppgave a)

def wholeNumber():
    numa = et tall input fra brukeren
    if numa == et heltall:
        print at dette er et heltall
    else:
        dette er ikke et heltall


def evenNumber():
    numb = tar inn enda et tall fra brukeren
    if numb/2 == et heltall:
        print dette er et partall
    else:
        dette er et oddetall

def ayNumber():
    numc = tar inn enda et tall fra brukeren
    if numc er >= 0:
        print Dette tallet er positivt
    else:
        dette tallet er negativt

def compareNr():
    numd og nume tar inn to tall fra brukeren
    if numd er større enn nume:
        print False
    elif numd er mindre enn nume:
        print False
    else:
        print True

Oppgave b)
Hva er et flytdiagram?
Et flytdiagram er et diagram som representerer en algoritme, prosess eller hvordan man skal arbeide(arbeidsprosess).
Diagrammet viser forskjellige steg som bokser, der boksene betyr forskjellige ting, og piler som skal sende deg fran en boks til en annen

Oppgave c)
Debugging er å gå igjennom koden for å se etter feil og mulige grunner for at koden kræsjer, å fikse på dette.

Opogave d)
Forskjellen på et høynivå programmeringspråk og et lavnivå programmeringspråk er at jo lavere du går, jo nærmere "kommer" du til å skrive
en kode slik som maskinen faktisk forstår det. Maskinkode er noe av det laveste man kommer, som er ganske uforståelig hvis man ikke kan
det. Oh et høynivå språk er mer forståelige for oss mennesker, f.eks i python kan vi bare skrive while og maskinen vil forstå at det er
en loop som skal kjøre for alltid

oppgave e)
Hente/Utføre kretsen består av 5 forskjellige steg
1 Instruction Fetch (IF) - Henter instrucksjonene fra PC (Program coutner ) fra minnet som plasserer den i dekodings plassen
2 Instruction Decode (ID) - Dekodingen finner memory addressen til instruksjonene, som skal bli brukt ab Data Fetch delen og destinasjons
addressen som return result delen skal bruke
3 Data Fetch (DF) - Data fetch oversetter informasjonen til f.eks tall, eksempelet i boka er at addresse 2000 blir tallet 30 og addressen
2080 blir tallet 12
4 Instruction Execute (EX) - I denne delen så legger maskinen bare sammen det som ble gjort i forrige del, altså 30 + 12 = 42. eller 2000
+ 2080.
5 Result Return (RR) - I denne siste delen legger svaret 42, inn i addressen 4000self.

oppgave f)
Program Counter (PC) Leser av instruksjons addressen og setter den inn i Fetch/Execute cycle. Når den da er ferdig legger den til 4 (bytes)
fordi det er omtrent ett ord
