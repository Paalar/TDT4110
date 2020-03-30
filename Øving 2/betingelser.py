a = eval(input("Skriv inn et tall.\n"))
b = eval(input("Skrv inn enda et tall.\n"))
c = a*b
d = a+b

if a*b > a+b:
    print("{0}*{1} = {2}, Er større enn {0}+{1} = {3} \n Det minste tallet er {3}".format(a, b, c, d))
elif a*b < a+b:
    print("{0}+{1} = {3}, Er større enn {0}*{1} = {2} \n Det minste tallet er {2}".format(a, b, c, d))

e = eval(input("Hva er 3*4?\n"))

if e == 12:
    print("Det er riktig!")
else:
    print("Dette var feil :(")
