def studie(filename):
    f = open(filename, "r")
    r = f.read()
    for i in r:
        #if i == "Alle":
        print (i)
    #return r

print(studie("poenggrenser_2011.csv"))
