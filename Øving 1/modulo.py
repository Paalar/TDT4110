x = ("Hello world.")

print (x + "\nNå skal du skrive inn to gyldige tall og så finner jeg restverdien til disse to tallene")

NumberA = int(input("Skriv inn et tall: "))

while NumberA == 0:
    print("Dette tallet er ikke gyldig")
    NumberA = int(input("Skriv inn et gyldig tall som ikke er null: "))
#    try:
#        NumberA = int(input("Skriv inn et gyldig tall som ikke er null: "))
#    except ValueError:
#        pass

NumberB = int(input("Skriv inn enda et tall: "))
while NumberB == 0:
    print("Dette tallet er ikke gyldig")
    NumberB = int(input("Skriv inn et tall som ikke er null, man kan ikke dele på null: "))

if NumberB > NumberA:
    print("Det første tallet må være større enn det siste")
else:
    print ("Restverdien er ", + NumberA%NumberB)
