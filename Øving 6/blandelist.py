liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [6, 5, 4, 3, 2, 1]
liste3 = [6, 5, 4, 4, 5, 6]
liste4 = [1, 2, 3, 3, 2, 1]

def isSixAtEdge(listen):
    if listen[0] == 6 or listen[-1] == 6:
        return True
    else:
        return False

#print(isSixAtEdge(liste1))
#print(isSixAtEdge(liste2))
#print(isSixAtEdge(liste3))
#print(isSixAtEdge(liste4))


def average(enliste):
    average = sum(enliste)/len(enliste)
    return average

#print(average(liste1))


oddliste = [1, 9, 2, 8, 3, 7, 4, 6, 5]
# sortert = [1, 2, 3, 4, 5, 6, 7, 8, 9] der 5 er medianen.
def median(enliste):
    listesort = sorted(enliste)
    length = len(listesort)
    if length < 1:
        return False
    elif length == 1:
        return enliste[0]
    elif length % 2 == 0:
        median = (enliste[int(length/2)] + enliste[int(length/2)-1])/2
        return median
    else:
        median = enliste[int(length/2)]
        return median

print(median(oddliste))
