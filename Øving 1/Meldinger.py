    #print("Klokken", TidX, "sendte", NavnX, "følgende melding: ", MeldingX )

from datetime import datetime
from time import strftime, gmtime
Navn1 = ("Mr. Y")
Navn2 = ("Mdm. Evil")
Navn3 = ("Dr. Horrible")

Tid1 = ("23:59")
Tid2 = ("0:00")
Tid3 = ("0:03")
Tid4 = ("0:09")

Melding1 = ("Har du mottatt pakken?")
Melding2 =("Ja. Pakken er mottatt.")
Melding3 = ("All you need is love!")
Melding4 = ("Dr. Horrible, Dr. Horrible, calling Dr. Horrible.")
Melding5 = ("Dr. Horribble, Dr. Horrible wake up now.")
Melding6 = ("Up now!")

MeldingX = "navn"
TidX = strftime("%H:%M:%S", gmtime())

n = 1

def logg(Tid, Navn, Melding):
    global n
    print("Msg", n , "Klokken {0} sendte {1} følgende melding: \"{2}\"\n" .format(Tid, Navn, Melding))
    n = n+1


def main():
    logg(Tid1, Navn1, Melding1)
    logg(Tid2, Navn2, Melding2)
    logg(Tid3, Navn3, Melding3)
    logg(Tid4, Navn1, Melding4)
    logg(Tid4, Navn1, Melding5)
    logg(Tid4, Navn3, Melding6)

main()
