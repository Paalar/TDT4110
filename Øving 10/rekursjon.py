from random import randint

sumn = 0
x = 1
def recursive_sum(n):
    global sumn
    global x
    sumn += x
    #print(sumn)
    if x == n:
        return sumn
    else:
        x += 1
        recursive_sum(n)

#print(recursive_sum(10))

rannum = []
nummer = [9, 8, 1, 2, 7, 5, 4, 6, 0, 3]
for i in range(1, 20):
    rannum.append(randint(1, 10))

#print(rannum)
lengde = 0

def find_smallest_element(numbers):
    global lengde
    print(numbers)
    if lengde == 1:
        return numbers
    lengde = 0
    for i in numbers:
        for x in numbers:
            if x > i:
                print(x, i, numbers)
                numbers.remove(x)
    for i in numbers:
        lengde += 1
    if lengde-1 > 0:
        if numbers[0] == numbers[lengde-1]:
            numbers.remove(numbers[0])

    find_smallest_element(numbers)


#print (find_smallest_element(rannum))
#print(find_smallest_element(nummer))
#print(rannum)
#print (find_smallest_element([2, 6, 0]))


rannum = []
for i in range(1, 20):
    rannum.append(randint(1, 10))


def binary_search(numbers, element):
    print(numbers)
    lengde = 0
    for i in numbers:
        lengde += 1
    #print (lengde)
    half = lengde//2
    #print(half)
    vhalve = numbers[:half]
    hhalve = numbers[half:]
    hlengde = lengde - half
    #print (vhalve[half-1])
    print ("venstre",vhalve, "høyere", hhalve)
    print("dette er halvparten", half)
    try:
        if vhalve[half-1] == element:
            print (True)
        elif hhalve[hlengde-1] == element:
            print(True)
        elif element <= vhalve[half-1]:
            print("Venstre del av første liste")
            binary_search(vhalve, element)
        elif vhalve[half-1] <= element:
            print("Høyere del av første liste")
            binary_search(hhalve, element)
    except IndexError:
        print("Tallet finnes ikke i lista")

#print(binary_search(sorted(rannum), 2))



def binary_search1(numbers, element):
    print(numbers)
    if len(numbers) == 0:
        print("Tallet finnes ikke i listen")
        return -float('inf')
    lengde = (len(numbers)-1)//2
    print (lengde, numbers[lengde])
    if numbers[lengde] == element:
        print("Indeksen til elementet {0} er {1}".format(element, lengde))
        return lengde
    elif numbers[lengde] > element:
        print("venstre side")
        return binary_search1(numbers[0:lengde], element)
    elif numbers[lengde] < element:
        print("høyere side")
        return (lengde+1) + binary_search1(numbers[lengde+1:], element)


def binary_search2(numbers, element, start, stop):
    if start > stop:
        return -float('inf')
    mid = (start + stop)//2
    if element < numbers[mid]:
        return binary_search2(numbers, element, start, mid-1)
    elif element > numbers[mid]:
        return binary_search2(numbers, element, mid+1, stop)
    else:
        return mid



print(binary_search1(sorted(rannum), 8))
#print(binary_search2(sorted(rannum), 8, 0, len(rannum) -1))
