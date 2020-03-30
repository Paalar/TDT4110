x = "Jeg har vært en slem gutt."
import random

#y = random.randint(1, 100)
#z = int(input("Gi meg et heltall mellom 1 og 100\n"))

#while z != y:
#    print ("Dette var feil")
#    if y>z:
#        print ("tallet ditt var litt for lite.")
#        z = int(input("Gi meg et heltall mellom 1 og 100\n"))
#    elif y<z:
#        print ("Tallet ditt var litt for stort")
#        z = int(input("Gi meg et heltall mellom 1 og 100\n"))

#print ("Yay tallet ditt var riktig, tallet er: ", y)

z = 0
for y in range (1,4):
    for x in range (1,10):
        z = x * y
        print (z)
