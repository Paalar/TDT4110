import random
print("Snart skal du gjette mellom 2 tall. Skriv hva det høyeste tallet skal være, det laveste starter på 0")
x = int(input(""))
tilfeldig_tall = random.randint(0, x)

print("Nå skal du gjette på et tilfeldig tall mellom det tallet du skrev inn og 0")
z = int(input(""))

while tilfeldig_tall != z:
    if z > tilfeldig_tall:
        print("Du gjettet for høyt, prøv igjen")
        z = int(input(""))
    elif z < tilfeldig_tall:
        print("Du gjettet for lavt, prøv igjen")
        z = int(input(""))
    else:
        pass

print("Gratulerer, du gjettet riktig!")
