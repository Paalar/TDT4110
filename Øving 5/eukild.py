def errora():
    try:
        while True:
            a = int(input("Gi meg et heltall a:     "))
            if a == 0:
                print("0 er ikke gyldig.")
                a = int(input("Gi meg et heltall a:     "))
            return a
    except (NameError, ValueError):
            print("a var ikke et gyldig heltall.")
            errora()

def errorb():
    try:
        while True:
            b = int(input("Gi meg et heltall b:     "))
            if b == 0:
                print("0 er ikke gyldig.")
                b = int(input("Gi meg et heltall b:     "))
            return b
    except (NameError, ValueError):
            print("b var ikke et gyldig heltall.")
            errorb()

def eukild(a, b):
    while b:
        a, b = b, a%b
    return a, b


def reduce_fraction(c, d):
    a, b = eukild(c, d)
    print (a, "/", b)



reduce_fraction(errora(), errorb())
