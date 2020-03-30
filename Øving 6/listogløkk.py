number_list = []
sumnum = 0


for i in range(0, 100):
    number_list.append(i)
    if i % 3 == 0 or i % 10 == 0:
        sumnum += i
print("vanlig liste fra 0 til 99", number_list)
print("summen av alle tallene i lista", sumnum)


number_listeven = number_list[0:100:2]
#print (number_listeven)
number_listodd = number_list[1:100:2]
#print (number_listodd)

for i in number_listeven:
    number_listodd.insert(i+1, i)
print("Endret rekkefølge på listen", number_listodd)



def reverselist(liste):
    reversenum = []
    num = -1
    for i in liste:
        m = liste[num]
        reversenum.append(m)
        num -= 1
    return reversenum

print("reversert lista", reverselist(number_listodd))
