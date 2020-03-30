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

Msg1 = ("Msg 1")
Msg2 = ("Msg 2")
Msg3 = ("Msg 3")
Msg4 = ("Msg 4")
Msg5 = ("Msg 5")
Msg6 = ("Msg 6")

MeldingX = "navn"
TidX = strftime("%H:%M:%S", gmtime())

def logg():
    print(Msg1 + ", Klokken", Tid1, "Sendte", Navn1, Melding1)
    print(Msg2 + ", Klokken", Tid2, "Sendte", Navn2, Melding2)
    print(Msg3 + ", Klokken", Tid3, "Sendte", Navn3, Melding3)
    print(Msg4 + ", Klokken", Tid4, "Sendte", Navn1, Melding4)
    print(Msg5 + ", Klokken", Tid4, "Sendte", Navn1, Melding5)
    print(Msg6 + ", Klokken", Tid4, "Sendte", Navn3, Melding6)

def main():
    logg()

main()
