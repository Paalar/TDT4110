
mynter = [20, 10, 1, 1, 5, 10]
mynerx = [12, 23, 34, 45, 56, 67, 78, 89, 90, 98, 87, 65, 54, 43, 32, 21]

def count_coins(coins):
    kroner = 0
    for i in coins:
        kroner += i
    return kroner

#print(count_coins(mynter))


def num_coins(numbers):
    mynterlist = []
    tjuere = 0
    tiere = 0
    femere = 0
    enere = 0
    for i in numbers:
        while i - 20 >= 0:
            tjuere += 1
            i = i - 20
        mynterlist.append(tjuere)
        while i - 10 >= 0:
            tiere += 1
            i = i - 10
        mynterlist.append(tiere)
        while i - 5 >= 0:
            femere += 1
            i = i - 5
        mynterlist.append(femere)
        while i - 1 >= 0:
            enere += 1
            i = i -1
        mynterlist.append(enere)
    return mynterlist


def check_weights(list1):
    weights = [9.9, 6.8, 7.85, 4.35]
            #20,  10,  5,   1
    vekt = []
    for i in range(len(weights)):
        vekter = (list1[i]*weights[i])
        vekter = ("%.2f" % vekter)
        vekt.append(float(vekter))

    print(vekt)


#(num_coins([55]))
check_weights(num_coins([63, 55]))
