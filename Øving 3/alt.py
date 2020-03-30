n = int(input("Hva skal n være?\n"))
#m = n
i = 1
Liste1 = []

while i<=n:
    Liste1.append(i**2)

print(sum(Liste1))


#for x in range(n):
#    m -= 1
#    if m % 2 == 0:
#        y1 = (n)**2
#        n -= 1
#        print (y1)
#    elif m % 2 != 0:
#        y2 = (n)**2
#        n -= 1
#        print (-y2)
