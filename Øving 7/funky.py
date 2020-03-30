from random import randint
from statistics import mode

random_numbers = []
for i in range(100):
    random_numbers.append(randint(0,9))

tallet2 = 0
for i in random_numbers:
    if i == 2:
        tallet2 += 1
#print(tallet2)

sumrand = 0
for i in random_numbers:
    sumrand += i
#print(sumrand)

sortert = sorted(random_numbers)
#print(sortert)


#print (mode(random_numbers))
reversrand = []
for i in sortert:
    reversrand.append(i)
reversrand.reverse()

print(sortert)
print(reversrand)


#print (reversed(sorted(random_numbers)))
