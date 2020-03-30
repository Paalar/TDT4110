def wholeNumber():
    numa = eval(input("Gi meg et tall!\n"))
    if type(numa) == int:
        print("Dette er et heltall.")
    elif type(numa) == float:
        print("Dette er ikke et heltall.")

wholeNumber()

def evenNumber():
    numb = eval(input("\nGi meg enda et tall!\n"))
    if type(numb/2) == int:
        print("Dette er et partall.")
    elif type(numb/2) == float:
        print("Dette er et oddetall.")

evenNumber()

def ayNumber():
    numc = eval(input("\nGi meg et tredje tall!\n"))
    if numc >= 0:
        print("Dette er et positivt tall.")
    elif numc < 0:
        print("Dette er et negativt tall.")

ayNumber()

def compareNr():
    print("\nNå skal vi sammenligne to tall.")
    numd = eval(input("Gi meg et tall.\n"))
    nume = eval(input("Gi meg enda et tall.\n"))
    if numd > nume:
        print(False)
    elif numd < nume:
        print(False)
    else:
        print(True)

compareNr()
