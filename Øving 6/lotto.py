from random import randint

numbers = []
my_guess = []
my_guess_tillegg = []
lol = []

for i in range(1, 35, 1):
    numbers.append(i)
 
def myGuess():
    global my_guess
    for i in range(0,7):
        my_guess.append(int(input("Gi meg 7 tall: ")))
#    if set(my_guess) & set(my_guess_tillegg) == True:
#        for k, l in (set(my_guess) & set(my_guess_tillegg).iteritiems()):
#            lol = [k, l]
#            my_guess_tillegg.append(lol)
#            my_guess_tillegg.remove(set(my_guess) & set(my_guess_tillegg))
#            print(my_guess_tillegg)
#            if len(my_guess_tillegg) > 3:
#                pass
#            elif len(my_guess_tillegg) < 3:
#                liketall()
    return my_guess

def myGuessTilegg():
    for i in range(0,3):
        my_guess_tillegg.append(int(input("Gi meg 3 tilleggstall: ")))
    return my_guess_tillegg

def numbersn(n):
    r_numbers = []
    num = randint(1,34)
    for i in range(0, n):
        while len(r_numbers) < n:
            num = randint(1,34)
            if num not in r_numbers:
                r_numbers.append(num)
                numbers.remove(num)
    r_numbers.sort()
    print(r_numbers)
    return r_numbers


def compList(liste1, liste2):
    print("Dine tall er", liste1)
    liste1 = set(liste1)
    liste2 = set(liste2)
    liketall = liste1 & liste2
    liketall1 = list(liketall)

    print("Dine riktige tall er", liketall1)
    return liketall1


randomnum = (numbersn(7))
riktige = compList(myGuess(), randomnum)
ekstrariktige = compList(myGuessTilegg(), randomnum)
if len(riktige) == 7:
    print("Du har vunnet kr 2 749 455. Tallene var", riktige)
elif len(riktige) == 6 and (len(ekstrariktige) == 1 or len(ekstrariktige) == 2 or len(ekstrariktige) == 3):
    print("Du har vunnet kr 102 110. Tallene var", riktige, ekstrariktige)
elif len(riktige) == 6:
    print("Du har vunnet kr 3 385. Tallene var", riktige)
elif len(riktige) == 5:
    print("Du har vunnet kr 95. Tallene var", riktige)
elif len(riktige) == 4 and (len(ekstrariktige) == 1 or len(ekstrariktige) == 2 or len(ekstrariktige) == 3):
    print("Du har vunnet kr 45. Tallene var", riktige, ekstrariktige)
else:
    print("Sorry, men du har tapt")
