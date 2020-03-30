from random import randint

def randList(size, lower_bound, upper_bound):
    randomlist = []
    for i in range(size):
        rannuminterval = randint(lower_bound, upper_bound)
        randomlist.append(rannuminterval)
    return randomlist

#print(sorted(randList(10, 0, 10)))

listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listy = [2, 4, 6, 8, 10, 12, 14, 16, 18]

def compareLists(list1, list2):
    print(sorted(list1))
    print(sorted(list2))
    alikenumbers = []
    for i in range(len(list1)):
        if list1[i] in list1 and list1[i] in list2:
            alikenumbers.append(list1[i])
    return(alikenumbers)

print(sorted(compareLists(randList(10, 0, 10), randList(10, 0, 10))))

#alikenumbers = []
#for i in range(len(listx)):
#    if listx[i] in listx and listx[i] in listy:
#        alikenumbers.append(listx[i])
#print(alikenumbers)
