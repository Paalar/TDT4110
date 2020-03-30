from random import randint
listex = []
for i in range(20):
    random = randint(0,20)
    listex.append(random)
print(listex)
x = [10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]



def bubble_sort(listen):
    for y in range(len(listen)-1): #for y i {20-1 =} 19, 0, -1// for y in range(19, 0 , -1)
        for i in range(len(listen)-1-y): #for i i range y = 0, 20, så i i range 0, 19, så i i range 0, 18, osv.
            if listen[i] > listen[i+1]: #hvis lsiten[0] er større enn listen[1], hvis listen[1] er større enn listen [2]
                listen[i], listen[i+1] = listen[i+1], listen[i] # bytter dem plass
                print (listen)
    return listen


#print(bubble_sort(listex))

def selection_sort(listen):
    sortedlist = []
    for x in range(len(listen)):
        maxvalue = 0
        for i in listen:
            if i >= maxvalue:
                maxvalue = i
        sortedlist.append(maxvalue)
        y = listen.index(maxvalue)
        del listen[y]
        print(listen, sortedlist)
    return sortedlist

print(selection_sort(listex))
