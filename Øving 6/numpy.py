#import numpy as np
#from time import sleep

ikkeunik = ["ITGK", "ITGK"]
unik = [1, 2, 3]
inA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
inB = [10, 30, 50, 70, 90, 110, 130, 150, 170]
#inA = [100, 60, 10, 30, 90, 40, 80, 20, 70, 50]
#inB = [170, 10, 150, 30, 130, 50, 110, 70, 90]

def allUnique(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
print(allUnique(ikkeunik)) # Prints False
print(allUnique(unik)) # Prints True


def removeDuplicates(lst):
    return list(set(lst))
print(removeDuplicates(ikkeunik)) # Prints ['ITGK']
print(removeDuplicates(unik)) # Prints [1, 2, 3]


def inAbutnotB(a,b):
    inAnotB = (list(set(a)-set(b)))
    inAnotB.sort()
    return inAnotB
print(inAbutnotB(inA, inB)) # Prints [20, 40, 60, 80, 100], men hvis ikke .sort så printer den [60, 80, 100, 20, 40], hvorfor?
print(inAbutnotB(inB, inA)) # Prints [110, 130, 150, 170], men hvis ikke .sort så printer den [170, 130, 150, 110]

#valg1 = input("Hvilken liste vil du bruke? ikkeunik eller unik. ikkeunik inneholder ikke unike elementer mens unik inneholder bare unike elementer.\n")
#sleep(1)

#if valg1 == "ikkeunik":
#    print(allUnique(ikkeunik))
#elif valg1 == "unik":
#    print(allUnique(unik))
